<script>
  import Popup from "../../components/Popup.svelte";

  let userData = {
      name: "Ramy",
      email: "ramy@envoyage.com",
      phone: "+213 123 45 67 89",
      dateOfBirth: "24 / 06 / 2005 - 18 yo",
      address: "11 rue Bainem, El Hammamet",
      password: "**********",
      passport: "***********************"
  };

  let isEditing = false;
  let newFieldValue = "";
  let fieldName = "";
  let title = "";

  function openPopup(field) {
      isEditing = true;
      fieldName = field;

      switch (field) {
          case "name":
              title = "Edit your Name";
              newFieldValue = userData.name;
              break;
          case "email":
              title = "Edit your Email";
              newFieldValue = userData.email;
              break;
          case "phone":
              title = "Edit your Phone Number";
              newFieldValue = userData.phone;
              break;
          case "dateOfBirth":
              title = "Edit your Date of Birth / Age";
              newFieldValue = userData.dateOfBirth;
              break;
          case "address":
              title = "Edit your Address";
              newFieldValue = userData.address;
              break;
          case "password":
              title = "Change your Password";
              newFieldValue = userData.password;
              break;
          case "passport":
              title = "Edit your Passport Number";
              newFieldValue = userData.passport;
              break;
      }
  }

  function saveChanges() {
      switch (fieldName) {
          case "name":
              userData.name = newFieldValue;
              break;
          case "email":
            userData.email = newFieldValue;
              break;
          case "phone":
          userData.phone = newFieldValue;
              break;
          case "dateOfBirth":
          userData.dateOfBirth = newFieldValue;
              break;
          case "address":
          userData.address = newFieldValue;
              break;
          case "password":
          userData.password = newFieldValue;
              break;
          case "passport":
          userData.passport = newFieldValue;
              break;
      }
      isEditing = false;
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
      title={title}
      isOpen={isEditing}
      onClose={() => (isEditing = false)}
      bind:newFieldValue
      fieldName={fieldName}
      on:changesSaved={handleChangesSaved}
  >
      <input class={fieldName === 'phone' || fieldName === 'dateOfBirth' ? 'numberInput' : ''} bind:value={newFieldValue} />
      <button on:click={saveChanges} class="ButtonEdit btn border-0 bg-primary text-white">save</button>
  </Popup>
{/if}
  <div class="Profile fp">
    <div class="Profile-background bg-primary">
      <div class="ProfileTopCard">
        <p class="text-white fw-semibold fs-2 fontPrimary">{userData.name}'s profile</p>
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
            <span id="info-name">{userData.name}</span>
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
            <span class="fw-bold">{userData.email}</span>
            <button
              class="ButtonEdit btn border-0 bg-primary text-white"
              on:click={() => openPopup("email")}>edit</button
            >
          </div>
        </div>
        <div class="ProfileInfo fs-5">
          <p class="text-secondary">Phone Number</p>
          <div class="ProfileEditInfo">
            <span class="fw-bold">{userData.phone}</span>
            <button
              class="ButtonEdit btn border-0 bg-primary text-white"
              on:click={() => openPopup("phone")}>edit</button
            >
          </div>
        </div>
      </div>
      <div class="ProfileContainerDisplay fs">
        <p class="fs-3 mb-5">
          About <span class="text-primary">{userData.name}</span>
          <span class="text-muted">(facultatif)</span>
        </p>
        <div class="ProfileInfo fs-5">
          <p class="text-secondary">Date of birth / Age</p>
          <div class="ProfileEditInfo">
            <span class="fw-bold">{userData.dateOfBirth}</span>
            <button
              class="ButtonEdit btn border-0 bg-primary text-white"
              on:click={() => openPopup("dateOfBirth")}>edit</button
            >
          </div>
        </div>
        <div class="ProfileInfo fs-5">
          <p class="text-secondary">Adresse</p>
          <div class="ProfileEditInfo">
            <span class="fw-bold">{userData.address}</span>
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
            <span class="fw-bold">{userData.password}</span>
            <button
              class="ButtonEdit btn border-0 bg-primary text-white"
              on:click={() => openPopup("password")}>edit</button
            >
          </div>
        </div>
        <div class="ProfileInfo fs-5">
          <p class="text-secondary">Passport Number</p>
          <div class="ProfileEditInfo">
            <p class="fw-bold"><span class="fw-bold">{userData.passport}</span></p>
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
    height: 300px;
    display: block;
    justify-content: center;
    margin: auto;
  }

  .ProfileTopCard {
    padding: 40px 50px 80px 50px;
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

  .ProfileInfo {
    margin: 0 0 20px;
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
</style>
