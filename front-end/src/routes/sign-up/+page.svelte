<script>
   // Code to handle clicks on sender and travler buttons
   document.addEventListener("DOMContentLoaded", () => {
       // Get all elements with the class "sender"
       const senderElements = document.querySelectorAll(".sender");
       // Get all elements with the class "travler"
       const travlerElements = document.querySelectorAll(".travler");

       // Add click event listeners to sender elements
       senderElements.forEach((sender) => {
           sender.addEventListener("click", () => {
               document.querySelectorAll(".tr").forEach((element) => {
                   element.classList.add("hidden");
               });
               document.querySelectorAll(".sn").forEach((element) => {
                   element.classList.remove("hidden");
               });
               console.log("Sender clicked");
           });
       });

       // Add click event listeners to travler elements
       travlerElements.forEach((travler) => {
           travler.addEventListener("click", () => {
               document.querySelectorAll(".tr").forEach((element) => {
                   element.classList.remove("hidden");
               });
               document.querySelectorAll(".sn").forEach((element) => {
                   element.classList.add("hidden");
               });
               console.log("Travler clicked");
           });
       });
   });
</script>


<div class="bd">
   <div class="singup tr m-auto">
      <div class="box p-0 buttons has-addons m-0">
         <button
            id=""
            class="sender button is-primary py-5 w-50 m-0 is-selected is-radiusless"
            >Sing up as Sender</button
         >
         <button
            id=""
            class="travler button w-50 py-5 m-0 is-radiusless"
            style="border:solid #fff 1px;">Travler</button
         >
      </div>
      <form class="box is-radiusless">
         <div
            class="field is-flex is-justify-content-space-between is-align-content-center"
         >
            <div class="control mx-3 w-100">
               <label class="label" for ="nom">Nom</label>
               <input 
               class="input is-rounded" 
               type="text" 
               placeholder="Nom " 
               id="nom" 
               />
            </div>
            <div class="control w-100 mx-3">
               <label class="label" for="prenom">Prénom</label>
               <input
                  class="input is-rounded"
                  type="text"
                  placeholder="Prénom"
                  id ="prenom"
               />
            </div>
         </div>
         <div
            class="field is-flex is-justify-content-space-between is-align-content-center"
         >
            <div class="control mx-3 w-100">
               <label class="label" for ="adresse">Address</label>
               <input
                  class="input is-rounded"
                  type="text"
                  placeholder="Address"
                  id ="adresse"
               />
            </div>
            <div class="control w-100 mx-3">
               <label class="label" for ="ddn">Date de naissance</label>
               <input 
               class="input is-rounded" 
               type="date" 
               placeholder="" 
               id ="ddn"
               />
            </div>
         </div>
         <!-- <label class="label is-block ml-3">Photo de passport</label>
        <div class="file has-name is-fullwidth mx-3">
            <label class="file-label">
                <input class="file-input" style="border-radius: 9999px !important;" type="file" name="resume">
                <span class="file-cta" style=" border-radius:  9999px 0px 0px 9999px ;">
                    <span class="file-icon">
                        <i class="fas fa-upload"></i>
                    </span>
                    <span class="file-label ">
                        Choose a file…
                    </span>
                </span>
                <span class="file-name" style=" border-radius: 0px 9999px 9999px 0px  !important;">
                    Screen Shot 2017-07-29 at 15.54.25.png
                </span>
            </label>
        </div> -->
         <div
            class="field is-flex is-justify-content-space-between is-align-content-center"
         >
            <div class="control mx-3 w-100">
               <label class="label" for="passport">Passport</label>
               <input
                  class="input is-rounded"
                  type="file"
                  placeholder="Address"
                  id="passport"
               />
            </div>
         </div>
         <div
            class="field is-flex is-justify-content-space-between is-align-content-center"
         >
            <div class="control mx-3 w-100">
               <label class="label" for ="email">Email</label>
               <input
                  class="input is-rounded"
                  type="email"
                  placeholder="Email"
                  id ="email"
               />
            </div>
         </div>
         <div
            class="field is-flex is-justify-content-space-between is-align-content-center"
         >
            <div class="control mx-3 w-100">
               <label class="label" for ="password">mot de passe</label>
               <input
                  class="input is-rounded"
                  type="password"
                  placeholder="**************"
                  id ="password"
               />
            </div>
            <div class="control w-100 mx-3">
               <label class="label" for="ConfirmPassword">confirmer le mot de passe</label>
               <input
                  class="input is-rounded"
                  type="password"
                  placeholder="**************"
                  id ="ConfirmPassword"
               />
            </div>
         </div>

         <div class="is-justify-content-center mt-5 is-flex">
            <button
               class="button mt-2 px-6 py-5 has-text-weight-bold bbtn is-rounded is-primary"
               >Sign in</button
            >
         </div>
      </form>
   </div>
   <div class="singup sn m-auto">
      <div class="box p-0 buttons has-addons m-0">
         <button
            id=""
            class="sender button is-primary py-5 w-50 m-0 is-selected is-radiusless"
            >Sing up as Sender</button
         >
         <button
            id=""
            class="travler button w-50 py-5 m-0 is-radiusless"
            style="border:solid #fff 1px;">Travler</button
         >
      </div>
      <form class="box is-radiusless has-background-primary">
         <div
            class="field is-flex is-justify-content-space-between is-align-content-center"
         >
            <div class="control mx-3 w-100">
               <label class="label" for ="Sender-nom">Nom</label>
               <input 
               class="input is-rounded" 
               type="text" 
               placeholder="Nom " 
               id ="Sender-nom"
               />
            </div>
            <div class="control w-100 mx-3">
               <label class="label" for ="Sender-prenom">Prénom</label>
               <input
                  class="input is-rounded"
                  type="text"
                  placeholder="Prénom"
                  id="Sender-prenom"
               />
            </div>
         </div>
         <div
            class="field is-flex is-justify-content-space-between is-align-content-center"
         >
            <div class="control mx-3 w-100">
               <label class="label" for ="Sender-email">Email</label>
               <input
                  class="input is-rounded"
                  type="email"
                  placeholder="Email"
                  id="Sender-email"
               />
            </div>
         </div>
         <div
            class="field is-flex is-justify-content-space-between is-align-content-center"
         >
            <div class="control mx-3 w-100">
               <label class="label" for="Sender-password">mot de passe</label>
               <input
                  class="input is-rounded"
                  type="password"
                  placeholder="**************"
                  id ="Sender-password"
               />
            </div>
            <div class="control w-100 mx-3">
               <label class="label" for ="Sender-ConfirmPassword">confirmer le mot de passe</label>
               <input
                  class="input is-rounded"
                  type="password"
                  placeholder="**************"
                  id="Sender-ConfirmPassword"
               />
            </div>
         </div>

         <div class="is-justify-content-center mt-5 is-flex">
            <button
               class="button mt-2 px-6 py-5 has-text-weight-bold bbtn is-rounded is-primary"
               >Sign in</button
            >
         </div>
      </form>
   </div>
</div>
