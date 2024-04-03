<script>
</script>

<main>
  <nav class="navbar navbar-expand-lg bg-body-tertiary fontPrimary">
    <div class="container-fluid">
      <a class="navbar-brand" href="/">Envoyage</a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="/">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/recherche">Recherche</a>
          </li>
          <!-- <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="/" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  Dropdown
                </a>
                <ul class="dropdown-menu">
                  <li><a class="dropdown-item" href="/">Action</a></li>
                  <li><a class="dropdown-item" href="/">Another action</a></li>
                  <li><hr class="dropdown-divider"></li>
                  <li><a class="dropdown-item" href="/">Something else here</a></li>
                </ul>
              </li> -->
          <!-- <li class="nav-item">
                <a class="nav-link disabled" href="/" aria-disabled="true">Disabled</a>
              </li> -->
        </ul>
        <ul class="SignUp-LogIn d-flex m-0 p-0">
          <li>
            <a class="LogIn fw-semibold nav-link bg-primary" href="/creation">Créer une annonce +</a>
          </li>
          <li>
            <a class="LogIn fw-semibold nav-link" href="/profil">
              <img class="Profil-img-top-nav-bar" src="../svg/utilisateur.png" alt="profil-icon">
            </a>
          </li>
          <li>
            <a class="SignUp fw-semibold nav-link text-primary" href="/sign-up">Sign up</a>
          </li>
          <li>
            <a class="LogIn fw-semibold nav-link bg-primary" href="/log-in">Log in</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</main>

<style>
  .SignUp {
    background-color: #ffe767;
    border-radius: 5px;
    padding: 10px;
  }
  .LogIn {
    color: white;
    border-radius: 5px;
    padding: 10px;
  }
  .SignUp-LogIn {
    gap: 20px;
  }
  li {
    list-style: none;
  }
</style>
