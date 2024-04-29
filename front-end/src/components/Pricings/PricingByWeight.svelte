<script>
  // Imports des stores nécessaires
  import PopupPricing from "../PopupPricing.svelte";
 
  // import { calculatePricing } from "../../lib/calculatePricing.js";
  import { poidsPaliersStore } from "../../stores/paliersStore.js";
  import { pricingDataStore } from "../../stores/pricingDataStore.js";
  import { writable } from "svelte/store";
  // Utilisation des stores locaux pour les poidsPaliers et les prix

  let valueMax = 0;
  let valueInterm = 0;
  let poidsMaxEntered = false;
  let poidsPaliers = [];
  let palierMin = "";
  let palierMax = "";
  let title = "";
  let isPricingPopupOpen = false;
  let erreurMessage = "";
  let firstPalierMax;

  
poidsPaliersStore.subscribe(value => {
  poidsPaliers = value;
});

  function updatePricing() {
    if (valueMax > 0) {
      // const { poidsPaliers, prixPaliers } = calculatePricing(
      //   "weight",
      //   valueMax,
      //   poidsPaliers
      // );
      // console.log("Poids des poidsPaliers :", poidsPaliers);
      // console.log("Prix des poidsPaliers :", prixPaliers);

      // Mise à jour du store poidsPaliersStore avec les nouveaux poidsPaliers
      poidsPaliersStore.set(poidsPaliers);

      poidsMaxEntered = true;
      console.log("paliers ::::::", poidsPaliers);
      console.log("Mise à jour des poidsPaliers effectuée.");
    } else {
      poidsMaxEntered = false;
      console.log("Le poids maximum doit être supérieur à 0.");
    }
  }

  function openPricingPopup() {
    isPricingPopupOpen = true;
    title = "Ajouter un palier";
    if (poidsPaliers.length > 0) {
        palierMin = poidsPaliers[poidsPaliers.length - 1].max;
    } else {
        palierMin = 0;
    }
    console.log(poidsPaliersStore); // Utilisez poidsPaliersStore au lieu de poidsPaliersStore
  }

  function updatePoidsMax(newPoidsMax) {
    valueMax = newPoidsMax;
    poidsMaxEntered = true;
    poidsPaliers = [];
    console.log("New valueMax", newPoidsMax, "ancien", valueMax);
    console.log("Paliers after reset:", poidsPaliers);
    updatePricing();

  }

  function addNewPalier(price) {
    const palier = { min: valueInterm, max: valueMax, price };
    poidsPaliers.push(palier);
    poidsPaliersStore.set(poidsPaliers); // Mettre à jour le store avec les nouveaux poidsPaliers
    pricingDataStore.update(data => ({ ...data, pricingByWeight: poidsPaliers }));
    updatePricing();
    console.log("Nouveau palier ajouté :", palier);
    valueInterm = $poidsPaliersStore[i - 1] ? $poidsPaliersStore[i - 1].max : 0;
  }

  
  function removePalier(index) {
    $poidsPaliersStore.splice(index, 1);
    if (index < $poidsPaliersStore.length) {
        $poidsPaliersStore[index].min = index > 0 ? $poidsPaliersStore[index - 1].max : 0;
    }
    updatePricing();
    pricingDataStore.update(data => ({ ...data, pricingByWeight: $poidsPaliersStore }));
    console.log(index);
}

  function removeAllPaliers() {
    valueMax = 0;
    poidsMaxEntered = false;
    $poidsPaliersStore = [];
    pricingDataStore.update(data => ({ ...data, pricingByWeight: [] }));
  }
  function suggestPaliers() {
    poidsPaliers = [];
    const step = valueMax / 4;
    let min = 0;
    let max = step;
    let price;

    for (let i = 0; i < 4; i++) {
      price = (5 - i * 1/3).toFixed(1);
      const palier = { min, max: Math.round(max), price }; // Round the value of max
      poidsPaliers.push(palier);
      min = max;
      max += step;
      console.log("Paliers suggérés :", poidsPaliers);
    }
    console.log("Paliers suggérés :", poidsPaliers);
    poidsPaliersStore.set(poidsPaliers);
    updatePricing();
  }
  function validateNewPalier(valueMin, poidsMaxPopup) {
    // Vérifier si le poids minimum est supérieur au maximum du palier précédent
    erreurMessage = "";
    if (
      $poidsPaliersStore.length > 0 &&
      valueMin < $poidsPaliersStore[$poidsPaliersStore.length - 1].max
    ) {
      console.log(
        "Le poids minimum doit être supérieur au maximum du palier précédent."
      );
      erreurMessage =
        "Le poids minimum doit être supérieur au maximum du palier précédent.";
      return false;
    }

    // Vérifier si le poids maximum ne dépasse pas le poids maximum global
    if (poidsMaxPopup > valueMax) {
      console.log(
        "Le poids maximum ne doit pas dépasser le poids maximum global."
      );
      erreurMessage =
        "Le poids maximum ne doit pas dépasser le poids maximum global.";
      return false;
    }

    // Autres validations nécessaires (par exemple, poids min < poids max)

    return true; // Si toutes les validations passent
  }
  function handleChangesSaved(event) {
    const { fieldName, paliersData } = event.detail;

    if (paliersData && Array.isArray(paliersData)) {
      paliersData.forEach((palierData, index) => {
        const { valueMin, valueMax, price } = palierData;

        if (validateNewPalier(palierMin, valueMax, poidsPaliers)) {
          if (poidsPaliers.length >= 4) {
            console.log("Le nombre maximum de poidsPaliers est atteint.");
            return;
          }

          const newPalier = { min: palierMin, max: valueMax, price };

          poidsPaliers.push(newPalier);
          poidsPaliersStore.set(poidsPaliers);
          updatePricing();
          console.log("Nouveau palier ajouté :", newPalier);
          console.log("Contenu du tableau Paliers :", poidsPaliers);
        }
      });
    } else {
      console.error("paliersData est indéfini ou n'est pas un tableau.");
    }
  }

  // Abonnement au store poidsPaliersStore
  $: {
    if ($poidsPaliersStore[0]) {
      firstPalierMax = $poidsPaliersStore[0].max;
    }
  }
  $: if (poidsMaxEntered) {
  pricingDataStore.update(data => ({ ...data, pricingByWeight: valueMax }));
  console.log("Le data center a été appelé.");
}
  $: poidsPaliers = $poidsPaliersStore;
