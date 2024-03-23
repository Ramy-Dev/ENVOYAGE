<script>
   import { onMount } from 'svelte';
   import ColorGenerator from '../../../components/colorGenerator.svelte';
   import ColorSwitchStyles from '../../../components/colorOriginalSwitchStyle.svelte';

let color; // Variable pour stocker la couleur

export async function load({ params }) {
    console.log('Loading data for ID:', params.id);
    try {
        const response = await fetch(`http://127.0.0.1:8000/recherche/${params.id}`);
        if (!response.ok) {
            throw new Error('Failed to fetch data');
        }
        const data = await response.json();
        console.log('Fetched data:', data);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}


const toggle = (event) => {
    const clickedButton = event.target.closest('button');
    const clickedTarif = clickedButton.querySelector('.tarifCard');
    const otherTarif = clickedTarif.id === 'c1' ? document.getElementById('c2') : document.getElementById('c1');

    if (clickedTarif.classList.contains('colorOriginalSwitch')) return;

    // Désactiver toutes les classes colorOriginalSwitch
    document.querySelectorAll('.tarifCard.colorOriginalSwitch').forEach(tarif => {
        tarif.classList.remove('colorOriginalSwitch');
        tarif.classList.add('colorSecondarySwitch');
    });

    // Activer la classe colorOriginalSwitch pour le bouton cliqué
    clickedTarif.classList.add('colorOriginalSwitch');
    clickedTarif.classList.remove('colorSecondarySwitch');

    // Activer le bouton cliqué
    clickedButton.disabled = false;
};
onMount(() => {

  const urlParams = new URLSearchParams(window.location.search);
  color = urlParams.get('color'); // Récupérer la couleur à partir des paramètres d'URL
});
</script>
<main>
  <div class="mb-5 pb-5 annc fp">
    <h1 class="text-center display-4 m-5 fw-bold">L'annonce</h1>
    <div class="details mx-auto fw-semibold">
      <div class="colorTopAnnonce" style="background-color: {color};"></div>
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
              style="fill: {color} ; fill-rule: nonzero;"
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
        <div class="textTarif fw-bold fs-3">
          Tarifs disponibles
        </div>
        <div class="tarifDetailsCard" id="tarifs">

          <button class="" type="button" on:click={toggle}>
            <div class="tarifCard colorSecondarySwitch" id="c1">
                <div class="categorieTarifCard fw-bold fs-3">Par Colis</div>
                <ul class="prixTarifCard fs-5 fw-bold">
                  <li>20$ / Colis</li>
                  <li>Max : 2 Colis</li>
                </ul>
              </div>
            </button>

              <button class="" type="button" on:click={toggle}>
            <div class="tarifCard colorSecondarySwitch" id="c2">
                <div class="categorieTarifCard fw-bold fs-3">Par Kg</div>
                  <ul class="prixTarifCard fs-5 fw-bold">
                    <li>5$ / Kg</li>
                    <li>Max : 40 Kg</li>
                  </ul>
              </div>
            </button>
        </div>
      </div>
    </div>
  </div>
</main>

<ColorGenerator />
<ColorSwitchStyles {color} />

<style>
  /* Définissez ici les styles de la classe categorieTarifCard */
  .details {
    padding: 20px;
    margin: 25px 0 100px 0;
    background-color: #f5f5f5;
    border-radius: 30px;
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
    gap: 40px;
  }
  .descriptionCard p {
    padding: 25px;
  }
  .textTarif {
    text-align: center;
  }
  .tarifDetailsCard {
    padding: 10px 100px 70px 100px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
  }
  .tarifCard {
  width: 225px;
  height: 180px;
    padding: 30px 10px 20px 35px ;
    
    appearance: none;
    display: flex;
    flex-direction: column;
   
    justify-content: space-between;
    border-radius: 20px;
    transition: 0.3s ease;
  }
  .prixTarifCard {
    padding-left: 40px;
  }
</style>
