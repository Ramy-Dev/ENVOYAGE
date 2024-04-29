<script>
import { onMount } from 'svelte';

let isDragging = false, isAutoPlay = false, startX, startScrollLeft, timeoutId;

let AOS;
onMount(async () => {
    if (typeof window !== 'undefined') {
      const module = await import('aos');
      AOS = module.default;
      AOS.init({
        duration: 1000,
      });
    }
  });
onMount(() => {
  const wrapper = document.querySelector(".wrapper");
  const carousel = document.querySelector(".carousel");
  const firstCardWidth = carousel.querySelector(".card").offsetWidth;
  const arrowBtns = document.querySelectorAll(".wrapper i");
  const carouselChildrens = [...carousel.children];

  // Get the number of cards that can fit in the carousel at once
  let cardPerView = Math.round(carousel.offsetWidth / firstCardWidth);

  // Insert copies of the last few cards to beginning of carousel for infinite scrolling
  carouselChildrens.slice(-cardPerView).reverse().forEach(card => {
    carousel.insertAdjacentHTML("afterbegin", card.outerHTML);
  });

  // Insert copies of the first few cards to end of carousel for infinite scrolling
  carouselChildrens.slice(0, cardPerView).forEach(card => {
    carousel.insertAdjacentHTML("beforeend", card.outerHTML);
  });

  // Scroll the carousel at appropriate postition to hide first few duplicate cards on Firefox
  carousel.classList.add("no-transition");
  carousel.scrollLeft = carousel.offsetWidth;
  carousel.classList.remove("no-transition");

  // Add event listeners for the arrow buttons to scroll the carousel left and right
  arrowBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      carousel.scrollLeft += btn.id == "left" ? -firstCardWidth : firstCardWidth;
    });
  });

  const dragStart = (e) => {
    isDragging = true;
    carousel.classList.add("dragging");
    // Records the initial cursor and scroll position of the carousel
    startX = e.pageX;
    startScrollLeft = carousel.scrollLeft;
  }

  const dragging = (e) => {
    if(!isDragging) return; // if isDragging is false return from here
    // Updates the scroll position of the carousel based on the cursor movement
    carousel.scrollLeft = startScrollLeft - (e.pageX - startX);
  }

  const dragStop = () => {
    isDragging = false;
    carousel.classList.remove("dragging");
  }

  const infiniteScroll = () => {
    // If the carousel is at the beginning, scroll to the end
    if(carousel.scrollLeft === 0) {
      carousel.classList.add("no-transition");
      carousel.scrollLeft = carousel.scrollWidth - (2 * carousel.offsetWidth);
      carousel.classList.remove("no-transition");
    }
    // If the carousel is at the end, scroll to the beginning
    else if(Math.ceil(carousel.scrollLeft) === carousel.scrollWidth - carousel.offsetWidth) {
      carousel.classList.add("no-transition");
      carousel.scrollLeft = carousel.offsetWidth;
      carousel.classList.remove("no-transition");
    }
    // Clear existing timeout & start autoplay if mouse is not hovering over carousel
    clearTimeout(timeoutId);
    if(!wrapper.matches(":hover")) autoPlay();
  }

  const autoPlay = () => {
    if(window.innerWidth < 800 || !isAutoPlay) return; // Return if window is smaller than 800 or isAutoPlay is false
    // Autoplay the carousel after every 2500 ms
    timeoutId = setTimeout(() => carousel.scrollLeft += firstCardWidth, 2500);
  }

  autoPlay();
  carousel.addEventListener("mousedown", dragStart);
  carousel.addEventListener("mousemove", dragging);
  document.addEventListener("mouseup", dragStop);
  carousel.addEventListener("scroll", infiniteScroll);
  wrapper.addEventListener("mouseenter", () => clearTimeout(timeoutId));
  wrapper.addEventListener("mouseleave", autoPlay);
  
  document.addEventListener('DOMContentLoaded', function() {
  var observer = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('slide-fade-in');
      } else {
        entry.target.classList.remove('slide-fade-in');
      }
    });
  });

  observer.observe(document.querySelector('.containerSectionTop'));
});
});
</script>

