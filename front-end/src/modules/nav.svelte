<!-- svelte-ignore a11y-no-redundant-roles -->
<nav class="navbar is-fixed-top" role="navigation" aria-label="main navigation">
        <div class="navbar-brand">
            <a class="navbar-item" href="/">
                <div class="is-size-3 ml-2">OUANIS</div>
            </a>
<!-- IL Y'AVAIT UN PROBLEME ICI -->
            <!-- svelte-ignore a11y-missing-attribute -->
            <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false"
                data-target="navbarBasicExample">
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
            </a>
        </div>


        <div id="navbarBasicExample" class="navbar-menu">
            <div class="ml-auto navbar-start">
                <a href="/" class="navbar-item">
                    Home
                </a>

                <a href="/" class="navbar-item">
                    About
                </a>
                <a href="/recherche" class="navbar-item">
                    Announces
                </a>
                <a href="/" class="navbar-item">
                    Contact
                </a>


            </div>

            
            <div class="navbar-end ml-0">
                <div class="navbar-item">
                    <div class="buttons">
                        <a href="/sign-up" class="button bbtn">
                            <strong>Sign up</strong>
                        </a>
                        <a href="/log-in" class="button is-light">
                            Log in
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </nav>