<main>

<div class="container bd">
   <div class="login mx-auto">
       <div class="box p-0">
           <button id="" class="login-btn sender btn-block bg-primary text-white fw-bolder fs-5 border-0 w-100 py-3 mb-0">Log in</button>
       </div>
       <div class="container container-form">
       <form class="box">
           <div class="form-group">
               <label for="email">E-mail :</label>
               <input type="email" class="form-control" id="email" required>
           </div>
           <div class="form-group">
               <label for="password">Mot de passe :</label>
               <input type="password" class="form-control" id="password" required>
           </div>
           <div class="text-center mt-4">
               <button class="submitLogin border-0 bg-primary text-white fw-bolder mt-3">Log in</button>
           </div>
       </form>
    </div>
   </div>
</div>    

</main>

<style>

    .login {
        background-color: #fff;
        border-radius: 20px;
        box-shadow:
      #a186ff -5px 5px,
      #d0c2ff -10px 10px,
      #e6e0f9 -15px 15px,
      rgba(0, 0, 0, 0.1) -10px 10px,
      rgba(0, 0, 0, 0.05) -0 0;
    }
    .login label {
    color: black;
    font-weight: 650;
    margin-top: 20px;

  }

  input {
    border: none;
    border-radius: 20px;
    background-color: #F0F0F0;
  }
  .container-form {
        padding: 25px;
  }
    .login-btn {
        border-top-left-radius: 20px;
        border-top-right-radius: 20px;
    }

    .submitLogin {
        border-radius: 20px;
    padding: 7px 50px;
    }

</style>