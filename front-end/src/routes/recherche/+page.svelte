<script>
   import { onMount } from "svelte";
   import ColorGenerator from "../../components/colorGenerator.svelte";
   import { getRandomColor } from "../../lib/functions/randomColor.js";
   import SearchForm from "../../components/Recherche/SearchForm.svelte";
   import AdCard from "../../components/AdCard.svelte";

   let ads = [
      { id: 1, name: 'John Doe', dob: '01/01/1990', from: 'Paris', to: 'Marseille', date: 'September 5th', updated: '3 mins ago' },
      { id: 2, name: 'Jane Smith', dob: '02/02/1995', from: 'Lyon', to: 'Toulouse', date: 'September 6th', updated: '5 mins ago' },
      { id: 3, name: 'David Johnson', dob: '03/03/1985', from: 'Algiers', to: 'Oran', date: 'September 7th', updated: '10 mins ago' },
      { id: 4, name: 'Emma Brown', dob: '04/04/1992', from: 'Nice', to: 'Bordeaux', date: 'September 8th', updated: '15 mins ago' },
      { id: 5, name: 'Michael Wilson', dob: '05/05/1988', from: 'Marseille', to: 'Paris', date: 'September 9th', updated: '20 mins ago' },
      { id: 6, name: 'Sophia Taylor', dob: '06/06/1993', from: 'Toulouse', to: 'Lyon', date: 'September 10th', updated: '25 mins ago' },
      { id: 7, name: 'Daniel Anderson', dob: '07/07/1987', from: 'Oran', to: 'Algiers', date: 'September 11th', updated: '30 mins ago' },
      { id: 8, name: 'Olivia Martinez', dob: '08/08/1998', from: 'Bordeaux', to: 'Nice', date: 'September 12th', updated: '35 mins ago' },
      { id: 9, name: 'William Thomas', dob: '09/09/1991', from: 'Paris', to: 'Marseille', date: 'September 13th', updated: '40 mins ago' },
      // Add more random data here
   ];
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

   onMount(() => {
      get_annonce();
      const cards = document.querySelectorAll(".cardAnnonce");
      cards.forEach((card) => {
         const cardColor = getRandomColor();
         const colorTopElement = card.querySelector(".colorTopAnnonce");
         colorTopElement.style.backgroundColor = cardColor;
      });
   });
</script>

<main>
   <div class="header">
      <div class="recherche_cover">
         <img class="image_bg_recherche" src="../svg/bg_recherche.svg">
         <div class="textIntro text-white fontSecondary">
            Explorez des milliers d'annonces en toute <span class="simpl-text">simplicité </span>
         </div>
         <div class="">
            <SearchForm />
         </div>
        
      </div>
      
   </div>
   <section class="section-annonces mt-5">
      <div class="textIntro text-secondary fontSecondary mb-5">
         annonce trouvées
      </div>
      <div class="ads-container">
         {#each ads as ad}
            <AdCard {ad} />
         {/each}
      </div>
   </section>
</main>

<!-- <ColorGenerator /> -->

<style>
   .header {
      margin-top: 0;
      position: relative;
      height: 50vh;
   }
   .recherche_cover {
      position: relative;
      width: 100%;
      height: 100%;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      padding: 100px;
      gap: 30px;
   }
   .image_bg_recherche {
      width: 100%;
      height: 100%;
      object-fit: cover;
      position: absolute;
      top: 0;
      left: 0;
      z-index: -1;
   }
   .textIntro {
      margin-top: 90px;
      font-size: 3rem;
      font-weight: 700;
      text-align: center;
   }

   .simpl-text {
    font-size: 3rem;
    font-weight: 700;
    color: #FFFFFF; /* White color for the main text */
    text-shadow: 
        -1px -7px 0 #4FE1F9, /* Shadow effect to the top-left */
        1px -1px 0 #40c5de,  /* Shadow effect to the top-right */
        -1px 1px 0 #40c5de,  /* Shadow effect to the bottom-left */
        1px 7px 0 #4FE1F9;   /* Shadow effect to the bottom-right */
   }
   .section-annonces {
      padding: 20px;
   }
   .ads-container {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
   }
</style>
