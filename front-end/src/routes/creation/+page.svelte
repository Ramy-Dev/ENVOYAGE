<script>
  import Popup from "../../components/Popup.svelte";

  let userData = {
    name: "Ramy",
    email: "ramy@envoyage.com",
    phone: "+213 123 45 67 89",
    dateOfBirth: "24 / 06 / 2005 - 18 yo",
    address: "11 rue Bainem, El Hammamet",
    password: "**********",
    passport: "***********************",
  };

  let isEditing = false;
  let newFieldValue = "";
  let fieldName = "";
  let title = "";
  let isProfileActive = true;

  //*************************************/

  let newTag = "";
  let tags = [];

  function handleTagInput(event) {
    if (event.key === "Enter" && newTag.trim() !== "") {
      tags = [...tags, newTag.trim()];
      newTag = "";
    }
  }

  function removeTag(tagToRemove) {
    tags = tags.filter((tag) => tag !== tagToRemove);
  }
  //*************************************/

  function toggleColis() {
    isProfileActive = true;
  }

  function toggleCourrier() {
    isProfileActive = false;
  }
  function toggleProfileAndToggle() {
    toggleColis();
    toggle();
  }

  function toggleHistoryAndToggle() {
    toggleCourrier();
    toggle();
  }

  const toggle = (event) => {
    const clickedButton = event.target.closest("button");
    const clickedTarif = clickedButton.querySelector(".choiceProfileBtn");
    const otherTarif =
      clickedTarif.id === "c1"
        ? document.getElementById("c2")
        : document.getElementById("c1");

    if (clickedTarif.classList.contains("colorProfileOriginalSwitch")) return;

    // Désactiver toutes les classes colorOriginalSwitch
    document
      .querySelectorAll(".choiceProfileBtn.colorProfileOriginalSwitch")
      .forEach((tarif) => {
        tarif.classList.remove("colorProfileOriginalSwitch");
        tarif.classList.add("colorProfileSecondarySwitch");
      });

    // Activer la classe colorOriginalSwitch pour le bouton cliqué
    clickedTarif.classList.add("colorProfileOriginalSwitch");
    clickedTarif.classList.remove("colorProfileSecondarySwitch");

    // Activer le bouton cliqué
    clickedButton.disabled = false;
  };
</script>

