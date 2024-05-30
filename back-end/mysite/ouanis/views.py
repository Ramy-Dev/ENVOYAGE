from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator

from .models import (
    Utilisateur, DemandeDeCompteVoyageur,
    Annonce, DemandeAnnonce, Tag, AnnonceTag, Palier, AnnoncePalier
)
from .serializers import (
    UserRegistrationSerializer, UtilisateurSerializer, DemandeDeCompteVoyageurSerializer, 
    AnnonceSerializer, DemandeAnnonceSerializer,  PasswordResetRequestSerializer, PasswordResetConfirmSerializer,
    TagSerializer, AnnonceTagSerializer, PalierSerializer, AnnoncePalierSerializer
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken


class PasswordResetRequestView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = Utilisateur.objects.filter(email=email).first()
            if user:
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                reset_link = f"{request.scheme}://{request.get_host()}/reset_password_confirm/{uid}/{token}/"
                send_mail(
                    'Password Reset Request',
                    f'Click the link to reset your password: {reset_link}',
                    'from@example.com',
                    [user.email],
                    fail_silently=False,
                )
            return Response({"message": "Password reset link has been sent to your email."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PasswordResetConfirmView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, uidb64, token):
        serializer = PasswordResetConfirmSerializer(data=request.data)
        if serializer.is_valid():
            try:
                uid = force_str(urlsafe_base64_decode(uidb64))
                user = Utilisateur.objects.get(pk=uid)
            except (TypeError, ValueError, OverflowError, Utilisateur.DoesNotExist):
                user = None

            if user is not None and default_token_generator.check_token(user, token):
                user.set_password(serializer.validated_data['new_password'])
                user.save()
                return Response({"message": "Password has been reset successfully."}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Invalid token or user ID."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        username = self.request.query_params.get('username', None)
        if username is not None:
            user = get_object_or_404(Utilisateur, username=username)
            return Utilisateur.objects.filter(username=user.username)
        return Utilisateur.objects.all()
    def get_queryset(self):
        return Utilisateur.objects.filter(id=self.request.user.id)





class DemandeDeCompteVoyageurViewSet(viewsets.ModelViewSet):
    queryset = DemandeDeCompteVoyageur.objects.all()
    serializer_class = DemandeDeCompteVoyageurSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return DemandeDeCompteVoyageur.objects.filter(user=self.request.user)
    
    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        demande = self.get_object()
        demande.est_approuve = True
        demande.save()
        return Response({'status': 'Demande approuvée'}, status=status.HTTP_200_OK)



class AnnonceViewSet(viewsets.ModelViewSet):
    queryset = Annonce.objects.all()
    serializer_class = AnnonceSerializer
    permission_classes = [IsAuthenticated]



class DemandeAnnonceViewSet(viewsets.ModelViewSet):
    queryset = DemandeAnnonce.objects.all()
    serializer_class = DemandeAnnonceSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def accept(self, request, pk=None):
        demande = self.get_object()
        demande.statut = 'accepte'
        demande.save()
        return Response({'status': 'Demande acceptée'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def reject(self, request, pk=None):
        demande = self.get_object()
        demande.statut = 'rejete'
        demande.save()
        return Response({'status': 'Demande rejetée'}, status=status.HTTP_200_OK)

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]

class AnnonceTagViewSet(viewsets.ModelViewSet):
    queryset = AnnonceTag.objects.all()
    serializer_class = AnnonceTagSerializer
    permission_classes = [IsAuthenticated]

class PalierViewSet(viewsets.ModelViewSet):
    queryset = Palier.objects.all()
    serializer_class = PalierSerializer
    permission_classes = [IsAuthenticated]

class AnnoncePalierViewSet(viewsets.ModelViewSet):
    queryset = AnnoncePalier.objects.all()
    serializer_class = AnnoncePalierSerializer
    permission_classes = [IsAuthenticated]

# Custom view to handle user registration
class UserRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"user": serializer.data, "token": Token.objects.get(user=user).key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Custom view to handle user login
class UserLoginView(ObtainAuthToken):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.pk, 'email': user.email})
