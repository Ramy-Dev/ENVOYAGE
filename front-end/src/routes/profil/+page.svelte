<script>
  import Popup from "../../components/Popup.svelte";
  import { onMount } from "svelte";
  import { tick } from "svelte";

  let userData = [];
  let isEditing = false;
  let newFieldValue = "";
  let fieldName = "";
  let title = "";
  let isProfileActive = true;

  
  onMount(async () => {
    const token = localStorage.getItem("authToken");
    userData = await fetchUserData(token);
    // Now userData should be populated
    console.log("User data loaded:", userData);
});

async function fetchUserData(token) {
    try {
        const response = await fetch("http://127.0.0.1:8000/utilisateurs/", {
            headers: {
                "Authorization": `Token ${token}`
            }
        });

        if (response.ok) {
            const data = await response.json();
            console.log("Fetched user data:", data);
            return data; // Ensure to return the fetched data
        } else {
            console.error("Failed to fetch user info.");
            return {}; // Return an empty object or handle the error as needed
        }
    } catch (error) {
        console.error("Error fetching user info:", error);
        return {}; // Return an empty object or handle the error as needed
    }
}

  function toggleProfile() {
    isProfileActive = true;
    console.log(userData, userData[0].username);
  }

  function toggleHistory() {
    isProfileActive = false;
  }

  function toggleProfileAndToggle() {
    toggleProfile();
    toggle();
  }

  function toggleHistoryAndToggle() {
    toggleHistory();
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

    document
      .querySelectorAll(".choiceProfileBtn.colorProfileOriginalSwitch")
      .forEach((tarif) => {
        tarif.classList.remove("colorProfileOriginalSwitch");
        tarif.classList.add("colorProfileSecondarySwitch");
      });

    clickedTarif.classList.add("colorProfileOriginalSwitch");
    clickedTarif.classList.remove("colorProfileSecondarySwitch");

    clickedButton.disabled = false;
  };

  function openPopup(field) {
    isEditing = true;
    fieldName = field;

    switch (field) {
      case "name":
        title = "Edit your Name";
        newFieldValue = userData[0].first_name;
        break;
      case "email":
        title = "Edit your Email";
        newFieldValue = userData[0].email;
        break;
      case "phone":
        title = "Edit your Phone Number";
        newFieldValue = userData[0].numero_telephone;
        break;
      case "dateOfBirth":
        title = "Edit your Date of Birth / Age";
        newFieldValue = userData[0].date_de_naissance;
        break;
      case "address":
        title = "Edit your Address";
        newFieldValue = userData[0].adresse;
        break;
      case "password":
        title = "Change your Password";
        newFieldValue = userData[0].password; // Placeholder, you might not want to display password
        break;
      case "passport":
        title = "Edit your Passport Number";
        newFieldValue = userData[0].numero_passeport;
        break;
    }
  }

  function saveChanges() {
    switch (fieldName) {
      case "name":
        userData[0].first_name = newFieldValue;
        break;
      case "email":
        userData[0].email = newFieldValue;
        break;
      case "phone":
        userData[0].numero_telephone = newFieldValue;
        break;
      case "dateOfBirth":
        userData[0].date_de_naissance = newFieldValue;
        break;
      case "address":
        userData[0].adresse = newFieldValue;
        break;
      case "password":
        userData[0].password = newFieldValue;
        break;
      case "passport":
        userData[0].numero_passeport = newFieldValue;
        break;
    }
    isEditing = false;

    tick().then(() => {
    // Optionally, you can perform additional operations here if needed
  });
  }

  function handleChangesSaved(event) {
    const { fieldName, newValue } = event.detail;
    userData[fieldName] = newValue;
  }

  $: {
    console.log("Updated userData:", userData);
  }
</script>