<main>
  <div class="Profile">
    <div class="Profile-background">
      <div class="ProfileTopCard">
        <p class="text-primary fw-semibold fs-2 fontPrimary">
          Post your Ad
          <span class="text-white bg-primary rounded px-2">{userData.name}</span
          >
        </p>
      </div>

      <div class="choiceProfile bg-primary">
        <div class="ProfileDisplay card-shadow-gray">
          <div class="pt-5 ProfileDisplayTopCard">
            <p class="fs-1 fw-bold text-darkPrimary fontPrimary">
              General informations
            </p>
          </div>
          <div class="departureCreation">
            <p class="fs-3 fw-bold text-primary fontPrimary my-4">
              Departure :
            </p>
            <div class="ProfileContainerDisplay">
              <div class="parentGridCreation">
                <div class="airportDepartureCreation">
                  <div class="airportDepartureCreation">
                    <p class="fs-3 fw-bold text-darkPrimary fontPrimary">
                      Airport :
                    </p>
                  </div>
                </div>
                <div class="airportDepartureCreationInput">
                  <div class="input-box-creation">
                    <input
                      class="fs-5 fw-normal text-primary fontSecondary"
                      type="text"
                      placeholder="choose an airport"
                      required
                    />
                  </div>
                </div>
                <div class="dateDepartureCreation">
                  <div class="dateDepartureCreation">
                    <p class="fs-3 fw-bold text-darkPrimary fontPrimary">
                      Date :
                    </p>
                  </div>
                </div>
                <div class="DateDepartureCreationInput">
                  <div class="input-box-date-creation">
                    <input
                      class="DateInput fs-5 fw-normal text-primary fontSecondary"
                      type="date"
                      required
                    />
                  </div>
                </div>
                <div class="hoursMinutesDateDepartureCreationInput">
                  <div class="input-box-date-creation">
                    <input
                      class="DateInput fs-5 fw-normal text-primary fontSecondary"
                      type="time"
                      required
                    />
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="arrivalCreation">
            <p class="fs-3 fw-bold text-primary fontPrimary my-4">Arrival :</p>

            <div class="ProfileContainerDisplay">
              <div class="parentGridCreation">
                <div class="airportDepartureCreation">
                  <div class="airportDepartureCreation">
                    <p class="fs-3 fw-bold text-darkPrimary fontPrimary">
                      Airport :
                    </p>
                  </div>
                </div>
                <div class="airportDepartureCreationInput">
                  <div class="input-box-creation">
                    <input
                      class="fs-5 fw-normal text-primary fontSecondary"
                      type="text"
                      placeholder="choose an airport"
                      required
                    />
                  </div>
                </div>
                <div class="dateDepartureCreation">
                  <div class="dateDepartureCreation">
                    <p class="fs-3 fw-bold text-darkPrimary fontPrimary">
                      Date :
                    </p>
                  </div>
                </div>
                <div class="DateDepartureCreationInput">
                  <div class="input-box-date-creation">
                    <input
                      class="DateInput fs-5 fw-normal text-primary fontSecondary"
                      type="date"
                      required
                    />
                  </div>
                </div>
                <div class="hoursMinutesDateDepartureCreationInput">
                  <div class="input-box-date-creation">
                    <input
                      class="DateInput fs-5 fw-normal text-primary fontSecondary"
                      type="time"
                      required
                    />
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="conditionCreation">
            <p class="fs-3 fw-bold text-primary fontPrimary my-4">
              Conditions :
            </p>
            <div class="ProfileContainerDisplay">
              <div class="tagInputBox">
                <input
                  class="fs-5 fw-normal text-primary fontSecondary"
                  type="text"
                  placeholder="Enter tags..."
                  bind:value={newTag}
                  on:keydown={handleTagInput}
                />
              </div>
              <div class="tagContainer">
                {#each tags as tag}
                  <div class="tagBadge">
                    {tag}
                    <button class="removeTagBtn fontSecondary" on:click={() => removeTag(tag)}
                      >.x.</button
                    >
                  </div>
                {/each}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</main>

<style>
  .ProfileTopCard {
    padding: 40px 50px 50px 0;
  }

  .choiceProfile {
    border-radius: 40px;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 60px 0px 186px 0px;
    height: 20px;
    background-color: #007bff; /* Couleur de fond */
  }

  .ProfileDisplay {
    width: 80%;
    margin: auto;
    margin-top: 70px;
    display: flex;
    flex-direction: column;
    padding: 60px 150px;
    border-radius: 40px;
    background-color: #ffffff;
    gap: 50px;
  }

  .ProfileDisplayTopCard {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .ProfileContainerDisplay {
    padding: 50px 100px;
    border: 2px solid #b6b3b3;
    border-radius: 40px;
    box-shadow: 0 4px 4px 0 rgba(0, 0, 0, 0.25);
    display: flex;
    flex-direction: column;
    gap: 50px;
  }

  .input-box-creation input {
    width: 100%;
    padding: 1.5rem 7rem;
    border-radius: 20px;
    border: 2px solid #b6b3b3;
    box-shadow: 0 3px 3px 0 rgba(0, 0, 0, 0.25);
    text-align: center; /* Centrer le contenu */
  }
  .input-box-creation input::placeholder {
    text-align: center;
  }
  .input-box-date-creation {
    display: flex;
    justify-content: center; /* Centrer horizontalement */
    align-items: center; /* Centrer verticalement */
  }
  .input-box-date-creation input {
    padding: 1.5rem 2rem;
    width: 50%;
    border-radius: 20px;
    border: 2px solid #b6b3b3;
    box-shadow: 0 3px 3px 0 rgba(0, 0, 0, 0.25);
  }
  .input-box-date-creation input::placeholder {
    text-align: center;
  }
  .airportDepartureCreation {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .dateDepartureCreation {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .DateInput {
    display: flex;
    justify-content: center;
    text-align: center;
  }
  .parentGridCreation {
    display: grid;
    grid-template-columns: repeat(2, 1fr) 2fr 1fr;
    grid-template-rows: repeat(3, 1fr);
    grid-column-gap: 50px;
    grid-row-gap: 0px;
  }

  .airportDepartureCreation {
    grid-area: 1 / 1 / 2 / 2;
  }
  .airportDepartureCreationInput {
    grid-area: 1 / 3 / 2 / 5;
  }
  .dateDepartureCreation {
    grid-area: 3 / 1 / 4 / 2;
  }
  .DateDepartureCreationInput {
    grid-area: 3 / 3 / 4 / 4;
  }
  .DateDepartureCreationInput input {
    width: 100%;
  }
  .hoursMinutesDateDepartureCreationInput {
    grid-area: 3 / 4 / 4 / 5;
  }
  .hoursMinutesDateDepartureCreationInput input {
    width: 100%;
  }
  .tagInputBox {
    margin-bottom: 20px;
  }

  .tagContainer {
    display: flex;
    flex-wrap: wrap;
  }

  .removeTagBtn {
    background-color: transparent;
    border: none;
    color: white;
    margin-left: 5px;
    cursor: pointer;
  }
</style>
