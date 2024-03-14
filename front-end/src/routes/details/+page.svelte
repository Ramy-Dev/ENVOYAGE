<script>
  let activeTarif = 'c1';

  const toggle = (event) => {
      const clickedButton = event.target;
      const clickedTarif = clickedButton.closest('.tarifCard').id;

      if (clickedTarif === activeTarif) return; // Ne rien faire si le même tarif est déjà sélectionné

      // Désactiver tous les boutons
      const buttons = document.querySelectorAll('.PrixTarifCard button');
      buttons.forEach(button => {
          button.disabled = true;
      });

      // Switcher les classes des tarifs
      const tarifs = document.querySelectorAll('.tarifCard');
      tarifs.forEach(tarif => {
          tarif.classList.toggle('colorOriginalSwitch');
          tarif.classList.toggle('colorSecondarySwitch');
      });

      // Activer le bouton cliqué
      clickedButton.disabled = false;

      // Mettre à jour le tarif actif
      activeTarif = clickedTarif;
  };
</script>
<main>
  <div class="mb-5 pb-5 annc">
    <h1 class="text-center display-4 m-5 fw-bold">L'annonce</h1>
    <div class="details cardAnnonce mx-auto rounded fw-semibold">
      <div class="profileDetails ml-2 m-5">
        <img src="../svg/photoProfile.svg" class="card-img-top" alt="..." />
        <div class="nomDateTopCard text-secondary">
          <h5 class="card-title fw-semibold">Nom Prénom</h5>
          <h5 class="card-title DateTopCard fw-normal">jj/mm/aaaa</h5>
        </div>
      </div>
      <div class="dataCard">
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

        <div class="poidsDateCard">
          <h5 class="card-title fw-bold">Poids Max : 40 Kg</h5>
          <h5 class="card-title fw-bold">Date : jj/mm/aaaa</h5>
        </div>
        <div class="descriptionCard">
          <h5 class="card-title fw-bold">Description :</h5>
          <p class="fw-semibold">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Ex quas
            ipsa commodi placeat voluptates, officia consequatur excepturi?
            Delectus, dolorum ullam nam quae maxime molestias obcaecati pariatur
            commodi illum. Aliquid, rem?
          </p>
        </div>
        <div class="tarifDetailsCard" id="tarifs">

            <div class="tarifCard colorOriginalSwitch rounded" id="c1">
                <div class="categorieTarifCard text-gold">Par Colis</div>
                <div class="PrixTarifCard">20$ / Colis</div>
                <div class="PrixTarifCard">
                    <button value="0"
                    type="button"
                    on:click={toggle}
                    class="border-0 p-2 rounded bg-gold fw-bold">Choisir</button>
                    </div>
            </div>

            <div class="tarifCard colorSecondarySwitch rounded" id="c2">
                <div class="categorieTarifCard text-gold">Par Kg</div>
                <div class="PrixTarifCard">20$ / Kg</div>
                <div class="PrixTarifCard">
                    <button value="1" 
                    type="button"
                    on:click={toggle}
                    class="border-0 p-2 rounded bg-gold fw-bold">Choisir</button>
                    </div>
            </div>

        </div>
      </div>
    </div>
  </div>
</main>

<style>
  .details {
    padding: 20px;
    margin-top: 25px;
    background-color: #f5f5f5;
  }
  .profileDetails {
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 30px;
  }
  .poidsDateCard {
    display: flex;
    justify-content: space-between;
    padding: 0 50px;
  }
  .dataCard {
    display: flex;
    flex-direction: column;
    padding: 0 50px;
    gap: 50px;
  }
  .descriptionCard p {
    padding: 25px;
  }
  .tarifDetailsCard {
    padding: 20px 50px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
  }
  .tarifCard {
    width: 175px;
    height: 225px;
    padding: 20px 0;
    text-align: center;
    appearance: none;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
  }
  .tarifCard button {

  }
</style>
