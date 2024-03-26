<script>
 import Popup from "../../components/Popup.svelte";

// Déclarer des variables réactives
let name = "Ramy";
let isEditing = false;
let newName = name;
let fieldName = "";
let title = "";

// Ouvrir le pop-up pour éditer le champ spécifié
function openPopup(field) {
  isEditing = true;
  fieldName = field;

  // Mettre à jour le titre du pop-up en fonction du champ à éditer
  switch (field) {
    case "name":
      title = "Edit your Name";
      break;
    case "email":
      title = "Edit your Email";
      break;
    case "phone":
      title = "Edit your Phone Number";
      break;
    case "dob":
      title = "Edit your Date of Birth / Age";
      break;
    case "address":
      title = "Edit your Address";
      break;
    case "password":
      title = "Change your Password";
      break;
    case "passport":
      title = "Edit your Passport Number";
      break;
    // Ajoutez d'autres cas pour d'autres champs si nécessaire
  }
}
// Enregistrer les modifications après l'édition dans le pop-up
function saveChanges() {
  name = newName; // Mettre à jour le nom avec la nouvelle valeur
  isEditing = false; // Fermer le pop-up

  // Mettre à jour le champ spécifique qui a été édité
  const infoText = document.getElementById(`info-${fieldName}`);
  infoText.textContent = newName;
}

  function editInfo(field) {
    const inputField = document.getElementById(field);
    const infoText = document.getElementById(`info-${field}`);
    const editButton = document.getElementById(`edit-${field}`);

    inputField.style.display = "inline-block";
    infoText.style.display = "none";
    editButton.style.display = "none";

    inputField.focus();

    inputField.addEventListener("blur", () => {
      inputField.style.display = "none";
      infoText.style.display = "inline-block";
      editButton.style.display = "inline-block";
    });

    inputField.addEventListener("keydown", (event) => {
      if (event.key === "Enter") {
        newName = inputField.value;
        saveChanges();
      }
    });
  }
</script>

<main>
  {#if isEditing}
  <div class="overlay"></div>
  <Popup
    title={title} 
    isOpen={isEditing}
    onClose={() => (isEditing = false)}
    bind:newName
  >
    <input bind:value={newName} />
    <button on:click={saveChanges} class="ButtonEdit btn border-0 bg-primary text-white">Save</button>
  </Popup>
{/if}
  <div class="Profile fp">
    <div class="Profile-background bg-primary">
      <div class="ProfileTopCard">
        <p class="text-white fw-semibold fs-2 fontPrimary">{name}'s profile</p>
        <img src="../svg/VerifStar.svg" alt="Verif Star" />
      </div>
    <div class="ProfileDisplay card-shadow-gray">
      <div class="ProfileDisplayTopCard">
        <img src="../svg/image_profil.svg" alt="Photo de profile" />
        <button class="ButtonEdit btn border-0 bg-primary text-white fs"
          >upload image</button
        >
      </div>
      <div class="ProfileContainerDisplay fs">
        <p class="fs-2 mb-5">Importants informations</p>
        <div class="ProfileInfo fs-5">
          <p class="text-secondary">Your Name</p>
          <div class="ProfileEditInfo">
            <span id="info-name">{name}</span>
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
            <p class="fw-bold">{name}@envoyage.com</p>
            <button
              class="ButtonEdit btn border-0 bg-primary text-white"
              on:click={() => openPopup("email")}>edit</button
            >
          </div>
        </div>
        <div class="ProfileInfo fs-5">
          <p class="text-secondary">Phone Number</p>
          <div class="ProfileEditInfo">
            <p class="fw-bold">+213 123 45 67 89</p>
            <button
              class="ButtonEdit btn border-0 bg-primary text-white"
              on:click={() => openPopup("phone")}>edit</button
            >
          </div>
        </div>
      </div>
      <div class="ProfileContainerDisplay fs">
        <p class="fs-3 mb-5">
          About <span class="text-primary">{name}</span>
          <span class="text-muted">(facultatif)</span>
        </p>
        <div class="ProfileInfo fs-5">
          <p class="text-secondary">Date of birth / Age</p>
          <div class="ProfileEditInfo">
            <p class="fw-bold">24 / 06 / 2005 - 18 yo</p>
            <button
              class="ButtonEdit btn border-0 bg-primary text-white"
              on:click={() => openPopup("dob")}>edit</button
            >
          </div>
        </div>
        <div class="ProfileInfo fs-5">
          <p class="text-secondary">Adresse</p>
          <div class="ProfileEditInfo">
            <p class="fw-bold">11 rue Bainem, El Hammamet</p>
            <button
              class="ButtonEdit btn border-0 bg-primary text-white"
              on:click={() => openPopup("address")}>edit</button
            >
          </div>
        </div>
      </div>
      <div class="ProfileContainerDisplay fs">
        <p class="fs-3 mb-5">Security</p>
        <div class="ProfileInfo fs-5">
          <p class="text-secondary">Password</p>
          <div class="ProfileEditInfo">
            <p class="fw-bold">**********</p>
            <button
              class="ButtonEdit btn border-0 bg-primary text-white"
              on:click={() => openPopup("password")}>edit</button
            >
          </div>
        </div>
        <div class="ProfileInfo fs-5">
          <p class="text-secondary">Passport Number</p>
          <div class="ProfileEditInfo">
            <p class="fw-bold">***********************</p>
            <button
              class="ButtonEdit btn border-0 bg-primary text-white"
              on:click={() => openPopup("passport")}>edit</button
            >
          </div>
        </div>
      </div>
    </div>
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

  .Profile {
    padding: 120px 0 0 0;
    margin: 0 0 2000px 0;
  }

  .Profile-background {
    border-radius: 40px;
    width: 90%;
    height: 250px;
    display: block;
    justify-content: center;
    margin: auto;
  }

  .ProfileTopCard {
    padding: 40px 50px;
    display: flex;
    justify-content: space-between;
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
  }

  .ButtonEdit {
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

  .ProfileInfo fs-5 {
    margin: 10px 0;
  }

  .ProfileEditInfo {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
  }
</style>
