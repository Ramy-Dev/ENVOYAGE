<main>
  <header class="section text-white bg-white">
    <div class="cover-recherche position-absolute"></div>
    <div class="cover-img"></div>
    <div
      class="containerRecherche container index text-center position-relative"
    >
      <h1 class="display-3 fw-semibold">
        Trouvez votre nouveau<br />facteur !
      </h1>
      <p class="pl-2 mb-6 py-6 fs-4 fw-normal">
        Recherchez des voyageurs qui accepteront de prendre votre colis en
        charge
      </p>
      <form>
        <div class="container containerBooking">
          <input
            type="text"
            class="form-control"
            placeholder="D'ou envoyez vous votre colis ?"
            required
          />
          <a href="/" class="dateRecherche bg-white">Date</a>
          <input
            type="text"
            class="form-control"
            placeholder="Où l'envoyez vous ?"
            required
          />
        </div>
      </form>
    </div>
  </header>
  <div class="intro_text">
    <label for="" class="has-text-weight-semibold">
      <center>
        Trouvez votre nouveau<br />facteur !
      </center>
    </label>
  </div>
  <div class="subintro_text">
    <label for="">
      Recherchez des voyageurs qui accepteront de prendre votre colis en charge
    </label>
  </div>
  <div class="intro_choix">
    <div class="level">
      <div class="level-left">
        <div
          class="card level-item carteGD has-text-white has-text-weight-bold"
        >
          D'ou envoyez vous votre colis ?
        </div>
      </div>
      <div class="arrow arrow-left"></div>
      <div class="card level-item carteC px-5">Date</div>

      <div class="arrow arrow-right"></div>
      <div class="level-right">
        <div
          class="card level-item carteGD has-text-white has-text-weight-bold"
        >
          Où l'envoyez vous ?
        </div>
      </div>
    </div>
  </div>
  <div class="card bouton_recherche has-text-weight-bold">
    <center>
      <input
        type="submit"
        value="Rechercher"
        name="valider"
        class="input_recherche"
      />
    </center>
  </div>
</main>

<style>
  .bg-primary {
    background-color: #27005d !important;
  }
  .text-primary {
    color: #27005d !important;
  }
  header {
    margin-top: 0;
    position: relative;
    height: 94vh;
  }
  .containerRecherche {
    position: absolute; /* Changement en position absolue */
    top: 40%; /* Déplace le containerHome à 50% du haut du header */
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

  .dateRecherche {
    color: #84bbff;
    border-radius: 20px;
    padding: 1.2 1.2;
  }

  .containerBooking {
    margin-top: 25px;
    gap: 70px;
    display: flex;
    flex-direction: row;
  }

  .containerBooking input {
    padding: 1.4rem 6rem;
    border: none;
    background-color: #84bbff;
    color: white;
  }
  .containerBooking input::placeholder {
    color: white;
    min-width: 50ch;
  }
</style>
