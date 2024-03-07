<script>

      const toggle = () => {
         let tr = document.getElementById("tr")
         let sn = document.getElementById("sn")
         
         tr.classList.toggle("hidden")
         sn.classList.toggle("hidden")
         
         // rah ndir toggle bin class hidden ila kant nhiha il mkantch zidha
      }


</script>

<main>
   <div class="bd">
      <div id="tr" class="singup hidden tr m-auto">
        <div class="container">
          <div class="row">
            <div class="col p-0">
              <div class="d-flex flex-row">
                <button type="button" on:click={toggle} class="sender btn btn-primary py-3 w-50 m-0 rounded-0 is-selected">Sign up as Sender</button>
                <button class="travler btn btn-light py-3 w-50 m-0 rounded-0" style="border: 1px solid #fff;">Traveler</button>
              </div>
            </div>
          </div>
        </div>
        <form class="box">
          <div class="row">
            <div class="col-md-6">
              <div class="form-group">
                <label for="nom">Nom</label>
                <input type="text" class="form-control" id="nom" placeholder="Nom">
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-group">
                <label for="prenom">Prénom</label>
                <input type="text" class="form-control" id="prenom" placeholder="Prénom">
              </div>
            </div>
          </div>
          <div class="form-group">
            <label for="adresse">Address</label>
            <input type="text" class="form-control" id="adresse" placeholder="Address">
          </div>
          <div class="form-group">
            <label for="ddn">Date de naissance</label>
            <input type="date" class="form-control" id="ddn">
          </div>
          <div class="form-group">
            <label for="passport">Passport</label>
            <input type="file" class="form-control-file" id="passport">
          </div>
          <div class="form-group">
            <label for="email">Email</label>
            <input type="email" class="form-control" id="email" placeholder="Email">
          </div>
          <div class="form-group">
            <label for="password">Mot de passe</label>
            <input type="password" class="form-control" id="password" placeholder="**************">
          </div>
          <div class="form-group">
            <label for="ConfirmPassword">Confirmer le mot de passe</label>
            <input type="password" class="form-control" id="ConfirmPassword" placeholder="**************">
          </div>
          <div class="d-flex justify-content-center">
            <button type="submit" class="btn btn-primary btn-block mt-4">Sign in</button>
          </div>
        </form>
      </div>
      <div id="sn" class="singup sn m-auto">
        <div class="container">
          <div class="row">
            <div class="col p-0">
              <div class="d-flex flex-row">
                <button class="sender btn btn-primary py-3 w-50 m-0 rounded-0 is-selected">Sign up as Sender</button>
                <button type="button" on:click={toggle} class="travler btn btn-light py-3 w-50 m-0 rounded-0" style="border: 1px solid #fff;">Traveler</button>
              </div>
            </div>
          </div>
        </div>
        <form class="box has-background-primary">
          <div class="row">
            <div class="col-md-6">
              <div class="form-group">
                <label for="Sender-nom">Nom</label>
                <input type="text" class="form-control" id="Sender-nom" placeholder="Nom">
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-group">
                <label for="Sender-prenom">Prénom</label>
                <input type="text" class="form-control" id="Sender-prenom" placeholder="Prénom">
              </div>
            </div>
          </div>
          <div class="form-group">
            <label for="Sender-email">Email</label>
            <input type="email" class="form-control" id="Sender-email" placeholder="E-mail">
          </div>
          <div class="form-group">
            <label for="Sender-password">Mot de passe</label>
            <input type="password" class="form-control" id="Sender-password" placeholder="**************">
          </div>
          <div class="form-group">
            <label for="Sender-ConfirmPassword">Confirmer le mot de passe</label>
            <input type="password" class="form-control" id="Sender-ConfirmPassword" placeholder="**************">
          </div>
          <div class="d-flex justify-content-center">
            <button type="submit" class="btn btn-primary btn-block mt-4">Sign in</button>
          </div>
        </form>
      </div>
    </div>
</main>

