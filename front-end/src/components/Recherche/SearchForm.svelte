<script>
    let from = '';
    let to = '';
    let date = '';
    let tariff = '';
    let conditions = '';
</script>

<div class="search-form">
    <input type="text" bind:value={from} placeholder="De (ville, aéroport, port)" />
    <input type="text" bind:value={to} placeholder="Vers (ville, aéroport, port)" />
    <input type="text" bind:value={date} placeholder="Date (jj/mm/aaaa)" />
    <input type="text" bind:value={tariff} placeholder="Tarifs (poids, volume, quantité)" />
    <input type="text" bind:value={conditions} placeholder="Conditions" />
    <button on:click={() => console.log({ from, to, date, tariff, conditions })}>Search</button>
</div>

<style>
    /* Ajoutez vos styles ici */
</style>