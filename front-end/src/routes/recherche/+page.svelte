<!-- <script>
document.addEventListener("DOMContentLoaded", function() {
    // Définir les couleurs disponibles
    const colors = ['#FF5733', '#33FF57', '#5733FF', '#FFFF33', '#33FFFF'];

    // Fonction pour obtenir une couleur aléatoire différente des couleurs voisines
    function getRandomColor(previousColor) {
      let color = previousColor;
      while (color === previousColor) {
        color = colors[Math.floor(Math.random() * colors.length)];
      }
      return color;
    }

    // Générer les cartes avec des couleurs uniques pour chaque carte et ses voisins
    const cardsContainer = document.getElementById('cardsContainer');
    const cards = cardsContainer.querySelectorAll('.card');
    let previousColors = [];

    cards.forEach((card, index) => {
      const leftNeighborColor = (index % 3 !== 0) ? previousColors[index - 1] : null;
      const topNeighborColor = (index >= 3) ? previousColors[index - 3] : null;

      let newColor = getRandomColor(leftNeighborColor);
      newColor = getRandomColor(topNeighborColor);

      card.style.backgroundColor = newColor;
      previousColors.push(newColor);
    });
  });
</script> -->

<script>
  // Importer la fonction `navigate` de Svelte Router si vous utilisez un routeur
  import { navigate } from "svelte-routing";

  // Fonction pour effectuer la redirection
  function redirectToPage() {
    // Redirection vers la page souhaitée
    // Remplacez 'url_de_la_page' par l'URL de la page vers laquelle vous souhaitez rediriger
    navigate("/");
  }
