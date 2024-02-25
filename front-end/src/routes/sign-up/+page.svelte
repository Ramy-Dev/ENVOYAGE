<script>
   document.addEventListener("DOMContentLoaded", () => {
      // Get all "navbar-burger" elements
      const $navbarBurgers = Array.prototype.slice.call(
         document.querySelectorAll(".navbar-burger"),
         0
      );

//       // Add a click event on each of them
//       $navbarBurgers.forEach((el) => {
//          el.addEventListener("click", () => {
//             // Get the target from the "data-target" attribute
//             const target = el.dataset.target;
//             const $target = document.getElementById(target);

//             // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
//             el.classList.toggle("is-active");
//             $target.classList.toggle("is-active");
//          });
//       });
//    });

//    $(".sender").on("click", function () {
//       $(".tr").css("display", "none");
//       $(".sn").css("display", "block");
//       $(".tr").css("transition", "transform 1s");
//    });

//    $(".travler").on("click", function () {
//       $(".tr").css("display", "block");
//       $(".sn").css("display", "none");
//       $(".sn").css("transition", "transform 1s");
//       $(".sn").css("transition", "transform 1s");
//    });
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