</script>

<main>
  <div class="choicePricingOptions bg-white">
    <div class="colorTopAnnonce"></div>
    <div class="informationsPricing">
      <div class="infoMax">
        <div class="textPalier text-darkPrimary fw-bold fs-3 fontSecondary">
          Poids Max :
        </div>
        <div class="inputPalier text-primary fs-5 fontSecondary">
          <!-- Utiliser les nouvelles variables et la nouvelle fonction pour mettre à jour les prix -->
          <input
            type="number"
            class="inputPrix fw-normal text-primary fontSecondary"
            placeholder="Poids maximum"
            bind:value={valueMax}
            on:change={updatePoidsMax(valueMax)}
            required
          />
        </div>
      </div>
      {#if poidsPaliersStore && poidsMaxEntered}
        <div class="prixPalier">
          {#if $poidsPaliersStore.length === 0}
            <!-- Afficher le palier par défaut seulement si poidsPaliersStore est vide -->
            <div class="palierPricing">
              <div
                class="textPalier text-darkPrimary fw-bold fs-3 fontSecondary"
              >
                0 Kg - {valueMax} Kg
              </div>
              <div class="inputPalier">
                <input
                  type="number"
                  class="inputPrix fw-normal text-primary fontSecondary"
                  placeholder="Prix"
                  required
                />
                <p class="text-primary fontSecondary">
                  €/kg
                </p>
              </div>
              
            </div>
          {/if}
          {#if $poidsPaliersStore.length !== 0}
            {#each $poidsPaliersStore as poids, i}
              <div class="palierPricing">
                <div
                  class="textPalier text-darkPrimary fw-bold fs-3 fontSecondary"
                >
                  {$poidsPaliersStore[i - 1] ? $poidsPaliersStore[i - 1].max : 0} Kg - {poids.max}
                  Kg
                </div>
                <div class="inputPalier">
                  <button
                    class="deleteButton fw-normal text-white bg-primary fontSecondary"
                    on:click={() => removePalier(i)}>x</button
                  >
                  <input
                    type="number"
                    class="inputPrix text-primary fontSecondary"
                    placeholder="Prix"
                    bind:value={poids.price}
                    required
                  />
                  <p class="text-primary fontSecondary">
                    €/kg
                  </p>
                </div>
              </div>
            {/each}
          {/if}
        </div>
        <div class="ajoutPalierBtn">
          <div class="ajoutPalierBtnEtage1">
            <button
              class="text-primary bg-white border-0 fs-5 fst-italic fontSecondary"
              on:click={openPricingPopup}
            >
              * ajouter un palier
            </button>
            <button
              class="text-primary bg-white border-0 fs-5 fst-italic fontSecondary"
              on:click={suggestPaliers}
            >
              * paliers suggérés
            </button>
          </div>
          <div class="ajoutPalierBtnEtage2">
            <button
              class="text-primary bg-white border-0 fs-5 fst-italic fontSecondary"
              on:click={removeAllPaliers}
            >
              * Supprimer tous les paliers
            </button>
          </div>
        </div>
        {#if isPricingPopupOpen}
          <div class="overlay"></div>
          <PopupPricing
            isOpen={isPricingPopupOpen}
            onClose={() => (isPricingPopupOpen = false)}
            {title}
            fieldName="weight"
            on:changesSaved={handleChangesSaved}
            valueMin={palierMin}
            valueMax={palierMax}
            valueMaxGlobal={valueMax}
            addPalier={addNewPalier}
            {erreurMessage}
          />
        {/if}
      {/if}
    </div>
  </div>
</main>

<style>
  .overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5); /* Opacité réduite */
    z-index: 999; /* Assure que la superposition est au-dessus de tout */
  }
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
    flex-direction: column;
    justify-content: space-between;
    gap: 30px;
  }
  .inputPalier {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
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
    border: 2px solid transparent;
    outline: 3px solid #5a02d4;
  }
  .inputPalier p {
    margin: 0;
  }
  .palierPricing {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .ajoutPalierBtn {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 15px;
  }
  .ajoutPalierBtnEtage1 {
    display: flex;
    justify-content: space-between;
  }
  .ajoutPalierBtnEtage2 {
    display: flex;
    justify-content: center;
  }
  .deleteButton {
    border: none;
    border-radius: 20px;
    padding: 0.5rem 0.7rem;
    cursor: pointer;
  }
</style>
