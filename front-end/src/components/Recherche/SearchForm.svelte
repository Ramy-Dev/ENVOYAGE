<script>
  import { onMount } from 'svelte';

  let from = '';
  let to = '';
  let date = '';
  let tariff = '';
  let conditions = '';

  let input1, input2, input3, input4, input5;
  let isFocused1 = false, isFocused2 = false, isFocused3 = false, isFocused4 = false, isFocused5 = false;

  function search() {
      console.log({ from, to, date, tariff, conditions });
  }

  function clearInput(ref, bindValueSetter) {
    ref.value = '';
    ref.dispatchEvent(new Event('input'));
    bindValueSetter(''); // Update the bound variable directly using the setter
  }
  function onBlur(setter) {
    setTimeout(() => setter(false), 115);
  }
  onMount(() => {
      const inputs = document.querySelectorAll('.custom-placeholder');
      inputs.forEach(input => {
          const placeholderText = input.getAttribute('data-placeholder').split('|');
          input.addEventListener('input', () => {
              if (input.value) {
                  input.setAttribute('placeholder', '');
              } else {
                  input.setAttribute('placeholder', placeholderText.join(' '));
              }
          });
          input.setAttribute('placeholder', placeholderText.join(' '));
      });
  });
</script>

<div class="search-form fontSecondary">
  <div class="input-container">
      <label class="custom-label">
          De<br>
      </label>
      <input bind:this={input1} class="custom-placeholder input1" type="text" bind:value={from} data-placeholder="ville, aéroport, port"
        on:focus={() => isFocused1 = true} on:blur={() => onBlur(value => isFocused1 = value)} />
      {#if from && isFocused1}
      <button class="clear-button" on:click={() => clearInput(input1, value => from = value)}>
        <lord-icon
            class="animated-cross"
            src="https://cdn.lordicon.com/zxvuvcnc.json"
            colors="primary:#4FE1F9"
            style="background-color: white;"
            trigger="hover">
        </lord-icon>
    </button>
      {/if}
  </div>
  <div class="input-container">
      <label class="custom-label">
          Vers<br>
      </label>
      <input bind:this={input2} class="custom-placeholder input2" type="text" bind:value={to} data-placeholder="ville, aéroport, port"
        on:focus={() => isFocused2 = true} on:blur={() => onBlur(value => isFocused2 = value)} />
      {#if to && isFocused2}
      <button class="clear-button" on:click={() => clearInput(input2, value => to = value)}>
        <lord-icon
            class="animated-cross"
            src="https://cdn.lordicon.com/zxvuvcnc.json"
            colors="primary:#4FE1F9"
            style="background-color: white;"
            trigger="hover">
        </lord-icon>
    </button>
      {/if}
  </div>
  <div class="input-container">
      <label class="custom-label">
          Date<br>
      </label>
      <input bind:this={input3} class="custom-placeholder input3" type="text" bind:value={date} data-placeholder="jj/mm/aaaa"
        on:focus={() => isFocused3 = true} on:blur={() => onBlur(value => isFocused3 = value)} />
      {#if date && isFocused3}
      <button class="clear-button" on:click={() => clearInput(input3, value => date = value)}>
        <lord-icon
            class="animated-cross"
            src="https://cdn.lordicon.com/zxvuvcnc.json"
            colors="primary:#4FE1F9"
            style="background-color: white;"
            trigger="hover">
        </lord-icon>
    </button>
      {/if}
  </div>
  <div class="input-container">
      <label class="custom-label">
          Tarifs<br>
      </label>
      <input bind:this={input4} class="custom-placeholder input4" type="text" bind:value={tariff} data-placeholder="poids, volume, quantité"
        on:focus={() => isFocused4 = true} on:blur={() => onBlur(value => isFocused4 = value)} />
      {#if tariff && isFocused4}
      <button class="clear-button" on:click={() => clearInput(input4, value => tariff = value)}>
        <lord-icon
            class="animated-cross"
            src="https://cdn.lordicon.com/zxvuvcnc.json"
            colors="primary:#4FE1F9"
            style="background-color: white;"
            trigger="hover">
        </lord-icon>
    </button>
      {/if}
  </div>
  <div class="input-container">
      <label class="custom-label">
          Conditions<br>
      </label>
      <input bind:this={input5} class="custom-placeholder input5" type="text" bind:value={conditions} data-placeholder="pick from the list"
        on:focus={() => isFocused5 = true} on:blur={() => onBlur(value => isFocused5 = value)} />
      {#if conditions && isFocused5}
      <button class="clear-button" on:click={() => clearInput(input5, value => conditions = value)}>
        <lord-icon
            class="animated-cross"
            src="https://cdn.lordicon.com/zxvuvcnc.json"
            colors="primary:#4FE1F9"
            style="background-color: white;"
            trigger="hover">
        </lord-icon>
    </button>
      {/if}
  </div>
  <button class="searchButton" on:click={search}>Search</button>
</div>

<style>
  .search-form {
      display: flex;
      gap: 12px;
      justify-content: center;
      align-items: center;
      padding: 10px;
      border-radius: 12px;
  }
  .input-container {
      position: relative;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      background-color: #ffffff;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.35);
      padding: 20px 10px;
      border-radius: 20px;
  }
  .custom-label {
      font-weight: bold;
      color: #434343;
      text-align: center;
      font-size: 14px;
  }
  .custom-label span {
      font-weight: normal;
      color: #aaaaaa;
      font-size: 12px;
  }
  .search-form label {
    padding-left: 10px;
  }
  .search-form input {
      padding: 5px 10px;
      border: none;
      border-radius: 20px;
      background-color: transparent;
      font-size: 14px;
      width: 200px;
      text-align: left;
  }
  .search-form .input3 {
      width: 120px;
  }
  .search-form .input4 {
      width: 220px;
  }
  .search-form .input5 {
      width: 180px;
  }
  .search-form .searchButton {
      padding: 35px 30px;
      border: none;
      border-radius: 20px;
      background-color: #4FE1F9;
      color: white;
      font-size: 14px;
      cursor: pointer;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.35);
      transition: background-color 0.3s ease;
  }
  .search-form .searchButton:hover {
      background-color: #3bc7d7;
  }
  .search-form input:focus {
    text-align: left;
      outline: none;
  }
  .search-form input::placeholder {
    text-align: left;
      color: #aaaaaa;
      font-weight: 600;
  }
  .clear-button {
      position: absolute;
      top: 50%;
      right: 10px;
      transform: translateY(-50%);
      background: none;
      border: none;
      padding: 0;
      margin: 0;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
  }
  .clear-button:hover {
      color: #333;
  }
  .animated-cross {

  }
</style>
