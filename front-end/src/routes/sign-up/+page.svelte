<script>
  let message = "";

  async function handleSubmit(event) {
    event.preventDefault(); // Prevent the default form submission

    // Get form data
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());

    try {
      const response = await fetch('http://127.0.0.1:8000/register/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',        },
        body: JSON.stringify(data)
      });

      if (response.ok) {
        const result = await response.json();
        message = "Registration successful!";
        console.log('Success:', result);
        // Handle success (e.g., show a success message, clear form, etc.)
      } else {
        const error = await response.json();
        message = "Registration failed!";
        console.error('Error:', error);
        // Handle errors (e.g., show error messages)
      }
    } catch (error) {
      message = "An error occurred!";
      console.error('Error:', error);
      // Handle errors (e.g., show error messages)
    }
  }

</script>

<main>
  <div class="bd">
    <b>{message}</b>
    <div id="sn" class="singup sn bg-primary m-auto">
      <div class="card-shadow">
        <div class="container">
          <div class="row">
            <div class="col p-0">
              <div class="d-flex flex-row">
                <button
                  class="sender-btn bg-primary border-0 text-white fs-4 fw-semibold py-3 w-50 m-0 is-selected"
                >
                  Sign up as Sender
                </button>
                <button
                  type="button"
                  class="travler-btn bg-white border-0 text-primary fs-4 fw-semibold py-3 w-50 m-0"
                  style="border: 1px solid #fff;"
                >
                  Traveler
                </button>
              </div>
            </div>
          </div>
        </div>

        <form id="registrationForm" class="box has-background-primary" on:submit={handleSubmit}>
          <div class="row">
            <div class="col-md-6">
              <div class="form-group">
                <label for="Sender-username">User Name :</label>
                <input
                  type="text"
                  class="snl form-control"
                  id="Sender-username"
                  required
                  name="username"
                />
              </div>
              <div class="form-group">
                <label for="Sender-nom">Nom :</label>
                <input
                  type="text"
                  class="snl form-control"
                  id="Sender-nom"
                  required
                  name="last_name"
                />
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-group">
                <label for="Sender-prenom">Prénom :</label>
                <input
                  type="text"
                  class="snl form-control"
                  id="Sender-prenom"
                  required
                  name="first_name"
                />
              </div>
            </div>
          </div>
          <div class="form-group">
            <label for="Sender-email">Email :</label>
            <input
              type="email"
              class="snl form-control"
              id="Sender-email"
              required
              name="email"
            />
          </div>
          <div class="row">
            <div class="col-md-6">
              <div class="form-group">
                <label for="Sender-password">Mot de passe :</label>
                <input
                  type="password"
                  class="snl form-control"
                  id="Sender-password"
                  required
                  name="password"
                />
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-group">
                <label for="Sender-ConfirmPassword">Confirmer le mot de passe :</label>
                <input
                  type="password"
                  class="snl form-control"
                  id="Sender-ConfirmPassword"
                  required
                  name="password2"
                />
              </div>
            </div>
          </div>
          <div class="d-flex justify-content-center">
            <button
              type="submit"
              id="submitSignupSender"
              class="submitSignupSender border-0 bg-white text-primary fw-bolder mt-5"
            >
              Sign up
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</main>

<style>
  .sn {
    margin-top: 160px !important;
    border-radius: 20px;
    align-items: center;
  }
  form {
    padding: 20px;
  }
  label {
    font-weight: 650;
    margin-top: 20px;
  }
  .sn label {
    color: white;
  }
  .sn input {
    background-color: white;
  }
  .sender-btn {
    border-top-left-radius: 20px;
  }
  .travler-btn {
    border-top-right-radius: 20px;
  }
  .submitSignupSender {
    border-radius: 20px;
    padding: 7px 50px;
  }
</style>