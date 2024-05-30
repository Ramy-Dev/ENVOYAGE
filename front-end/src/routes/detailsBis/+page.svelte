<script>
</script>

<main class="fontSecondary">
  <img class="image_bg_recherche_ads" src="../svg/bg-recherche-ads.svg" />
  <div class="containerAnnonce">
    <div class="textAnnonce">L'annonce</div>
    <div class="annonce">
      <!--  Top Annonce -->

      <div class="topAnnonce">
        <div class="imageProfile">
          <img src="../svg/image_profil.svg" alt="Photo de profile" />
        </div>
        <div class="trajet"></div>
      </div>

      <!--  Mid Annonce -->

      <div class="midAnnonce">
        <div class="elementAnnonce"></div>
        <div class="elementAnnonce"></div>
        <div class="elementAnnonce"></div>
        <div class="elementAnnonce"></div>
      </div>
    </div>

    <!--  Main Annonce -->

    <div class="mainAnnonce">
      <div class="leftMain">
        <div class="inputPoids"></div>
        <div class="tarif"></div>
      </div>
      <div class="rightMain">
        <div class="conditions"></div>
      </div>
    </div>

    <!--  Bottom Annonce -->

    <div class="bottomAnnonce">
      <div class="prixFinal"></div>
      <div class="reserveButton"></div>
    </div>
  </div>
</main>

<style>
  main {
    position: relative;
    height: 200vh;
  }

  .image_bg_recherche_ads {
    width: 120%;
    height: 100%;
    object-fit: cover;
    position: absolute;
    top: -10%;
    left: -10%;
    z-index: -2;
    transition: transform 0.5s ease;
  }
  .containerAnnonce{

    margin: 100px;
  }
  .textAnnonce {
    font-size: 2.5rem;
    text-align: center;
  }
  .annonce {
    width: 80%;
    margin: auto;
    display: flex;
    flex-direction: column;
    padding: 60px 150px;
    border-radius: 40px;
    background-color: #ffffff;
    gap: 50px;
  }

</style>
