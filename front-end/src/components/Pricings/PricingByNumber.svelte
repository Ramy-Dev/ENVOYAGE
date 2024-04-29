<script>

    import { calculatePricing } from "../../lib/calculatePricing.js";

    let poidsMax = 0;
let { poidsPaliers, prixPaliers } = calculatePricing("number",poidsMax);

function updatePricing() {
  // Appelez la fonction pour recalculer les paliers de poids et les prix associés
  let { poidsPaliers, prixPaliers } = calculatePricing("number",poidsMax);
  console.log(poidsMax, poidsPaliers, prixPaliers);
}
</script>

<main>
    <div class="choicePricingOptions bg-white">
        <div class="colorTopAnnonce">

        </div>
        <div class="informationsPricing">
          <div class="infoMax">
            <div class="textPalier text-darkPrimary fw-bold fs-3 fontSecondary">
              Number Max :
            </div>
            <div class="inputPalier text-primary fs-5 fontSecondary">
              <input type="number" class="inputPrix fw-normal text-primary fontSecondary" placeholder="Poids maximum"  bind:value={poidsMax} on:change={updatePricing} required>
            </div>
          </div>
          {#each poidsPaliers as poids, i}
          {#if i > 0}
            <div class="prixPalier">
              <div class="textPalier text-darkPrimary fw-bold fs-3 fontSecondary">
                {poidsPaliers[i - 1]} - {poids} Colis
              </div>
              <div class="inputPalier text-primary fs-5 fontSecondary">
                <input type="number" class="inputPrix fw-normal text-primary fontSecondary" placeholder="Prix" value={prixPaliers[i - 1]} required>
              </div>
            </div>
          {/if}
        {/each}
    </div>
  </div>
</main>
<style>
    .choicePricingOptions {
    padding: 30px 40px;
    border-radius: 40px;
    display: flex;
    flex-direction: column;
    gap: 50px;
  }
  
.informationsPricing {
    display: flex;
    flex-direction: column;
    gap: 30px;
  }
  .infoMax {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .prixPalier {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .inputPalier input {
    padding: 0.5rem 0.2rem;
    border-radius: 20px;
    border: 2px solid #b6b3b3;
    box-shadow: 0 3px 3px 0 rgba(0, 0, 0, 0.25);
    text-align: center; /* Centrer le contenu */
  }
  .inputPalier input::placeholder {
    text-align: center;
  }
  .inputPalier input:focus {
    border: 2px solid transparent ;
    outline: 3px solid #5a02d4 ;
  }
</style>