<main>
  {#if isEditing}
    <div class="overlay"></div>
    <Popup
      {title}
      isOpen={isEditing}
      onClose={() => (isEditing = false)}
      bind:newFieldValue
      {fieldName}
      on:changesSaved={handleChangesSaved}
    >
      <input
        class={fieldName === "phone" || fieldName === "dateOfBirth"
          ? "numberInput"
          : ""}
        bind:value={newFieldValue}
      />
      <button
        on:click={saveChanges}
        class="ButtonEdit btn border-0 bg-primary text-white">save</button
      >
    </Popup>
  {/if}

  <div class="Profile fp">
    <div class="Profile-background bg-primary">
      <div class="ProfileTopCard">
        <p class="text-white fw-semibold fs-2 fontPrimary">
          {#if isProfileActive}
            {userData[0]?.username || 'N/A'}'s profile
          {:else}
            {userData[0]?.username}'s history
          {/if}
        </p>
        <img src="../svg/VerifStar.svg" alt="Verif Star" />
      </div>

      <div class="choiceProfile" id="tarifs">
        <button
          class="border-0"
          type="button"
          on:click={toggleProfileAndToggle}
        >
          <div
            class="choiceProfileBtn {isProfileActive
              ? 'colorProfileOriginalSwitch'
              : 'colorProfileSecondarySwitch'} fw-bold fs-5"
            id="c1"
          >
            Profile
          </div>
        </button>
        <button
          class="border-0"
          type="button"
          on:click={toggleHistoryAndToggle}
        >
          <div
            class="choiceProfileBtn {!isProfileActive
              ? 'colorProfileOriginalSwitch'
              : 'colorProfileSecondarySwitch'} fw-bold fs-5"
            id="c2"
          >
            History
          </div>
        </button>
      </div>

      {#if isProfileActive}
        <div class="ProfileDisplay card-shadow-gray">
          <div class="ProfileDisplayTopCard">
            <img src="../svg/image_profil.svg" alt="Photo de profile" />
            <button class="ImageEdit btn text-primary fontSecondary"
              >upload image</button
            >
          </div>
          <div class="ProfileContainerDisplay fontSecondary">
            <p class="fs-2 mb-5">Important information</p>
            <div class="ProfileInfo fs-5">
              <p class="text-secondary">Your Name</p>
              <div class="ProfileEditInfo">
                <span id="info-name">{userData[0]?.first_name}</span>
                <button
                  id="edit-name"
                  class="ButtonEdit btn border-0 bg-primary text-white"
                  on:click={() => openPopup("name")}>edit</button
                >
              </div>
            </div>
            <div class="ProfileInfo fs-5">
              <p class="text-secondary">Email</p>
              <div class="ProfileEditInfo">
                <span class="fw-bold">{userData[0]?.email}</span>
                <button
                  class="ButtonEdit btn border-0 bg-primary text-white"
                  on:click={() => openPopup("email")}>edit</button
                >
              </div>
            </div>
            <div class="ProfileInfo fs-5">
              <p class="text-secondary">Phone Number</p>
              <div class="ProfileEditInfo">
                <span class="fw-bold">{userData[0]?.numero_telephone}</span>
                <button
                  class="ButtonEdit btn border-0 bg-primary text-white"
                  on:click={() => openPopup("phone")}>edit</button
                >
              </div>
            </div>
          </div>
          <div class="ProfileContainerDisplay fontSecondary">
            <p class="fs-3 mb-5">
              About <span class="text-primary">{userData[0]?.first_name}</span>
              <span class="text-muted">(optional)</span>
            </p>
            <div class="ProfileInfo fs-5">
              <p class="text-secondary">Date of birth / Age</p>
              <div class="ProfileEditInfo">
                <span class="fw-bold">{userData[0]?.date_de_naissance}</span>
                <button
                  class="ButtonEdit btn border-0 bg-primary text-white"
                  on:click={() => openPopup("dateOfBirth")}>edit</button
                >
              </div>
            </div>
            <div class="ProfileInfo fs-5">
              <p class="text-secondary">Address</p>
              <div class="ProfileEditInfo">
                <span class="fw-bold">{userData[0]?.adresse}</span>
                <button
                  class="ButtonEdit btn border-0 bg-primary text-white"
                  on:click={() => openPopup("address")}>edit</button
                >
              </div>
            </div>
            <div class="ProfileInfo fs-5">
              <p class="text-secondary">Password</p>
              <div class="ProfileEditInfo">
                <span class="fw-bold">********</span>
                <button
                  class="ButtonEdit btn border-0 bg-primary text-white"
                  on:click={() => openPopup("password")}>edit</button
                >
              </div>
            </div>

            {#if userData[0]?.is_voyageur}
              <div class="ProfileInfo fs-5">
                <p class="text-secondary">Passport Number</p>
                <div class="ProfileEditInfo">
                  <span class="fw-bold">{userData[0]?.numero_passeport}</span>
                  <button
                    class="ButtonEdit btn border-0 bg-primary text-white"
                    on:click={() => openPopup("passport")}>edit</button
                  >
                </div>
              </div>
            {/if}
          </div>
        </div>

      {:else}
        <!-- Afficher le contenu de le partie history -->

        <div class="ProfileDisplay card-shadow-gray">
          <p class="profileTitle text-primary fs-2 fw-bold mb-2">My Ads</p>
          <div class="album py-5">
            <div class="container containerAnnonces">
               <div
                  class="row row-cols-1 row-cols-md-2 g-5 px-5"
                  id="cardsContainer"
               >
          <div class="col">
            <a href="" class="card cardAnnonce h-100 redirection-div">
              <div class="card-body">
                <div class="colorTopAnnonce mb-3"></div>
                <div class="topCard">
                  <img src="../svg/photoProfile.svg" class="card-img-top" alt="..." />
                  <div class="nomDateTopCard">
                    <h5 class="card-title fw-bold">
                      Amine Izem
                    </h5>
                    <h5 class="card-title DateTopCard fw-semibold">
                        24/06/2005
                    </h5>
                  </div>
                </div>
                <div class="destinationTopCard fw-semibold fs-5">
                  <div class="departureTopCard">Alger</div>
                  <svg class="svgArrow mt-2 mx-3" viewBox="246.554 219.198 189.9 12" width="189.9" height="12" xmlns="http://www.w3.org/2000/svg" xmlns:bx="https://boxy-svg.com">
                    <!-- svelte-ignore illegal-attribute-character -->
                    <path d="M 246.554 223.198 H 425.454 L 425.454 219.198 L 436.454 225.198 L 425.454 231.198 L 425.454 227.198 H 246.554 V 223.198 Z" style="fill-rule: nonzero;" transform="matrix(1.0000000000000002, 0, 0, 1.0000000000000002, 0, 0)" bx:shape="arrow 246.554 219.198 189.9 12 4 11 0 1@4082cbfb" />
                  </svg>
                  <div class="arrivalTopCard">Paris</div>
                </div>
                <div class="dateCard pt-4 pb-2 fw-semibold">
                  Date : 30/03/2024
                </div>
              </div>
              <div class="card-footer">
                <small class="text-body-secondary">Last updated mins ago</small>
              </div>
            </a>
          </div>
          <div class="col">
            <a href="" class="card cardAnnonce h-100 redirection-div">
              <div class="card-body">
                <div class="colorTopAnnonce mb-3"></div>
                <div class="topCard">
                  <img src="../svg/photoProfile.svg" class="card-img-top" alt="..." />
                  <div class="nomDateTopCard">
                    <h5 class="card-title fw-bold">
                      Amine Izem
                    </h5>
                    <h5 class="card-title DateTopCard fw-semibold">
                        24/06/2005
                    </h5>
                  </div>
                </div>
                <div class="destinationTopCard fw-semibold fs-5">
                  <div class="departureTopCard">Alger</div>
                  <svg class="svgArrow mt-2 mx-3" viewBox="246.554 219.198 189.9 12" width="189.9" height="12" xmlns="http://www.w3.org/2000/svg" xmlns:bx="https://boxy-svg.com">
                    <!-- svelte-ignore illegal-attribute-character -->
                    <path d="M 246.554 223.198 H 425.454 L 425.454 219.198 L 436.454 225.198 L 425.454 231.198 L 425.454 227.198 H 246.554 V 223.198 Z" style="fill-rule: nonzero;" transform="matrix(1.0000000000000002, 0, 0, 1.0000000000000002, 0, 0)" bx:shape="arrow 246.554 219.198 189.9 12 4 11 0 1@4082cbfb" />
                  </svg>
                  <div class="arrivalTopCard">Paris</div>
                </div>
                <div class="dateCard pt-4 pb-2 fw-semibold">
                  Date : 30/03/2024
                </div>
              </div>
              <div class="card-footer">
                <small class="text-body-secondary">Last updated mins ago</small>
              </div>
            </a>
          </div>
          <div class="col">
            <a href="" class="card cardAnnonce h-100 redirection-div">
              <div class="card-body">
                <div class="colorTopAnnonce mb-3"></div>
                <div class="topCard">
                  <img src="../svg/photoProfile.svg" class="card-img-top" alt="..." />
                  <div class="nomDateTopCard">
                    <h5 class="card-title fw-bold">
                      Amine Izem
                    </h5>
                    <h5 class="card-title DateTopCard fw-semibold">
                        24/06/2005
                    </h5>
                  </div>
                </div>
                <div class="destinationTopCard fw-semibold fs-5">
                  <div class="departureTopCard">Alger</div>
                  <svg class="svgArrow mt-2 mx-3" viewBox="246.554 219.198 189.9 12" width="189.9" height="12" xmlns="http://www.w3.org/2000/svg" xmlns:bx="https://boxy-svg.com">
                    <!-- svelte-ignore illegal-attribute-character -->
                    <path d="M 246.554 223.198 H 425.454 L 425.454 219.198 L 436.454 225.198 L 425.454 231.198 L 425.454 227.198 H 246.554 V 223.198 Z" style="fill-rule: nonzero;" transform="matrix(1.0000000000000002, 0, 0, 1.0000000000000002, 0, 0)" bx:shape="arrow 246.554 219.198 189.9 12 4 11 0 1@4082cbfb" />
                  </svg>
                  <div class="arrivalTopCard">Paris</div>
                </div>
                <div class="dateCard pt-4 pb-2 fw-semibold">
                  Date : 30/03/2024
                </div>
              </div>
              <div class="card-footer">
                <small class="text-body-secondary">Last updated mins ago</small>
              </div>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
      {/if}
    </div>
  </div>
</main>

<style>
  .overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5); /* Opacité réduite */
    z-index: 999; /* Assure que la superposition est au-dessus de tout */
  }

 

  .ProfileDisplay {
    width: 80%;
    margin: auto;
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
    padding: 0px 90px 0 60px;
  }

  .ButtonEdit {
    padding: 0.5rem 2.5rem;
    border-radius: 20px;
    font-size: 1.25rem;
  }
  .ImageEdit {
    border: 2px dashed #5A02D4;
    padding: 0.5rem 2.5rem;
    border-radius: 20px;
    font-size: 1.25rem;
  }
  .ProfileContainerDisplay {
    padding: 40px 60px;
    border: 2px solid #b6b3b3;
    border-radius: 40px;
    box-shadow: 0 4px 4px 0 rgba(0, 0, 0, 0.25);
  }

  .ProfileInfo {
    margin: 0 30px 20px 30px;
  }

  .ProfileEditInfo {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
  }
  
  p {
    margin-bottom: 0;
  }
  .profileTitle {
    display: flex;
    justify-content: center;
  }
  .card {
      border: none;
      border-radius: 20px;
   }
   .colorTopAnnonce {
      height: 30px;
   }
   .topCard {
      display: flex;
      flex-direction: row;
      padding: 0 50px 30px 50px;
      align-items: center;
      justify-content: space-between;
   }

</style>