<main>
  <header class="landingPage">
    
    <div class="headerContent">
      <div class="bgImage">
        <img src="../svg/hexaMotif.svg" alt="bgImage" />
      </div>
      <div class="headerText">
        <div class="brandName text-primary fontSecondary">Envoyage</div>
        <div class="brandSlogan text-darkPrimary fs-2 fontSecondary">
          gagnez de l’argent tout en voyageant
        </div>
        <div class="headerButtons"></div>
      </div>
      <div class="logo">
        <img src="../svg/logo_envoyage.svg" alt="logo" />
      </div>
      <div class="w-50"></div>
      <div class="gridBrandImage">
        <img class="brandImage" src="../svg/plane_sky.svg" alt="photo_brand">
      </div>
    </div>
  </header>
  <section>
    <div class="about">
      <div class="aboutTitle text-primary fs-1 fw-bold fontSecondary">
        Envoyage ?
      </div>
      <div class="aboutSectionsContainer">
        <div class="containerSectionTop"> 
        <div class="aboutSection aboutSectionType1" data-aos="fade-up">
          <div
            class="aboutSectionTitle text-secondary fs-2 fw-bold fontSecondary"
          >
            Qu'est ce qu'Envoyage ?
          </div>
          <div class="aboutSectionText fs-5 text-basic fontPrimary">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. A, dolorum
            optio? Voluptatibus nesciunt vitae tempore voluptate fuga, vel quo
            animi pariatur? Accusantium sapiente tempora fugit corporis,
            laboriosam laudantium? Similique, ratione.
          </div>
        </div>
        <div class="" data-aos="fade-down-left" data-aos-duration="2000" data-aos-delay="200">
          <img class="planeImage" src="../svg/plane.svg" alt="plane">
        </div>
      </div>
        <div class="containerSectionMiddle">
          <div class="aboutSectionHexagonLeft" data-aos="fade-right" data-aos-duration="2000" data-aos-delay="500">
            <img class="aboutBorderHexaLeft" src="../svg/half_hexa_rightpart.svg" alt="half_hexa_rightpart" />
          </div>
          <div class="aboutSection aboutSectionType2" data-aos="fade-up">
            <div
              class="aboutSectionTitle text-secondary fs-2 fw-bold fontSecondary"
            >
              Quel est notre but ?
            </div>
            <div class="aboutSectionText fs-5 text-basic fontPrimary">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. A,
              dolorum optio? Voluptatibus nesciunt vitae tempore voluptate fuga,
              vel quo animi pariatur? Accusantium sapiente tempora fugit
              corporis, laboriosam laudantium? Similique, ratione.
            </div>
          </div>
        </div>
        <div class="containerSectionBottom">
        
        <div class="aboutSection aboutSectionType1 " data-aos="fade-up">
          <div
            class="aboutSectionTitle text-secondary fs-2 fw-bold fontSecondary"
          >
            Pourquoi Envoyage ?
          </div>
          <div class="aboutSectionText fs-5 text-basic fontPrimary">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. A, dolorum
            optio? Voluptatibus nesciunt vitae tempore voluptate fuga, vel quo
            animi pariatur? Accusantium sapiente tempora fugit corporis,
            laboriosam laudantium? Similique, ratione.
          </div>
        </div>
        <div class="aboutSectionHexagonRight" data-aos="fade-left" data-aos-duration="2000" data-aos-delay="500">
          <img class="aboutBorderHexaRight" src="../svg/half_hexa_rightpart.svg" alt="half_hexa_leftpart" />
        </div>
      </div>
      </div>
    </div>
    
    <div class="steps" >
      <div class="arrow arrowAboutSteps" data-aos="fade-down">
        <img class="arrowSVG" src="../svg/arrow.svg" alt="arrow">
      </div>
      <div class="step01 step">
        <div class="stepTop">
          <div class="stepContent">
            <div class="stepTitle text-basic fw-bold fs-2 fontSecondary">
              <div class="stepNumber fontSecondary" data-aos="fade-up-right" data-aos-delay="100">01'</div>
              <div class="text fw-bold" data-aos="fade-up" data-aos-delay="750">
                Trouvez votre
                <div class="highlight bg-primary text-white" data-aos="flip-up" data-aos-delay="1500">
                expéditeur
              </div>
              </div>
            </div>
            <div class="stepText fs-5 fontPrimary" data-aos="fade-up" data-aos-delay="550">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Odio,
              culpa eius div dolorem iusto consectetur dolore eum voluptates
              aliquid voluptatem cum amet quaerat commodi et libero esse
              excepturi laudantium nesciunt.
            </div>
          </div>
          <div data-aos="fade-left" data-aos-delay="550">
            <img
              class="stepImage"
              src="../svg/deliveryHome.svg"
              alt="delivery"
            />
          </div>
        </div>
        <div class="stepAds">
          <div class="steptitle text-secondary fw-bold fs-2 fontSecondary" data-aos="fade-up" data-aos-delay="600">
            Quelques annonces
          </div>
        </div>
      </div>
      <div class="wrapper" data-aos="fade" data-aos-delay="650">
        <i id="left" class="fa-solid fa-angle-left text-darkSecondary">&lt</i>
        <div class="carousel">
          <div class="col">
            <div href="" class="card  h-100 redirection-div">
              <div class="card-body">
                <div class="colorTopAnnonce mb-3"></div>
                <div class="topCard">
                  <img
                    src="../svg/photoProfile.svg"
                    class="card-img-top"
                    alt="..."
                  />
                  <div class="nomDateTopCard">
                    <h5 class="card-title fw-bold">Amine Izem</h5>
                    <h5 class="card-title DateTopCard fw-semibold">
                      24/06/2005
                    </h5>
                  </div>
                </div>
                <div class="destinationTopCard fw-semibold fs-5 fontSecondary">
                  <div class="departureTopCard fw-bold">Alger</div>
                  <svg
                    class="svgArrow mt-2 mx-3"
                    viewBox="246.554 219.198 189.9 12"
                    width="189.9"
                    height="12"
                    xmlns="http://www.w3.org/2000/svg"
                    xmlns:bx="https://boxy-svg.com"
                  >
                    <!-- svelte-ignore illegal-attribute-character -->
                    <path
                      d="M 246.554 223.198 H 425.454 L 425.454 219.198 L 436.454 225.198 L 425.454 231.198 L 425.454 227.198 H 246.554 V 223.198 Z"
                      style="fill-rule: nonzero; fill: #21A5C3;"
                      transform="matrix(1.0000000000000002, 0, 0, 1.0000000000000002, 0, 0)"
                      bx:shape="arrow 246.554 219.198 189.9 12 4 11 0 1@4082cbfb"
                    />
                  </svg>
                  <div class="arrivalTopCard fw-bold">Paris</div>
                </div>
                <div class="dateCard pt-4 pb-2 text-darkSecondary fw-semibold">
                  Date : 30/03/2024
                </div>
              </div>
              <div class="card-footer border-0">
                <div class="text-body-secondary px-3 pb-3 text-midSecondary"
                  >last updated 3 mins ago</div
                >
              </div>
            </div>
          </div>
          <div class="col">
            <div href="" class="card  h-100 redirection-div">
              <div class="card-body">
                <div class="colorTopAnnonce mb-3"></div>
                <div class="topCard">
                  <img
                    src="../svg/photoProfile.svg"
                    class="card-img-top"
                    alt="..."
                  />
                  <div class="nomDateTopCard">
                    <h5 class="card-title fw-bold">Nassim Izem</h5>
                    <h5 class="card-title DateTopCard fw-semibold">
                      24/06/2005
                    </h5>
                  </div>
                </div>
                <div class="destinationTopCard fw-semibold fs-5 fontSecondary">
                  <div class="departureTopCard fw-bold">Alger</div>
                  <svg
                    class="svgArrow mt-2 mx-3"
                    viewBox="246.554 219.198 189.9 12"
                    width="189.9"
                    height="12"
                    xmlns="http://www.w3.org/2000/svg"
                    xmlns:bx="https://boxy-svg.com"
                  >
                    <!-- svelte-ignore illegal-attribute-character -->
                    <path
                      d="M 246.554 223.198 H 425.454 L 425.454 219.198 L 436.454 225.198 L 425.454 231.198 L 425.454 227.198 H 246.554 V 223.198 Z"
                      style="fill-rule: nonzero; fill: #21A5C3;"
                      transform="matrix(1.0000000000000002, 0, 0, 1.0000000000000002, 0, 0)"
                      bx:shape="arrow 246.554 219.198 189.9 12 4 11 0 1@4082cbfb"
                    />
                  </svg>
                  <div class="arrivalTopCard fw-bold">Paris</div>
                </div>
                <div class="dateCard pt-4 pb-2 text-darkSecondary fw-semibold">
                  Date : 30/03/2024
                </div>
              </div>
              <div class="card-footer border-0">
                <div class="text-body-secondary px-3 pb-3 text-midSecondary"
                  >last updated 3 mins ago</div
                >
              </div>
            </div>
          </div>
          <div class="col">
            <div href="" class="card  h-100 redirection-div">
              <div class="card-body">
                <div class="colorTopAnnonce mb-3"></div>
                <div class="topCard">
                  <img
                    src="../svg/photoProfile.svg"
                    class="card-img-top"
                    alt="..."
                  />
                  <div class="nomDateTopCard">
                    <h5 class="card-title fw-bold">Islem Izem</h5>
                    <h5 class="card-title DateTopCard fw-semibold">
                      24/06/2005
                    </h5>
                  </div>
                </div>
                <div class="destinationTopCard fw-semibold fs-5 fontSecondary">
                  <div class="departureTopCard fw-bold">Alger</div>
                  <svg
                    class="svgArrow mt-2 mx-3"
                    viewBox="246.554 219.198 189.9 12"
                    width="189.9"
                    height="12"
                    xmlns="http://www.w3.org/2000/svg"
                    xmlns:bx="https://boxy-svg.com"
                  >
                    <!-- svelte-ignore illegal-attribute-character -->
                    <path
                      d="M 246.554 223.198 H 425.454 L 425.454 219.198 L 436.454 225.198 L 425.454 231.198 L 425.454 227.198 H 246.554 V 223.198 Z"
                      style="fill-rule: nonzero; fill: #21A5C3;"
                      transform="matrix(1.0000000000000002, 0, 0, 1.0000000000000002, 0, 0)"
                      bx:shape="arrow 246.554 219.198 189.9 12 4 11 0 1@4082cbfb"
                    />
                  </svg>
                  <div class="arrivalTopCard fw-bold">Paris</div>
                </div>
                <div class="dateCard pt-4 pb-2 text-darkSecondary fw-semibold">
                  Date : 30/03/2024
                </div>
              </div>
              <div class="card-footer border-0">
                <div class="text-body-secondary px-3 pb-3 text-midSecondary"
                  >last updated 3 mins ago</div
                >
              </div>
            </div>
          </div>
          <div class="col">
            <div href="" class="card  h-100 redirection-div">
              <div class="card-body">
                <div class="colorTopAnnonce mb-3"></div>
                <div class="topCard">
                  <img
                    src="../svg/photoProfile.svg"
                    class="card-img-top"
                    alt="..."
                  />
                  <div class="nomDateTopCard">
                    <h5 class="card-title fw-bold">Wassim Izem</h5>
                    <h5 class="card-title DateTopCard fw-semibold">
                      24/06/2005
                    </h5>
                  </div>
                </div>
                <div class="destinationTopCard fw-semibold fs-5 fontSecondary">
                  <div class="departureTopCard fw-bold">Alger</div>
                  <svg
                    class="svgArrow mt-2 mx-3"
                    viewBox="246.554 219.198 189.9 12"
                    width="189.9"
                    height="12"
                    xmlns="http://www.w3.org/2000/svg"
                    xmlns:bx="https://boxy-svg.com"
                  >
                    <!-- svelte-ignore illegal-attribute-character -->
                    <path
                      d="M 246.554 223.198 H 425.454 L 425.454 219.198 L 436.454 225.198 L 425.454 231.198 L 425.454 227.198 H 246.554 V 223.198 Z"
                      style="fill-rule: nonzero; fill: #21A5C3;"
                      transform="matrix(1.0000000000000002, 0, 0, 1.0000000000000002, 0, 0)"
                      bx:shape="arrow 246.554 219.198 189.9 12 4 11 0 1@4082cbfb"
                    />
                  </svg>
                  <div class="arrivalTopCard fw-bold">Paris</div>
                </div>
                <div class="dateCard pt-4 pb-2 text-darkSecondary fw-semibold">
                  Date : 30/03/2024
                </div>
              </div>
              <div class="card-footer border-0">
                <div class="text-body-secondary px-3 pb-3 text-midSecondary"
                  >last updated 3 mins ago</div
                >
              </div>
            </div>
          </div>
        </div>
        <i id="right" class="fa-solid fa-angle-right text-darkSecondary">&gt</i>
      </div>
      <div class="step01 step">
        <div class="stepAds">
          <div class="stepText fs-5 fontPrimary" data-aos="fade-up" data-aos-delay="550">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Fugit
            officia, quaerat commodi culpa id fugiat div laudantium tenetur
            doloremque repellat itaque nemo tempora numquam velit impedit minus
            similique doloribus voluptas.
          </div>
          <div class="" data-aos="flip-up" data-aos-delay="700">
            <button
              class="stepButton bg-primary text-white highlight fs-5 fontSecondary"
            >
              Rechercher
            </button>
          </div>
        </div>
      </div>
      <div class="transition">
        <img class="transition" src="../svg/transition1.png" alt="transition" />
      </div>
    </div>
  </section>