</script>

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
    <div class="album py-5">
      <div class="container containerAnnonces">
        <div class="row row-cols-1 row-cols-md-3 g-5 px-5" id="cardsContainer">
          <div class="col">
            <a href="/details" class="card cardAnnonce h-100 redirection-div">
              <div class="card-body">
                <div class="topCard">
                  <img
                    src="../svg/photoProfile.svg"
                    class="card-img-top"
                    alt="..."
                  />
                  <div class="nomDateTopCard">
                    <h5 class="card-title fw-bolder">Nom Prénom</h5>
                    <h5 class="card-title DateTopCard fw-semibold">
                      jj/mm/aaaa
                    </h5>
                  </div>
                </div>
                <div class="destinationTopCard fw-semibold fs-5">
                  <div class="departureTopCard">Paris</div>
                  <svg
                    class="mt-2 mx-3"
                    viewBox="246.554 219.198 189.9 12"
                    width="189.9"
                    height="12"
                    xmlns="http://www.w3.org/2000/svg"
                    xmlns:bx="https://boxy-svg.com"
                  >
                    <!-- svelte-ignore illegal-attribute-character -->
                    <path
                      d="M 246.554 223.198 H 425.454 L 425.454 219.198 L 436.454 225.198 L 425.454 231.198 L 425.454 227.198 H 246.554 V 223.198 Z"
                      style="fill: rgba(39, 0, 93, 1); fill-rule: nonzero;"
                      transform="matrix(1.0000000000000002, 0, 0, 1.0000000000000002, 0, 0)"
                      bx:shape="arrow 246.554 219.198 189.9 12 4 11 0 1@4082cbfb"
                    />
                  </svg>
                  <div class="arrivalTopCard">Alger</div>
                </div>
                <div class="dateCard pt-4 pb-2 fw-semibold">Date : jj/mm/aaaa</div>
              </div>
              <div class="card-footer">
                <small class="text-body-secondary"
                  >Last updated 3 mins ago</small
                >
              </div>
            </a>
          </div>
          <div class="col">
            <a href="/details" class="card cardAnnonce h-100 redirection-div">
              <div class="card-body">
                <div class="topCard">
                  <img
                    src="../svg/photoProfile.svg"
                    class="card-img-top"
                    alt="..."
                  />
                  <div class="nomDateTopCard">
                    <h5 class="card-title fw-bolder">Nom Prénom</h5>
                    <h5 class="card-title DateTopCard fw-semibold">
                      jj/mm/aaaa
                    </h5>
                  </div>
                </div>
                <div class="destinationTopCard fw-semibold fs-5">
                  <div class="departureTopCard">Paris</div>
                  <svg
                    class="mt-2 mx-3"
                    viewBox="246.554 219.198 189.9 12"
                    width="189.9"
                    height="12"
                    xmlns="http://www.w3.org/2000/svg"
                    xmlns:bx="https://boxy-svg.com"
                  >
                    <!-- svelte-ignore illegal-attribute-character -->
                    <path
                      d="M 246.554 223.198 H 425.454 L 425.454 219.198 L 436.454 225.198 L 425.454 231.198 L 425.454 227.198 H 246.554 V 223.198 Z"
                      style="fill: rgba(39, 0, 93, 1); fill-rule: nonzero;"
                      transform="matrix(1.0000000000000002, 0, 0, 1.0000000000000002, 0, 0)"
                      bx:shape="arrow 246.554 219.198 189.9 12 4 11 0 1@4082cbfb"
                    />
                  </svg>
                  <div class="arrivalTopCard">Alger</div>
                </div>
                <div class="dateCard pt-4 pb-2 fw-semibold">Date : jj/mm/aaaa</div>
              </div>
              <div class="card-footer">
                <small class="text-body-secondary"
                  >Last updated 3 mins ago</small
                >
              </div>
            </a>
          </div>
          <div class="col">
            <a href="/details" class="card cardAnnonce h-100 redirection-div">
              <div class="card-body">
                <div class="topCard">
                  <img
                    src="../svg/photoProfile.svg"
                    class="card-img-top"
                    alt="..."
                  />
                  <div class="nomDateTopCard">
                    <h5 class="card-title fw-bolder">Nom Prénom</h5>
                    <h5 class="card-title DateTopCard fw-semibold">
                      jj/mm/aaaa
                    </h5>
                  </div>
                </div>
                <div class="destinationTopCard fw-semibold fs-5">
                  <div class="departureTopCard">Paris</div>
                  <svg
                    class="mt-2 mx-3"
                    viewBox="246.554 219.198 189.9 12"
                    width="189.9"
                    height="12"
                    xmlns="http://www.w3.org/2000/svg"
                    xmlns:bx="https://boxy-svg.com"
                  >
                    <!-- svelte-ignore illegal-attribute-character -->
                    <path
                      d="M 246.554 223.198 H 425.454 L 425.454 219.198 L 436.454 225.198 L 425.454 231.198 L 425.454 227.198 H 246.554 V 223.198 Z"
                      style="fill: rgba(39, 0, 93, 1); fill-rule: nonzero;"
                      transform="matrix(1.0000000000000002, 0, 0, 1.0000000000000002, 0, 0)"
                      bx:shape="arrow 246.554 219.198 189.9 12 4 11 0 1@4082cbfb"
                    />
                  </svg>
                  <div class="arrivalTopCard">Alger</div>
                </div>
                <div class="dateCard pt-4 pb-2 fw-semibold">Date : jj/mm/aaaa</div>
              </div>
              <div class="card-footer">
                <small class="text-body-secondary"
                  >Last updated 3 mins ago</small
                >
              </div>
            </a>
          </div>
          <div class="col">
            <a href="/details" class="card cardAnnonce h-100 redirection-div">
              <div class="card-body">
                <div class="topCard">
                  <img
                    src="../svg/photoProfile.svg"
                    class="card-img-top"
                    alt="..."
                  />
                  <div class="nomDateTopCard">
                    <h5 class="card-title fw-bolder">Nom Prénom</h5>
                    <h5 class="card-title DateTopCard fw-semibold">
                      jj/mm/aaaa
                    </h5>
                  </div>
                </div>
                <div class="destinationTopCard fw-semibold fs-5">
                  <div class="departureTopCard">Paris</div>
                  <svg
                    class="mt-2 mx-3"
                    viewBox="246.554 219.198 189.9 12"
                    width="189.9"
                    height="12"
                    xmlns="http://www.w3.org/2000/svg"
                    xmlns:bx="https://boxy-svg.com"
                  >
                    <!-- svelte-ignore illegal-attribute-character -->
                    <path
                      d="M 246.554 223.198 H 425.454 L 425.454 219.198 L 436.454 225.198 L 425.454 231.198 L 425.454 227.198 H 246.554 V 223.198 Z"
                      style="fill: rgba(39, 0, 93, 1); fill-rule: nonzero;"
                      transform="matrix(1.0000000000000002, 0, 0, 1.0000000000000002, 0, 0)"
                      bx:shape="arrow 246.554 219.198 189.9 12 4 11 0 1@4082cbfb"
                    />
                  </svg>
                  <div class="arrivalTopCard">Alger</div>
                </div>
                <div class="dateCard pt-4 pb-2 fw-semibold">Date : jj/mm/aaaa</div>
              </div>
              <div class="card-footer">
                <small class="text-body-secondary"
                  >Last updated 3 mins ago</small
                >
              </div>
            </a>
          </div>
          <div class="col">
            <a href="/details" class="card cardAnnonce h-100 redirection-div">
              <div class="card-body">
                <div class="topCard">
                  <img
                    src="../svg/photoProfile.svg"
                    class="card-img-top"
                    alt="..."
                  />
                  <div class="nomDateTopCard">
                    <h5 class="card-title fw-bolder">Nom Prénom</h5>
                    <h5 class="card-title DateTopCard fw-semibold">
                      jj/mm/aaaa
                    </h5>
                  </div>
                </div>
                <div class="destinationTopCard fw-semibold fs-5">
                  <div class="departureTopCard">Paris</div>
                  <svg
                    class="mt-2 mx-3"
                    viewBox="246.554 219.198 189.9 12"
                    width="189.9"
                    height="12"
                    xmlns="http://www.w3.org/2000/svg"
                    xmlns:bx="https://boxy-svg.com"
                  >
                    <!-- svelte-ignore illegal-attribute-character -->
                    <path
                      d="M 246.554 223.198 H 425.454 L 425.454 219.198 L 436.454 225.198 L 425.454 231.198 L 425.454 227.198 H 246.554 V 223.198 Z"
                      style="fill: rgba(39, 0, 93, 1); fill-rule: nonzero;"
                      transform="matrix(1.0000000000000002, 0, 0, 1.0000000000000002, 0, 0)"
                      bx:shape="arrow 246.554 219.198 189.9 12 4 11 0 1@4082cbfb"
                    />
                  </svg>
                  <div class="arrivalTopCard">Alger</div>
                </div>
                <div class="dateCard pt-4 pb-2 fw-semibold">Date : jj/mm/aaaa</div>
              </div>
              <div class="card-footer">
                <small class="text-body-secondary"
                  >Last updated 3 mins ago</small
                >
              </div>
            </a>
          </div>
          <div class="col">
            <a href="/details" class="card cardAnnonce h-100 redirection-div">
              <div class="card-body">
                <div class="topCard">
                  <img
                    src="../svg/photoProfile.svg"
                    class="card-img-top"
                    alt="..."
                  />
                  <div class="nomDateTopCard">
                    <h5 class="card-title fw-bolder">Nom Prénom</h5>
                    <h5 class="card-title DateTopCard fw-semibold">
                      jj/mm/aaaa
                    </h5>
                  </div>
                </div>
                <div class="destinationTopCard fw-semibold fs-5">
                  <div class="departureTopCard">Paris</div>
                  <svg
                    class="mt-2 mx-3"
                    viewBox="246.554 219.198 189.9 12"
                    width="189.9"
                    height="12"
                    xmlns="http://www.w3.org/2000/svg"
                    xmlns:bx="https://boxy-svg.com"
                  >
                    <!-- svelte-ignore illegal-attribute-character -->
                    <path
                      d="M 246.554 223.198 H 425.454 L 425.454 219.198 L 436.454 225.198 L 425.454 231.198 L 425.454 227.198 H 246.554 V 223.198 Z"
                      style="fill: rgba(39, 0, 93, 1); fill-rule: nonzero;"
                      transform="matrix(1.0000000000000002, 0, 0, 1.0000000000000002, 0, 0)"
                      bx:shape="arrow 246.554 219.198 189.9 12 4 11 0 1@4082cbfb"
                    />
                  </svg>
                  <div class="arrivalTopCard">Alger</div>
                </div>
                <div class="dateCard pt-4 pb-2 fw-semibold">Date : jj/mm/aaaa</div>
              </div>
              <div class="card-footer">
                <small class="text-body-secondary"
                  >Last updated 3 mins ago</small
                >
              </div>
            </a>
          </div>
          <div class="col">
            <a href="/details" class="card cardAnnonce h-100 redirection-div">
              <div class="card-body">
                <div class="topCard">
                  <img
                    src="../svg/photoProfile.svg"
                    class="card-img-top"
                    alt="..."
                  />
                  <div class="nomDateTopCard">
                    <h5 class="card-title fw-bolder">Nom Prénom</h5>
                    <h5 class="card-title DateTopCard fw-semibold">
                      jj/mm/aaaa
                    </h5>
                  </div>
                </div>
                <div class="destinationTopCard fw-semibold fs-5">
                  <div class="departureTopCard">Paris</div>
                  <svg
                    class="mt-2 mx-3"
                    viewBox="246.554 219.198 189.9 12"
                    width="189.9"
                    height="12"
                    xmlns="http://www.w3.org/2000/svg"
                    xmlns:bx="https://boxy-svg.com"
                  >
                    <!-- svelte-ignore illegal-attribute-character -->
                    <path
                      d="M 246.554 223.198 H 425.454 L 425.454 219.198 L 436.454 225.198 L 425.454 231.198 L 425.454 227.198 H 246.554 V 223.198 Z"
                      style="fill: rgba(39, 0, 93, 1); fill-rule: nonzero;"
                      transform="matrix(1.0000000000000002, 0, 0, 1.0000000000000002, 0, 0)"
                      bx:shape="arrow 246.554 219.198 189.9 12 4 11 0 1@4082cbfb"
                    />
                  </svg>
                  <div class="arrivalTopCard">Alger</div>
                </div>
                <div class="dateCard pt-4 pb-2 fw-semibold">Date : jj/mm/aaaa</div>
              </div>
              <div class="card-footer">
                <small class="text-body-secondary"
                  >Last updated 3 mins ago</small
                >
              </div>
            </a>
          </div>
          <div class="col">
            <a href="/details" class="card cardAnnonce h-100 redirection-div">
              <div class="card-body">
                <div class="topCard">
                  <img
                    src="../svg/photoProfile.svg"
                    class="card-img-top"
                    alt="..."
                  />
                  <div class="nomDateTopCard">
                    <h5 class="card-title fw-bolder">Nom Prénom</h5>
                    <h5 class="card-title DateTopCard fw-semibold">
                      jj/mm/aaaa
                    </h5>
                  </div>
                </div>
                <div class="destinationTopCard fw-semibold fs-5">
                  <div class="departureTopCard">Paris</div>
                  <svg
                    class="mt-2 mx-3"
                    viewBox="246.554 219.198 189.9 12"
                    width="189.9"
                    height="12"
                    xmlns="http://www.w3.org/2000/svg"
                    xmlns:bx="https://boxy-svg.com"
                  >
                    <!-- svelte-ignore illegal-attribute-character -->
                    <path
                      d="M 246.554 223.198 H 425.454 L 425.454 219.198 L 436.454 225.198 L 425.454 231.198 L 425.454 227.198 H 246.554 V 223.198 Z"
                      style="fill: rgba(39, 0, 93, 1); fill-rule: nonzero;"
                      transform="matrix(1.0000000000000002, 0, 0, 1.0000000000000002, 0, 0)"
                      bx:shape="arrow 246.554 219.198 189.9 12 4 11 0 1@4082cbfb"
                    />
                  </svg>
                  <div class="arrivalTopCard">Alger</div>
                </div>
                <div class="dateCard pt-4 pb-2 fw-semibold">Date : jj/mm/aaaa</div>
              </div>
              <div class="card-footer">
                <small class="text-body-secondary"
                  >Last updated 3 mins ago</small
                >
              </div>
            </a>
          </div>
          <div class="col">
            <a href="/details" class="card cardAnnonce h-100 redirection-div">
              <div class="card-body">
                <div class="topCard">
                  <img
                    src="../svg/photoProfile.svg"
                    class="card-img-top"
                    alt="..."
                  />
                  <div class="nomDateTopCard">
                    <h5 class="card-title fw-bolder">Nom Prénom</h5>
                    <h5 class="card-title DateTopCard fw-semibold">
                      jj/mm/aaaa
                    </h5>
                  </div>
                </div>
                <div class="destinationTopCard fw-semibold fs-5">
                  <div class="departureTopCard">Paris</div>
                  <svg
                    class="mt-2 mx-3"
                    viewBox="246.554 219.198 189.9 12"
                    width="189.9"
                    height="12"
                    xmlns="http://www.w3.org/2000/svg"
                    xmlns:bx="https://boxy-svg.com"
                  >
                    <!-- svelte-ignore illegal-attribute-character -->
                    <path
                      d="M 246.554 223.198 H 425.454 L 425.454 219.198 L 436.454 225.198 L 425.454 231.198 L 425.454 227.198 H 246.554 V 223.198 Z"
                      style="fill: rgba(39, 0, 93, 1); fill-rule: nonzero;"
                      transform="matrix(1.0000000000000002, 0, 0, 1.0000000000000002, 0, 0)"
                      bx:shape="arrow 246.554 219.198 189.9 12 4 11 0 1@4082cbfb"
                    />
                  </svg>
                  <div class="arrivalTopCard">Alger</div>
                </div>
                <div class="dateCard pt-4 pb-2 fw-semibold">Date : jj/mm/aaaa</div>
              </div>
              <div class="card-footer">
                <small class="text-body-secondary"
                  >Last updated 3 mins ago</small
                >
              </div>
            </a>
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
  .topCard {
    display: flex;
    flex-direction: row;
    padding: 0 50px 30px 50px;
    align-items: center;
    justify-content: space-between;
  }

</style>
