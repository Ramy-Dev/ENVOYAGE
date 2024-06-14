<script>
  // Imports des stores nécessaires
  import PopupPricing from "../PopupPricing.svelte";
  import PopupCalculVolume from "../PopupCalculVolume.svelte";
  import { pricingDataStore } from "../../stores/pricingDataStore.js";
  import { createEventDispatcher } from "svelte";
  import { writable } from "svelte/store";

  export let valueMax = 0;
const dispatch = createEventDispatcher();

function getVolumeMax(newVolumeMax) {
  valueMax = newVolumeMax;
  updateVolumeMax(newVolumeMax); // Appeler la fonction updatePoidsMax
  dispatch('valueMaxChange', valueMax); // Émettre l'événement avec la nouvelle valeur
}
  let valueInterm = 0;
  let volumeMaxEntered = false;
  let volumePaliers = [];
  let palierMin = "";
  let palierMax = "";
  let title = "";
  let isPricingPopupOpen = false;
  let isCalculVolumePopupOpen = false;
  let erreurMessage = "";
  let firstPalierMax;

  
// volumePaliersStore.subscribe(value => {
//   volumePaliers = value;
// });
//   function updatePricing() {
//     if (valueMax > 0) {
//       volumePaliersStore.set(volumePaliers);
//       volumeMaxEntered = true;
//       console.log("Mise à jour des volumePaliers effectuée.");
//     } else {
//       volumeMaxEntered = false;
//       console.log("Le volume maximum doit être supérieur à 0.");
//     }
//     console.log("Contenu du tableau Paliers :", volumePaliers);
//   }

//   function openPricingPopup() {
//     isPricingPopupOpen = true;
//     title = "Ajouter un palier";
//     if (volumePaliers.length > 0) {
//         palierMin = volumePaliers[volumePaliers.length - 1].max;
//     } else {
//         palierMin = 0;
//     }
//     console.log(volumePaliersStore);
//   }
function openCalculVolumePopup() {
    isCalculVolumePopupOpen = true;
    title = "Calculer le volume";
    // console.log(volumePaliersStore);
  }
  function updateVolumeMax(newVolumeMax) {
    valueMax = newVolumeMax;
    volumeMaxEntered = true;
    volumePaliers = [];
    console.log("New valueMax", newVolumeMax, "ancien", valueMax);
    console.log("Paliers after reset:", volumePaliers);
    // updatePricing();
  }
//   function addNewPalier(price) {
//     const palier = { min: valueInterm, max: valueMax, price };
//     volumePaliers.push(palier);
//     volumePaliersStore.set(volumePaliers);
//     pricingDataStore.update(data => ({ ...data, pricingByVolume: volumePaliers }));
//     updatePricing();
//     console.log("Nouveau palier ajouté :", palier);
//     valueInterm = $volumePaliersStore[i - 1] ? $volumePaliersStore[i - 1].max : 0;
//   }

//   function removePalier(index) {
//     $volumePaliersStore.splice(index, 1);
//     if (index < $volumePaliersStore.length) {
//         $volumePaliersStore[index].min = index > 0 ? $volumePaliersStore[index - 1].max : 0;
//     }
//     updatePricing();
//     pricingDataStore.update(data => ({ ...data, pricingByVolume: $volumePaliersStore }));
//     console.log(index);
// }

//   function removeAllPaliers() {
//     valueMax = 0;
//     volumeMaxEntered = false;
//     $volumePaliersStore = [];
//     pricingDataStore.update(data => ({ ...data, pricingByVolume: [] }));
//   }

//   function suggestPaliers() {
//     volumePaliers = [];
//     const step = valueMax / 4;
//     let min = 0;
//     let max = step;
//     let price;

//     for (let i = 0; i < 4; i++) {
//       price = (10 - i * 0.45).toFixed(1);
//       const palier = { min, max: max.toFixed(2), price };
//       volumePaliers.push(palier);
//       min = max;
//       max += step;
//       console.log("Paliers suggérés :", volumePaliers);
//     }
//     console.log("Paliers suggérés :", volumePaliers);
//     volumePaliersStore.set(volumePaliers);
//     updatePricing();
//   }

//   function validateNewPalier(valueMin, volumeMaxPopup) {
//     erreurMessage = "";
//     if (
//       $volumePaliersStore.length > 0 &&
//       valueMin < $volumePaliersStore[$volumePaliersStore.length - 1].max
//     ) {
//       console.log(
//         "Le volume minimum doit être supérieur au maximum du palier précédent."
//       );
//       erreurMessage =
//         "Le volume minimum doit être supérieur au maximum du palier précédent.";
//       return false;
//     }

//     if (volumeMaxPopup > valueMax) {
//       console.log(
//         "Le volume maximum ne doit pas dépasser le volume maximum global."
//       );
//       erreurMessage =
//         "Le volume maximum ne doit pas dépasser le volume maximum global.";
//       return false;
//     }

