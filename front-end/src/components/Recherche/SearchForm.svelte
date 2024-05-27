<script>
    let from = '';
    let to = '';
    let date = '';
    let tariff = '';
    let conditions = '';

    function search() {
        console.log({ from, to, date, tariff, conditions });
    }
</script>

<div class="search-form fontSecondary">
    <input type="text" bind:value={from} placeholder="De (ville, aéroport, port)" />
    <input type="text" bind:value={to} placeholder="Vers (ville, aéroport, port)" />
    <input type="text" bind:value={date} placeholder="Date (jj/mm/aaaa)" />
    <input type="text" bind:value={tariff} placeholder="Tarifs (poids, volume, quantité)" />
    <input type="text" bind:value={conditions} placeholder="Conditions" />
    <button on:click={search}>Search</button>
</div>

<style>
    .search-form {
      display: flex;
      gap: 10px;
      justify-content: center;
      align-items: center;
      /* background-color: #f0f0f0; */
      padding: 10px;
      border-radius: 12px;
    }
    .search-form input {
      padding: 30px;
      border: none;
      border-radius: 20px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.23);
      font-size: 14px;
      width: 200px;
      text-align: center;
    }
    .search-form button {
      padding: 30px 30px;
      border: none;
      border-radius: 20px;
      background-color: #4FE1F9;
      color: white;
      font-size: 14px;
      cursor: pointer;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.23);
      transition: background-color 0.3s ease;
    }
    .search-form button:hover {
      background-color: #3bc7d7;
    }
    .search-form input:focus {
      outline: none;
    }
    .search-form input::placeholder {
      color: #aaaaaa;
      font-weight: 600;
    }
    .search-form input:first-child {
      margin-left: 0px;
    }
    .search-form input:last-child {
      margin-right: 20px;
    }
  </style>
