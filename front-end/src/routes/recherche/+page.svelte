<main>
  <header class="section text-white bg-white">
    <div class="cover-recherche position-absolute"></div>
    <div class="cover-img"></div>
    <div class="containerHeader container index text-center position-relative">
      <h1 class="display-3 fw-semibold">
        Trouvez votre nouveau<br />facteur !
      </h1>
      <p class="pl-2 mb-6 py-6 fs-4 fw-normal">
        Recherchez des voyageurs qui accepteront de prendre votre colis en
        charge
      </p>
      <form>
        <!-- <div class="container containerBooking">
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
        </div> -->

        <!-- code mao albanie -->
        <div class="containerBooking">
          <div class="input-box">
            <input
              class="fw-semibold"
              type="text"
              placeholder="D'ou envoyez vous votre colis ?"
              required
            />
            <div>
              <a class="dateRecherche fw-bolder border-0" href="/">Date</a>
            </div>
            <input
              class="fw-semibold"
              type="text"
              placeholder="Où l'envoyez vous ?"
              required
            />
          </div>
        </div>
        <!-- ------------------- -->

        <button
          href="/"
          class="submit submitRecherche text-primary fw-bolder fs-4 border-0"
        >
          Rechercher
        </button>
        <div class=""></div>
      </form>
    </div>
  </header>
  <section class="about">
    <div class="">
      <h2 class="textAnnonceRecherche text-center fw-bold">Les annonces</h2>
    </div>
    <div class="album py-5 bg-body-tertiary">
      <div class="container containerAnnonces">
    <div class="row row-cols-1 row-cols-md-3 g-5 px-5">
      <div class="col">
        <div class="card cardAnnonce h-100">
          <img src="../svg/imagesVilles/Algerie/imageAlger" class="card-img-top" alt="..." />
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">
              This is a wider card with supporting text below as a natural
              lead-in to additional content. This content is a little bit
              longer.
            </p>
          </div>
          <div class="card-footer">
            <small class="text-body-secondary">Last updated 3 mins ago</small>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card cardAnnonce h-100">
          <img src="..." class="card-img-top" alt="..." />
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">
              This is a wider card with supporting text below as a natural
              lead-in to additional content. This content is a little bit
              longer.
            </p>
          </div>
          <div class="card-footer">
            <small class="text-body-secondary">Last updated 3 mins ago</small>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card cardAnnonce h-100">
          <img src="..." class="card-img-top" alt="..." />
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">
              This is a wider card with supporting text below as a natural
              lead-in to additional content. This content is a little bit
              longer.
            </p>
          </div>
          <div class="card-footer">
            <small class="text-body-secondary">Last updated 3 mins ago</small>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card cardAnnonce h-100">
          <img src="..." class="card-img-top" alt="..." />
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">
              This card has supporting text below as a natural lead-in to
              additional content.
            </p>
          </div>
          <div class="card-footer">
            <small class="text-body-secondary">Last updated 3 mins ago</small>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card cardAnnonce h-100">
          <img src="..." class="card-img-top" alt="..." />
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">
              This is a wider card with supporting text below as a natural
              lead-in to additional content. This card has even longer content
              than the first to show that equal height action.
            </p>
          </div>
          <div class="card-footer">
            <small class="text-body-secondary">Last updated 3 mins ago</small>
          </div>
        </div>
      </div>
    </div>
  </div>
  </div>
  </section>
</main>

<style>
  header {
    margin-top: 0;
    position: relative;
    height: 94vh;
  }

  .dateRecherche {
    color: #84bbff;
    border-radius: 10px;
    padding: 1.2 1.2;
    text-decoration: none;
    background-color: #fff;
    padding: 0.5rem 1rem;
  }

  .containerBooking {
    margin-top: 25px;
    min-width: 900px;
  }

  .containerBooking input {
    padding: 1.5rem;
    border-radius: 10px;
    border: none;
    background-color: #84bbff;
    color: white;
    appearance: none;
  }
  .containerBooking input::placeholder {
    color: white;
  }

  /* code mao albanie */

  .input-box {
    display: flex;
    width: 100%;
    gap: 90px;
    align-items: center;
  }

  .input-box input {
    width: 100%;
  }

  .input-box input::placeholder {
    text-align: center;
  }
  /* -------------------------- */

  .submitRecherche {
    background-color: #ffe767;
    text-decoration: none;
    padding: 1.25rem 2rem;
    border-radius: 10px;
    margin-top: 110px;
  }

  .about {
    padding: 20px;
    margin-top: 25px;
    background-color: #f5f5f5;
  }

  .textAnnonceRecherche {
    color: #4a4a4a;
    margin-top: 75px;
    margin-bottom: 50px;
  }
  .card {
    border: none;
    border-radius: 20px;
  }
  .containerAnnonces {
    
  }
  .cardAnnonce {
    box-shadow: 0 1px 3px 0 #25201f4d;
  }
</style>