</main>

<style>
  @import '../front-end/static/animation.css';
  main {
    overflow-x: hidden;
  }
  .landingPage {
    display: flex;
    flex-direction: column;
    justify-content: center;

    height: 100vh;
    width: 100%;
    position: relative;
  }
.bgImage {
  position: absolute;
    left: -10%;
    width: 100%;
    opacity: 15%;
    z-index: -1;
}

.bgImage::after {
  content: "";
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(to top, rgba(255,255,255,1) 5%, rgba(255,255,255,0) 50%,rgba(255,255,255,0) 100%);
  pointer-events: none;
}
  .headerContent {
    position: relative;
    display: grid;
    align-items: center;
    grid-template-columns: 1.5fr 0.5fr 1fr;
    margin: 0 auto;
    margin-right: 0;
    margin-left: 50px;
  }
  .headerText {
    width: 90%;
    margin: 0 auto;
  }
  .brandName {
    font-size: 7rem;
    font-weight: 700;
  }
  .logo {
    z-index: 1;
    position: absolute;
    top: 50%;
  left: 60%;
    transform: translate(-50%, -50%);
  }
  .brandImage {
    height: 100vh;
  }
  .gridBrandImage {
    position: relative;
  }
  .brandSlogan {
    margin-left: 5px ;
    font-size: 2rem;
    font-weight: 700;
  }
  .about {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 50px 0 150px 0;
    width: 90%;
    margin: 0 auto;
    gap: 70px;
  }
  .aboutSectionsContainer {
    display: flex;
    flex-direction: column;
    gap: 400px;
  }
  .aboutSection {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  .aboutSectionType1 {
    width: 70%;
  }
  .aboutSectionType2 {
    margin-left: 30%;
  }
  .containerSectionTop {
    height: 50vh;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .planeImage {
    position: absolute;
    top: 0;
    right: 0;
  }
  .containerSectionMiddle {
    height: 30vh;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 50px;
  }
  .containerSectionBottom {
    height: 70vh;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 50px;
    
  }
  .aboutSectionHexagonLeft {
    position: absolute;
    left: 0;
  }
  .aboutBorderHexaLeft {

  }
  .aboutSectionHexagonRight {
    position: absolute;
    right: 0;
  }
  .aboutBorderHexaRight {
    
    transform: scaleX(-1);
  }


  .arrow {
    position: absolute;
    align-items: center;
    margin: 0 auto;
    width: 100%;
    top: -4%;
    left: 55%;
    z-index: 2;
  }
  .arrowSVG{
    width: 150px;
    transform: rotate(10deg);
  }
  /* steps */

  .steps {
    position: relative;
    background-color: #efefef;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 150px 0 100px 0;
    width: 100%;
    margin: 0 auto;
    gap: 70px;
    z-index: 1;
  }

  .step {
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 90%;
    gap: 200px;
  }
  .stepTop {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 90%;
  }
  .stepContent {
    display: flex;
    flex-direction: column;
    gap: 100px;
  }
  .stepTitle {
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .stepTitle .text {
    margin-left: 50px;
    display: flex;
    gap: 5px;
  }
  .stepText {
    margin-left: 50px;
    width: 75%;
  }
  .stepNumber {
    position: absolute;
    font-size: 10rem;
    font-weight: 700;
    opacity: 30%;
  }
  .stepImage {
    width: 350px;
  }
  .stepAds {
    display: flex;
    flex-direction: column;
    gap: 30px;
    margin-left: 50px;
  }
  .stepAds .stepText {
    margin-left: 0;
  }
  .stepAds .stepButton {
    border: 0;
    appearance: none;
    padding: 15px 100px;
  }
  .transition {
    width: 100%;
  }
  .scrollAds {
    width: 100vw;
    overflow-x: auto;
    display: flex;
    gap: 20px;
    margin-left: 0;
  }
  .containerAnnonces {
    display: flex;
    flex-wrap: nowrap;
    overflow-x: scroll;
    gap: 20px;
    margin-left: 80px;
    scroll-behavior: smooth; /* Effet de défilement en douceur */
    user-select: none; /* Empêcher la sélection du texte lors du défilement */
    width: max-content; /* Ajuster la largeur du conteneur pour permettre le défilement infini */
    white-space: nowrap; /* Empêcher le saut à la ligne des cartes */
    padding-bottom: 20px; /* Ajouter un peu d'espace en bas pour éviter le saut abrupt */
    cursor: grab; /* Curseur de défilement au survol */
    cursor: -webkit-grab; /* Pour la compatibilité avec les navigateurs basés sur WebKit */
  }

  .card {
    border: none;
    border-radius: 20px;
    min-width: 500px; /* Ajuster la largeur de vos cartes */
    pointer-events: auto;
  }
  .containerAnnonces .active {
    cursor: grabbing;
  }
  .colorTopAnnonce {
  border-radius: 40px;
  height: 40px;
  width: 90%;
  margin: 0 auto;
}
  .topCard {
    display: flex;
    flex-direction: row;
    padding: 0 50px 30px 50px;
    align-items: center;
    justify-content: space-between;
  }
  .card-footer {
    width: 100%;
    border-radius: 0 0 40px 40px;
    background-color: #D9D9D9;
  }

















  .wrapper {
  width: 100%;
  position: relative;
}
.wrapper i {
  top: 50%;
  height: 50px;
  width: 50px;
  cursor: pointer;
  font-size: 1.25rem;
  position: absolute;
  text-align: center;
  line-height: 50px;
  background: #fff;
  border-radius: 50%;
  box-shadow: 0 3px 6px rgba(0,0,0,0.23);
  transform: translateY(-50%);
  transition: transform 0.1s linear;
}
.wrapper i:active{
  transform: translateY(-50%) scale(0.85);
}
.wrapper i:first-child{
  left: 23px;
    z-index: 20;
}
.wrapper i:last-child{
  right: 23px;
  z-index: 20;
}
.wrapper .carousel{
  display: grid;
  grid-auto-flow: column;
  /* grid-auto-columns: calc((100% / 4) - 12px); */
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  gap: 80px;
  border-radius: 8px;
  margin-left: -18%;
  scroll-behavior: smooth;
  scrollbar-width: none;
}
.carousel::-webkit-scrollbar {
  display: none;
}
.carousel.no-transition {
  scroll-behavior: auto;
}
.carousel.dragging {
  scroll-snap-type: none;
  scroll-behavior: auto;
}
.carousel.dragging .card {
  cursor: grab;
  user-select: none;
}
.carousel :where(.card, .img) {
  display: flex;
  justify-content: center;
  align-items: center;
}
.carousel .card {
  scroll-snap-align: start;
  height: 342px;
  box-shadow: 1px 1px 5px rgba(0, 0, 0, 0.29);;
  list-style: none;
  background: #fff;
  cursor: pointer;
  flex-direction: column;
  border-radius: 40px;
}

@media screen and (max-width: 900px) {
  .wrapper .carousel {
    grid-auto-columns: calc((100% / 2) - 9px);
  }
}
@media screen and (max-width: 600px) {
  .wrapper .carousel {
    grid-auto-columns: 100%;
  }
}

</style>