//     return true;
//   }

  // function handleChangesSaved(event) {
  //   const { fieldName, paliersData } = event.detail;

  //   if (paliersData && Array.isArray(paliersData)) {
  //     paliersData.forEach((palierData, index) => {
  //       const { valueMin, valueMax, price } = palierData;

  //       // if (validateNewPalier(palierMin, valueMax, volumePaliers)) {
  //       //   if (volumePaliers.length >= 4) {
  //       //     console.log("Le nombre maximum de volumePaliers est atteint.");
  //       //     return;
  //       //   }

  //       //   // const newPalier = { min: palierMin, max: valueMax, price };

  //       //   // volumePaliers.push(newPalier);
  //       //   // volumePaliersStore.set(volumePaliers);
  //       //   updatePricing();
  //       //   console.log("Nouveau palier ajouté :", newPalier);
  //       //   console.log("Contenu du tableau Paliers :", volumePaliers);
  //       // }
  //     });
  //   } else {
  //     console.error("paliersData est indéfini ou n'est pas un tableau.");
  //   }
  // }

  // $: {
  //   if ($volumePaliersStore[0]) {
  //     firstPalierMax = $volumePaliersStore[0].max;
  //   }
  // }
  $: if (volumeMaxEntered) {
  pricingDataStore.update(data => ({ ...data, pricingByVolume: valueMax }));
  console.log("Mise à jour des volumePaliers effectuée.");
}
  // $: volumePaliers = $volumePaliersStore;
</script>

<main>
  <div class="choicePricingOptions bg-white">
    <div class="colorTopAnnonce"></div>
    
    <div class="informationsPricing">
      <div class="infoMax">
        <div class="infoMaxEtage1">
          <button
          class="text-primary bg-white border-0 fs-5 fst-italic fontSecondary"
          on:click={openCalculVolumePopup}
        >
          ** calculer le volume
        </button>   
        {#if isCalculVolumePopupOpen}
          <div class="overlay"></div>
          <PopupCalculVolume
            isOpen={isCalculVolumePopupOpen}
            onClose={() => (isCalculVolumePopupOpen = false)}
            {title}
            fieldName="NomDuChamp"
            on:volumeAdded={event => updateVolumeMax(event.detail)}
            {erreurMessage}
          />
          
        {/if}     
        </div>
        <div class="infoMaxEtage2">
        <div class="textPalier text-darkPrimary fw-bold fs-3 fontSecondary">
          Volume Max :
        </div>
        <div class="inputPalier text-primary fs-5 fontSecondary">
          <input
            type="number"
            class="inputPrix fw-normal text-primary fontSecondary"
            placeholder="Volume maximum"
            bind:value={valueMax}
            on:change={getVolumeMax(valueMax)}
            required
          />
        </div>
      </div>
      </div>
      
      <!-- {#if volumePaliersStore && volumeMaxEntered}
        <div class="prixPalier">
          {#if $volumePaliersStore.length === 0}
            <div class="palierPricing">
              <div
                class="textPalier text-darkPrimary fw-bold fs-3 fontSecondary"
              >
                0 m³ - {valueMax} m³
              </div>
              <div class="inputPalier">
                <input
                  type="number"
                  class="inputPrix fw-normal text-primary fontSecondary"
                  placeholder="Prix"
                  required
                />
                <p class="text-primary fontSecondary">
                  €/0.1m³
                </p>
              </div>
            </div>
          {/if}
          {#if $volumePaliersStore.length !== 0}
            {#each $volumePaliersStore as volume, i}
              <div class="palierPricing">
                <div
                  class="textPalier text-darkPrimary fw-bold fs-3 fontSecondary"
                >
                  {$volumePaliersStore[i - 1] ? $volumePaliersStore[i - 1].max : 0} m³ - {volume.max}
                  m³
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
                    bind:value={volume.price}
                    required
                  />
                  <p class="text-primary fontSecondary">
                    €/0.1m³
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
            fieldName="volume"
            on:changesSaved={handleChangesSaved}
            valueMin={palierMin}
            valueMax={palierMax}
            valueMaxGlobal={valueMax}
            addPalier={addNewPalier}
            {erreurMessage}
          />
        {/if}
      {/if} -->
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
  }

  .informationsPricing {
    display: flex;
    flex-direction: column;
    gap: 30px;
  }
  .infoMax {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 10px;
  }
  .infoMaxEtage1 {
    display: flex;
    justify-content: flex-end;
  }
  .infoMaxEtage2{
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
    outline: 3px solid #4FE1F9;
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
  .ajoutPalierBtnEtage0  {
    display: flex;
    justify-content: right;

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
  .colorTopAnnonce {
    height: 0;
  }
</style>
