<script>
  export let ad;

  // Function to get a random color from the given list
  function getRandomColor() {
    const colors = ['#21A5C3', '#1A849C', '#0D434F', '#4FE1F9'];
    return colors[Math.floor(Math.random() * colors.length)];
  }

  // Variable to store the random color
  let randomColor = getRandomColor();
</script>

<div class="ad-card">
  <div class="col">
    <div href="" class="card h-100 redirection-div card-shadow-gray">
      <div class="card-body">
        <div class="colorTopAnnonce mb-3" style="background-color: {randomColor};"></div>
        <div class="topCard">
          <img
            src="../svg/photoProfile.svg"
            class="card-img-top"
            alt="Profile Picture"
          />
          <div class="nomDateTopCard">
            <h5 class="card-title fw-bold">{ad.name}</h5>
            <h5 class="card-title DateTopCard fw-semibold">
              {ad.dob}
            </h5>
          </div>
        </div>
        <div class="destinationTopCard fw-semibold fs-5 fontSecondary">
          <div class="departureTopCard fw-bold">{ad.from}</div>
          <svg
            class="svgArrow mt-2 mx-3"
            viewBox="246.554 219.198 189.9 12"
            width="189.9"
            height="12"
            xmlns="http://www.w3.org/2000/svg"
            xmlns:bx="https://boxy-svg.com"
          >
            <!-- svelte-ignore illegal-attribute-character -->
            <path
              d="M 246.554 223.198 H 425.454 L 425.454 219.198 L 436.454 225.198 L 425.454 231.198 L 425.454 227.198 H 246.554 V 223.198 Z"
              style="fill-rule: nonzero; fill: {randomColor};"
              transform="matrix(1.0000000000000002, 0, 0, 1.0000000000000002, 0, 0)"
              bx:shape="arrow 246.554 219.198 189.9 12 4 11 0 1@4082cbfb"
            />
          </svg>
          <div class="arrivalTopCard fw-bold">{ad.to}</div>
        </div>
        <div class="dateCard pt-4 pb-2 text-darkSecondary fw-semibold">
          Date : {ad.date}
        </div>
      </div>
      <div class="card-footer border-0">
        <div class="text-body-secondary px-3 pb-3 text-midSecondary">
          last updated {ad.updated}
        </div>
      </div>
    </div>
  </div>
</div>

<style>
  .col {
    background-color: transparent;
  }
  .card {
    border: none;
    border-radius: 40px;
    min-width: 400px; /* Adjust the width of your cards */
    pointer-events: auto;
  }

  .cardAnnonce {
    box-shadow: 0 1px 3px 0 #25201f4d;
    transition: 0.2s ease;
    text-decoration: none;
  }

  .cardAnnonce:hover {
    box-shadow: 2px 2px 3px 2px #25201f4d;
  }
  .card-body {
    padding: 16px 28px;
  }
  .card-footer {
    width: 100%;
    border-radius: 0 0 40px 40px;
    background-color: #d9d9d9;
  }

  .topCard {
    display: flex;
    flex-direction: row;
    padding: 0 50px 30px 50px;
    align-items: center;
    justify-content: space-between;
  }

  .colorTopAnnonce {
    border-radius: 40px;
    height: 40px;
    width: 90%;
    margin: 0 auto;
    width: 100%;
    height: 40px;
    border-radius: 30px;
  }

  .ad-card {
    padding: 16px;
    margin: 8px;
  }

  .ad-header {
    display: flex;
    justify-content: space-between;
    font-weight: bold;
  }

  .ad-body {
    margin-top: 8px;
  }

  .nomDateTopCard .DateTopCard {
    font-size: small;
    display: flex;
    justify-content: center;
  }

  .destinationTopCard {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
  }

  .dateCard {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
  }

  .tarifDetailsCard button {
    text-decoration: none;
    appearance: none;
    border: none;
    text-align: start;
  }
</style>
