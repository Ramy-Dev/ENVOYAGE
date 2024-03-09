<script>
  const toggle = () => {
    let tr = document.getElementById("tr");
    let sn = document.getElementById("sn");

    tr.classList.toggle("hidden");
    sn.classList.toggle("hidden");

    // rah ndir toggle bin class hidden ila kant nhiha il mkantch zidha
  };
</script>

<main>
  <div class="bd">
    <div id="sn" class="singup sn bg-primary m-auto">
      <div class="card-shadow">
        <div class="container">
          <div class="row">
            <div class="col p-0">
              <div class="d-flex flex-row">
                <button
                  class="sender-btn bg-primary border-0 text-white fs-4 fw-semibold py-3 w-50 m-0 is-selected"
                  >Sign up as Sender</button
                >
                <button
                  type="button"
                  on:click={toggle}
                  class="travler-btn bg-white border-0 text-primary fs-4 fw-semibold py-3 w-50 m-0"
                  style="border: 1px solid #fff;">Traveler</button
                >
              </div>
            </div>
          </div>
        </div>
        <form class="box has-background-primary">
          <div class="row">
            <div class="col-md-6">
              <div class="form-group">
                <label for="Sender-nom">Nom :</label>
                <input type="text" class="form-control" id="Sender-nom" required/>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-group">
                <label for="Sender-prenom">Prénom :</label>
                <input type="text" class="form-control" id="Sender-prenom" required/>
              </div>
            </div>
          </div>
          <div class="form-group">
            <label for="Sender-email">Email :</label>
            <input type="email" class="form-control" id="Sender-email" required/>
          </div>
          <div class="row">
            <div class="col-md-6">
              <div class="form-group">
                <label for="Sender-password">Mot de passe :</label>
                <input type="password" class="form-control" id="Sender-password" required/>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-group">
                <label for="Sender-ConfirmPassword"
                  >Confirmer le mot de passe :</label
                >
                <input type="password" class="form-control" id="Sender-ConfirmPassword" required/>
              </div>
            </div>
          </div>
          <div class="d-flex justify-content-center">
            <button
              type="submit"
              class="submitSignupSender border-0 bg-white text-primary fw-bolder mt-5"
              >sign up</button
            >
          </div>
        </form>
      </div>
    </div>
    <div id="tr" class="singup hidden tr m-auto">
      <div class="card-shadow">
        <div class="container">
          <div class="row">
            <div class="col p-0">
              <div class="d-flex flex-row">
                <button
                  type="button"
                  on:click={toggle}
                  class="sender-btn bg-primary border-0 text-white fs-4 fw-semibold py-3 w-50 m-0 is-selected"
                  >Sender</button
                >
                <button
                  class="travler-btn bg-white border-0 text-primary fs-4 fw-semibold py-3 w-50 m-0"
                  style="border: 1px solid #fff;">Sign up as Traveler</button
                >
              </div>
            </div>
          </div>
        </div>
        <form class="box">
          <div class="row">
            <div class="col-md-6">
              <div class="form-group">
                <label for="nom">Nom :</label>
                <input type="text" class="form-control" id="nom" required/>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-group">
                <label for="prenom">Prénom :</label>
                <input type="text" class="form-control" id="prenom" required/>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-md-6">
              <div class="form-group">
                <label for="adresse">Adresse :</label>
                <input type="text" class="form-control" id="adresse" required/>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-group">
                <label for="ddn">Date de naissance :</label>
                <input type="date" class="form-control" id="ddn" required/>
              </div>
            </div>
          </div>
          <div class="form-group">
            <label for="passport">Passport :</label><br />
            <input type="file" class="form-control" id="passport" required/>
          </div>
          <div class="form-group">
            <label for="email">Email :</label>
            <input type="email" class="form-control" id="email" required/>
          </div>
          <div class="row">
            <div class="col-md-6">
              <div class="form-group">
                <label for="password">Mot de passe :</label>
                <input type="password" class="form-control" id="password" required/>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-group">
                <label for="ConfirmPassword">Confirmer le mot de passe :</label>
                <input type="password" class="form-control" id="ConfirmPassword" required/>
              </div>
            </div>
          </div>
          <div class="d-flex justify-content-center">
            <button
              type="submit"
              class="submitSignupTravler border-0 bg-primary text-white fw-bolder mt-5">Sign in</button
            >
          </div>
        </form>
      </div>
    </div>
  </div>
</main>

<style>
  .sn {
    /* background-color: blue; */
    border-radius: 20px;
    align-items: center;
  }
  .card-shadow {
    border-radius: 20px;
    box-shadow:
      #a186ff -5px 5px,
      #d0c2ff -10px 10px,
      #e6e0f9 -15px 15px,
      rgba(0, 0, 0, 0.1) -10px 10px,
      rgba(0, 0, 0, 0.05) -0 0;
  }

  form {
    padding: 20px;
  }
  label {
    font-weight: 650;
    margin-top: 20px;
  }
  .sn label {
    color: white;
  }
  .tr label {
    color: black;
  }
  input {
    border: none;
    border-radius: 20px;
  }
  .sn input {
    background-color: white;
  }
  .tr input {
    background-color: #f0f0f0;
  }
  .sender-btn {
    border-top-left-radius: 20px;
  }
  .travler-btn {
    border-top-right-radius: 20px;
  }
  .submitSignupSender {
    border-radius: 20px;
    padding: 7px 50px;
  }
  .submitSignupTravler {
    border-radius: 20px;
    padding: 7px 50px;
  }
</style>
