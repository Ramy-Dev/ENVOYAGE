<!-- TagPanel.svelte -->
<script>
import Tag from '../Tag.svelte'; // Assuming Tag.svelte is in the same directory
  export let tags = [];
  export let visible = false;
  export let searchCriteria = "";

  let filteredTags = [];
  let selectedTags = [];
  
  $: filteredTags = tags.filter(tag => tag.toLowerCase().includes(searchCriteria.toLowerCase()));

  function handleTagClick(tag) {
    const event = new CustomEvent('tagSelected', { detail: tag });
    dispatchEvent(event);
  }
</script>

<main>
    <div class="tag-panel" style="display: {visible ? 'flex' : 'none'}">
      {#each filteredTags as tag}
        <Tag name={tag} selected={selectedTags.includes(tag)} on:click={handleTagClick(tag)} />
      {/each}
    </div>
  </main>

<style>
        .tag-panel {
            border: 0;
            margin-top: 5px;
            padding: 10px;
            position: absolute;
            top: 100%; /* Position below the input */
            right: 0;
            width: 450px; /* Full width of the parent container */
            height: 500px;
            background: white;
            box-shadow: 0 4px 30px 0 rgba(0, 0, 0, 0.29);;
            z-index: 1000;
            display: flex;
            flex-wrap: wrap;
            border-radius: 20px;
            gap: 10px;
            overflow-y: auto; /* Add this line */
        }
           /* Style the scrollbar track */
    .tag-panel::-webkit-scrollbar {
        width: 10px;
        border-radius: 20px;
    }

    /* Style the scrollbar handle */
    .tag-panel::-webkit-scrollbar-thumb {
        background: #888;
        border-radius: 20px;
    }

    /* Handle on hover */
    .tag-panel::-webkit-scrollbar-thumb:hover {
        background: #555;
    }
</style>
  