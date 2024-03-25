<script>
   
   import { onMount } from "svelte";
   import ColorGenerator from "../../components/colorGenerator.svelte";
   import { getRandomColor } from "../../lib/functions/randomColor.js";
   // Fonction exécutée après le rendu du composant

   let annonces = [];
   async function get_annonce() {
      let response;
      try {
         response = await fetch("http://127.0.0.1:8000/recherche/", {
            method: "GET",
            headers: {
               "Content-Type": "application/json",
            },
         });
      } catch (error) {
         console.error("Error:", error);
      }

      if (!response.ok) {
         const message = `An error has occured: ${response.status}`;
         throw new Error(message);
      }
     annonces = await response.json();
     annonces = annonces.map(annonce => ({
         ...annonce,
         created_at: annonce.created_at.split('T')[0],
         updated_at: annonce.updated_at.split('T')[0]
      }));
     console.log(annonces);

   }

   // Your code here
   onMount(() => {
      get_annonce();

      // Sélectionner toutes les cartes avec la classe cardAnnonce
      const cards = document.querySelectorAll(".cardAnnonce");

      // Parcourir chaque carte
      cards.forEach((card) => {
         // Obtenir une couleur aléatoire pour la carte
         const cardColor = getRandomColor();

         // Sélectionner les éléments colorTopAnnonce et svgArrow de la carte actuelle
         const colorTopElement = card.querySelector(".colorTopAnnonce");
         // const svgArrow = card.querySelector('.svgArrow');

         // Appliquer la couleur aléatoire aux éléments colorTopAnnonce et svgArrow de la carte
         colorTopElement.style.backgroundColor = cardColor;
         // svgArrow.style.fill = cardColor;
      });
   });
</script>

<main>
   <header class="section text-white bg-white fp">
      <div class="cover-recherche position-absolute"></div>
      <div class="cover-img"></div>
      <div
         class="containerHeader container index text-center position-relative"
      >
         <h1 class="display-3 fw-semibold">
            Trouvez votre nouveau<br />facteur !
         </h1>
         <p class="pl-2 mb-6 py-6 fs-4 fw-normal">
            Recherchez des voyageurs qui accepteront de prendre votre colis en
            charge
         </p>
         <form>
            <!-- <div class="container containerBooking">
          <input
            type="text"
            class="form-control"
            placeholder="D'ou envoyez vous votre colis ?"
            required
          />
          <a href="/" class="dateRecherche bg-white">Date</a>
          <input
            type="text"
            class="form-control"
            placeholder="Où l'envoyez vous ?"
            required
          />
        </div> -->

            <!-- code mao albanie -->
            <div class="containerBooking">
               <div class="input-box">
                  <input
                     class="fw-semibold"
                     type="text"
                     placeholder="D'ou envoyez vous votre colis ?"
                     required
                  />
                  <div>
                     <a class="dateRecherche fw-bolder border-0" href="/"
                        >Date</a
                     >
                  </div>
                  <input
                     class="fw-semibold"
                     type="text"
                     placeholder="Où l'envoyez vous ?"
                     required
                  />
               </div>
            </div>
            <!-- ------------------- -->

            <button
               href="/"
               class="submit submitRecherche text-primary fw-bolder fs-4 border-0"
            >
               Rechercher
            </button>
            <div class=""></div>
         </form>
      </div>
   </header>
   <section class="about fp">
      <div class="">
         <h2 class="textAnnonceRecherche text-center fw-bold">Les annonces</h2>
      </div>
      <div class="album py-5">
         <div class="container containerAnnonces">
            <div
               class="row row-cols-1 row-cols-md-3 g-5 px-5"
               id="cardsContainer"
            >
            {#each annonces as annonce (annonce.id)}
            <div class="col">
              <a href="/details/{annonce.id}" class="card cardAnnonce h-100 redirection-div">
                <div class="card-body">
                  <div class="colorTopAnnonce mb-3"></div>
                  <div class="topCard">
                    <img src="../svg/photoProfile.svg" class="card-img-top" alt="..." />
                    <div class="nomDateTopCard">
                      <h5 class="card-title fw-bolder">
                        {annonce.createur_nom} {annonce.createur_prenom}
                      </h5>
                      <h5 class="card-title DateTopCard fw-semibold">
                        {annonce.createur_date_de_naissance}
                      </h5>
                    </div>
                  </div>
                  <div class="destinationTopCard fw-semibold fs-5">
                    <div class="departureTopCard">{annonce.lieu_depart}</div>
                    <svg class="svgArrow mt-2 mx-3" viewBox="246.554 219.198 189.9 12" width="189.9" height="12" xmlns="http://www.w3.org/2000/svg" xmlns:bx="https://boxy-svg.com">
                      <!-- svelte-ignore illegal-attribute-character -->
                      <path d="M 246.554 223.198 H 425.454 L 425.454 219.198 L 436.454 225.198 L 425.454 231.198 L 425.454 227.198 H 246.554 V 223.198 Z" style="fill-rule: nonzero;" transform="matrix(1.0000000000000002, 0, 0, 1.0000000000000002, 0, 0)" bx:shape="arrow 246.554 219.198 189.9 12 4 11 0 1@4082cbfb" />
                    </svg>
                    <div class="arrivalTopCard">{annonce.destination}</div>
                  </div>
                  <div class="dateCard pt-4 pb-2 fw-semibold">
                    Date : {annonce.created_at}
                  </div>
                </div>
                <div class="card-footer">
                  <small class="text-body-secondary">Last updated {annonce.updated_at} mins ago</small>
                </div>
              </a>
            </div>
          {/each}
          
            </div>
         </div>
      </div>
   </section>
</main>

<ColorGenerator />

<style>
   header {
      margin-top: 0;
      position: relative;
      height: 94vh;
   }

   .dateRecherche {
      color: #84bbff;
      border-radius: 10px;
      padding: 1.2 1.2;
      text-decoration: none;
      background-color: #fff;
      padding: 0.5rem 1rem;
   }

   .containerBooking {
      margin-top: 25px;
      min-width: 900px;
   }

   .containerBooking input {
      padding: 1.5rem;
      border-radius: 10px;
      border: none;
      background-color: #84bbff;
      color: white;
      appearance: none;
   }
   .containerBooking input::placeholder {
      color: white;
   }

   /* code mao albanie */

   .input-box {
      display: flex;
      width: 100%;
      gap: 90px;
      align-items: center;
   }

   .input-box input {
      width: 100%;
   }

   .input-box input::placeholder {
      text-align: center;
   }
   /* -------------------------- */

   .submitRecherche {
      background-color: #ffe767;
      text-decoration: none;
      padding: 1.25rem 2rem;
      border-radius: 10px;
      margin-top: 110px;
   }

   .about {
      padding: 20px;
      margin-top: 25px;
      background-color: #f5f5f5;
   }

   .textAnnonceRecherche {
      color: #4a4a4a;
      margin-top: 75px;
      margin-bottom: 50px;
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
