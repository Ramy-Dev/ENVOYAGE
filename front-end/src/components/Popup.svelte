<script>
    export let isOpen = false;
    export let onClose = () => {};
  
    // Fonction appelée lorsque l'overlay est cliqué
    function handleOverlayClick() {
      onClose();
    }
  </script>
  
  <main>
    {#if isOpen}
      <div class="overlay" on:click={handleOverlayClick}>
        <div class="popup">
          <div class="popup-header">
            <h2>{title}</h2>
            <!-- Bouton de fermeture -->
            <button class="close-btn" on:click={onClose}>X</button>
          </div>
          <div class="popup-content">
            <!-- Utilisation de slot pour afficher le contenu transmis -->
            <slot></slot>
          </div>
        </div>
      </div>
    {/if}
  </main>
  
  <style>
    /* Styles pour votre popup */
  </style>
  