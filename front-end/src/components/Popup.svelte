<script>
  export let isOpen = false;
  export let onClose = () => {};
  export let newName = ""; // Déclaration de newName en tant que prop
  export let title = ""; // Autres props, comme title, si nécessaire

  let name = newName;

  function handleOverlayClick(event) {
    // Vérifier si l'événement de clic provient de l'overlay
    if (event.target.classList.contains('overlay')) {
      onClose();
    }
  }
  function saveChanges() {
    onClose(); // Fermer le popup
  }
</script>

<main>
  {#if isOpen}
    <div class="overlay" on:click={handleOverlayClick}>
      <div class="popup">
        <div class="popup-header">
          <h2 class="fw-bold">{title}</h2>
        </div>
        <div class="popup-content">
          <div class="EditText">
          <p class="text-secondary fw-bold">Your Name</p>
          <p class="text-secondary fw-bold">Your new Name</p>
        </div>
          <div class="EditNew">
            <span class="text-primary fw-bold">{name}</span>
          <div class="input-box">
            <input class="" bind:value={newName} />
            <button on:click={saveChanges} class="ButtonEdit btn border-0 bg-primary text-white">save</button>
          </div>
        </div>
        </div>
      </div>
    </div>
  {/if}
</main>

<style>
  /* Styles CSS pour le popup */
  .overlay {
    /* Styles pour l'overlay */
  }

  .popup {
    display: flex;
    flex-direction: column;
    justify-content: center;
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: white;
    padding: 50px 50px 30px 50px;
    border-radius: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    z-index: 9999; /* Placer la popup au-dessus des autres éléments */
    gap: 50px;
  }

  .popup-header {
    /* Styles pour l'en-tête de la popup */
  }

  .popup-content {
    display: flex;
    justify-content: center;
    gap: 50px;
  }

  .input-box {
    /* Styles pour la boîte (carte) contenant le champ de saisie */
    display: flex;
    justify-content: center;
    gap: 20px;
  }

  input {
    /* Styles pour le champ de saisie */
    appearance: none;
    padding: 5px;
    border-radius: 10px;
    border: 2px solid #5A02D4;
  }

  button {
    /* Styles pour le bouton */
  }

  .EditText {
    display: flex;
    flex-direction: column;
    gap: 25px;
  }
  .EditNew {
    display: flex;
    flex-direction: column;
    gap: 30px;
  }
</style>