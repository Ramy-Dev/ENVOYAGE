<script>

let name = "Ramy"
</script>

<main>
    <div class="Profile fp">
        <div class="Profile-background bg-primary">
            <div class="ProfileTopCard">
                <p class="text-white fw-semibold fs-2 fontPrimary">{name}'s profile</p>
                <img src="../svg/VerifStar.svg" alt="Verif Star">
            </div>
            <div class="ProfileDisplay card-shadow-gray">
                <div class="ProfileDisplayTopCard">
                    <img src="../svg/image_profil.svg" alt="Photo de profile">
                    <button class="ButtonEdit btn border-0 bg-primary text-white fs">upload image</button>
                </div>
                <div class="ProfileContainerDisplay fs">
                    <p class="fs-3 mb-5">Importants informations</p>
                    <div class="ProfileInfo">
                        <p class="text-secondary">Your Name</p>
                        <div class="ProfileEditInfo">
                        <p class="fw-bold">{name}</p>
                        <button class="ButtonEdit btn border-0 bg-primary text-white">edit</button>
                        </div>
                    </div>
                    <div class="ProfileInfo">
                        <p class="text-secondary">Email</p>
                        <div class="ProfileEditInfo">
                        <p class="fw-bold">{name}@envoyage.com</p>
                        <button class="ButtonEdit btn border-0 bg-primary text-white">edit</button>
                        </div>
                    </div>
                    <div class="ProfileInfo">
                        <p class="text-secondary">Phone Number</p>
                        <div class="ProfileEditInfo">
                        <p class="fw-bold">+213 123 45 67 89</p>
                        <button class="ButtonEdit btn border-0 bg-primary text-white">edit</button>
                        </div>
                    </div>
                </div>
                <div class="ProfileContainerDisplay fs">
                    <p class="fs-3 mb-5">About <span class="text-primary">{name}</span> <span class="text-muted">(facultatif)</span></p>
                    <div class="ProfileInfo">
                        <p class="text-secondary">Date of birth / Age</p>
                        <div class="ProfileEditInfo">
                        <p class="fw-bold">24 / 06 / 2005 - 18 yo</p>
                        <button class="ButtonEdit btn border-0 bg-primary text-white">edit</button>
                        </div>
                    </div>
                    <div class="ProfileInfo">
                        <p class="text-secondary">Adresse</p>
                        <div class="ProfileEditInfo">
                        <p class="fw-bold">11 rue Bainem, El Hammamet</p>
                        <button class="ButtonEdit btn border-0 bg-primary text-white">edit</button>
                        </div>
                    </div>
                </div>
                <div class="ProfileContainerDisplay fs">
                    <p class="fs-3 mb-5">Security</p>
                    <div class="ProfileInfo">
                        <p class="text-secondary">Password</p>
                        <div class="ProfileEditInfo">
                        <p class="fw-bold">**********</p>
                        <button class="ButtonEdit btn border-0 bg-primary text-white">edit</button>
                        </div>
                    </div>
                    <div class="ProfileInfo">
                        <p class="text-secondary">Passport Number</p>
                        <div class="ProfileEditInfo">
                        <p class="fw-bold">***********************</p>
                        <button class="ButtonEdit btn border-0 bg-primary text-white">edit</button>
                        </div>
                    </div>
                </div>
            </div>
        </div> 
    </div>
</main>

<style>


    .Profile {
        padding:  120px 0 0 0;
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
    }
    .ProfileContainerDisplay {
        padding: 40px 60px ;
        border: 2px solid #B6B3B3;
        border-radius: 40px;
        box-shadow: 0 4px 4px 0 rgba(0, 0, 0, 0.25);
    }
    .ProfileInfo{
        margin: 10px 0;
    }
    .ProfileEditInfo {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
    }
</style>