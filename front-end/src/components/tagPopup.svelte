<script>
    import { createEventDispatcher } from 'svelte';

    const dispatch = createEventDispatcher();

    export let isOpen = false;
    export let onClose = () => {};
    export let selectedTags = []; // Liste des tags sélectionnés
    export let availableTags = []; // Liste des tags disponibles
    export let title = ""; // Titre du popup

    function handleOverlayClick(event) {
        if (event.target.classList.contains('overlay')) {
            onClose();
        }
    }

    function saveChanges() {
        onClose();
        dispatch('changesSaved', { selectedTags });
    }
</script>

<main>
    {#if isOpen}
        <div class="overlay" on:click={handleOverlayClick}>
            <div class="popup">
                <div class="popup-header">
                    <h2 class="fw-bold fs">{title}</h2>
                </div>
                <div class="popup-content">
                    <div class="tag-selection">
                        <p class="text-secondary fw-bold fs-5 fs">Select Tags:</p>
                        {#each availableTags as tag}
                            <div class="tag-item">
                                <label>
                                    <input type="checkbox" bind:checked={selectedTags} value={tag} />
                                    {tag}
                                </label>
                            </div>
                        {/each}
                    </div>
                </div>
                <div class="popup-footer">
                    <button on:click={saveChanges} class="btn border-0 bg-primary text-white fs-5">Save</button>
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
        /* Styles pour la popup */
    }

    .popup-header {
        /* Styles pour l'en-tête de la popup */
    }

    .popup-content {
        /* Styles pour le contenu de la popup */
    }

    .tag-selection {
        /* Styles pour la sélection des tags */
    }

    .tag-item {
        /* Styles pour chaque élément de tag */
        margin-bottom: 10px;
    }

    .popup-footer {
        /* Styles pour le pied de la popup */
        display: flex;
        justify-content: flex-end;
        margin-top: 20px;
    }

    input[type="checkbox"] {
        /* Styles pour les cases à cocher */
        margin-right: 5px;
    }

    button {
        /* Styles pour les boutons */
    }
</style>
