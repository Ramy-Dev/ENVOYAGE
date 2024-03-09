<main>
<header class="section hero text-primary bg-primary">
   <div class="cover position-absolute"></div>
   <div class="cover-img"></div>
   <div class="containerHome container index text-center mt-6 position-relative">
      <h1 class="text display-2 fw-semibold">OUANIS</h1>
      <p class="text lead pl-2 mb-6 py-6 fs-3 fw-normal">
         le meilleur choix pour envoyer les colis
      </p>
      <a href="/sign-up" class="btn btn-lg btn-primary mt-6">
         <strong>ENVOYER un colis</strong>
      </a>
   </div>

  
</header>

<div class="container mt-5 work section">
   <h2 class="textStartHome text display-4 text-center fw-semibold">START</h2>
   <div class="row p-6 gx-5">
      <div class="col">
         <div class="card">
            <div class="card-body bg-primary rounded text-white">
               <div class="content p-5 pb-4 cardHome">
                  <h3 class="text text-white text-center mb-4">
                     Sender
                  </h3>
                  <p class="text card-text">
                     Lorem ipsum leo risus, porta ac consectetur ac, vestibulum
                     at eros. Donec id elit non mi porta gravida at eget metus.
                     Cum sociis natoque penatibus et magnis dis parturient
                     montes, nascetur ridiculus mus. Cras mattis consectetur
                     purus sit amet fermentum.
                  </p>
                  <div class="d-grid">
                     <a class="btn btn-primary fw-bold" href="/log-in">login</a>
                  </div>
               </div>
            </div>
         </div>
      </div>
      <div class="col">
         <div class="card ">
            <div class="card-body bg-primary rounded text-white">
               <div class="content p-5 pb-4 cardHome">
                  <h3 class="text text-white text-center mb-4">
                     Travler
                  </h3>
                  <p class="text card-text">
                     Lorem ipsum leo risus, porta ac consectetur ac, vestibulum
                     at eros. Donec id elit non mi porta gravida at eget metus.
                     Cum sociis natoque penatibus et magnis dis parturient
                     montes, nascetur ridiculus mus. Cras mattis consectetur
                     purus sit amet fermentum.
                  </p>
                  <div class="d-grid">
                     <a class="btn btn-primary fw-bold" href="/log-in">login</a>
                  </div>
               </div>
            </div>
         </div>
      </div>
   </div>
</div>
<section class="about">
   <div class="row">
      <div class="col my-auto">
         <div class="hero-head">
            <h1 class="row textAboutHome fw-bolder">ABOUT</h1>
         </div>
         <div class="pt-6">
            <div class="col paragrapheAboutHome">
               <p class="text fw-semibold fs-4 text-primary">Half height hero</p>
               <p class="text">
                  Lorem ipsum dolor, sit amet consectetur adipisicing elit. Modi
                  laboriosam atque enim voluptas iure ratione temporibus, quod
                  aperiam exercitationem quia numquam illo quis dolore autem.F
               </p>
            </div>
         </div>
      </div>
      <div class="col imageAboutHome">
         <img src="" class="p-6" alt="Image Delivary" />
      </div>
   </div>
</section>
<section class="hero pl-6 pt-3 bg-light contact"></section>
</main>
<style>
  
   header {
      margin-top: 0;
      position: relative;
      height: 90vh;
   }
   .text{
      font-family: "Poppins" , sans-serif;
   }


   .containerHome {
   position: absolute; /* Changement en position absolue */
   top: 42%; /* Déplace le containerHome à 50% du haut du header */
   transform: translateY(-50%); /* Centre le containerHome verticalement */
   left: 0; /* Aligne le containerHome à gauche */
   right: 0; /* Aligne le containerHome à droite */
   /* background-color: black; */
   min-height: 55vh;
   width: 100%; /* Ajuste la largeur au container parent */
   display: flex;
   flex-direction: column;
   align-items: center;
   gap: 70px;
   place-content: center;
}

   .containerHome a {
      margin-top: 30px;
      padding: .85rem 1.8rem;
   }

   .textStartHome{
      color: #4A4A4A;
      margin-top: 75px;
      margin-bottom: 50px;
   }
   .cardHome {
      align-items: center;
    display: flex;
    flex-direction: column;
   }
   .cardHome a{
      background-color: #FFE767;
      color : #27005D;
      padding: .65rem 1.25rem;
   }
   .about{
      padding: 50px;
      margin-top: 75px;
      background-color: #F5F5F5;
   }

   .textAboutHome {
      color: #4A4A4A;
      margin-bottom: 50px;
   }
   .paragrapheAboutHome {
      padding-left: 20px;
   }

   .imageAboutHome {
      display: flex;
      justify-content : center;
   }
   </style>
   