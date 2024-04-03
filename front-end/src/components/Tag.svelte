<!-- Tag.svelte -->
<script>
  import { createEventDispatcher } from "svelte";
  import { alreadySelectedConditions } from "../stores/alreadySelectedConditions.js"; // Import du store

  const dispatch = createEventDispatcher();

  export let name;

  // Abonnez-vous aux changements du store
  let isSelected;

  $: {
    isSelected = $alreadySelectedConditions.includes(name);
  }


  function handleClick() {
    isSelected = !isSelected; // Inverser l'état actuel du tag
    dispatch("tagClick", { name, isSelected }); // Émettre un événement avec le nouvel état du tag
    alreadySelectedConditions.toggle(name); // Mettre à jour le store avec l'état mis à jour du tag
  }
</script>

<main>
  <button
    class="{isSelected
      ? 'selected conditionTagBtn'
      : 'conditionTagBtn'} border-0 text-white fs-5 fontSecondary"
    on:click={handleClick}
  >
    <p class="m-0">{name}</p>
  </button>
</main>

<style>
  .selected {
    box-shadow: 0px 3px 0px 5px #BFACFE !important;
    background-color:  #27005d !important; /* Couleur de fond lorsque sélectionné */
  }

  .conditionTagBtn {
    padding: 1.5rem 2rem;
    border-radius: 20px;
    box-shadow: 0 3px 3px 1px rgba(0, 0, 0, 0.25);
    text-align: center; /* Centrer le contenu */
    background-color: #5a02d4; /* Couleur de fond par défaut */
  }
</style>
