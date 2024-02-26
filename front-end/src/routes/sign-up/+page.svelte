<script>
   document.addEventListener("DOMContentLoaded", () => {
       // Get all elements with the class "sender"
       const senderElements = document.querySelectorAll(".sender");
       // Get all elements with the class "travler"
       const travlerElements = document.querySelectorAll(".travler");
       
       // Add click event listeners to sender elements
       senderElements.forEach((sender) => {
           sender.addEventListener("click", () => {
               // Hide elements with class "tr"
               document.querySelectorAll(".tr").forEach((element) => {
                   element.style.display = "none";
                   element.style.transition = "transform 1s";
               });
               // Show elements with class "sn"
               document.querySelectorAll(".sn").forEach((element) => {
                   element.style.display = "block";
                   element.style.transition = "transform 1s";
               });
           });
       });
       
       // Add click event listeners to travler elements
       travlerElements.forEach((travler) => {
           travler.addEventListener("click", () => {
               // Show elements with class "tr"
               document.querySelectorAll(".tr").forEach((element) => {
                   element.style.display = "block";
                   element.style.transition = "transform 1s";
               });
               // Hide elements with class "sn"
               document.querySelectorAll(".sn").forEach((element) => {
                   element.style.display = "none";
                   element.style.transition = "transform 1s";
               });
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
            style="border:solid #fff 1px;">Maybe</button
         >
      </div>
      <form class="box is-radiusless">
         <div
            class="field is-flex is-justify-content-space-between is-align-content-center"
         >
            <div class="control mx-3 w-100">
               <label class="label">Nom</label>
               <input class="input is-rounded" type="text" placeholder="Nom " />
            </div>
            <div class="control w-100 mx-3">
               <label class="label">Prénom</label>
               <input
                  class="input is-rounded"
                  type="text"
                  placeholder="Prénom"
               />
            </div>
         </div>
         <div
            class="field is-flex is-justify-content-space-between is-align-content-center"
         >
            <div class="control mx-3 w-100">
               <label class="label">Address</label>
               <input
                  class="input is-rounded"
                  type="text"
                  placeholder="Address"
               />
            </div>
            <div class="control w-100 mx-3">
               <label class="label">Date de naissance</label>
               <input class="input is-rounded" type="date" placeholder="" />
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
               <label class="label">Passport</label>
               <input
                  class="input is-rounded"
                  type="file"
                  placeholder="Address"
               />
            </div>
         </div>
         <div
            class="field is-flex is-justify-content-space-between is-align-content-center"
         >
            <div class="control mx-3 w-100">
               <label class="label">Email</label>
               <input
                  class="input is-rounded"
                  type="email"
                  placeholder="Email"
               />
            </div>
         </div>
         <div
            class="field is-flex is-justify-content-space-between is-align-content-center"
         >
            <div class="control mx-3 w-100">
               <label class="label">mot de passe</label>
               <input
                  class="input is-rounded"
                  type="password"
                  placeholder="**************"
               />
            </div>
            <div class="control w-100 mx-3">
               <label class="label">confirmer le mot de passe</label>
               <input
                  class="input is-rounded"
                  type="password"
                  placeholder="**************"
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
            style="border:solid #fff 1px;">Maybe</button
         >
      </div>
      <form class="box is-radiusless has-background-primary">
         <div
            class="field is-flex is-justify-content-space-between is-align-content-center"
         >
            <div class="control mx-3 w-100">
               <label class="label">Nom</label>
               <input class="input is-rounded" type="text" placeholder="Nom " />
            </div>
            <div class="control w-100 mx-3">
               <label class="label">Prénom</label>
               <input
                  class="input is-rounded"
                  type="text"
                  placeholder="Prénom"
               />
            </div>
         </div>
         <div
            class="field is-flex is-justify-content-space-between is-align-content-center"
         >
            <div class="control mx-3 w-100">
               <label class="label">Email</label>
               <input
                  class="input is-rounded"
                  type="email"
                  placeholder="Email"
               />
            </div>
         </div>
         <div
            class="field is-flex is-justify-content-space-between is-align-content-center"
         >
            <div class="control mx-3 w-100">
               <label class="label">mot de passe</label>
               <input
                  class="input is-rounded"
                  type="password"
                  placeholder="**************"
               />
            </div>
            <div class="control w-100 mx-3">
               <label class="label">confirmer le mot de passe</label>
               <input
                  class="input is-rounded"
                  type="password"
                  placeholder="**************"
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
