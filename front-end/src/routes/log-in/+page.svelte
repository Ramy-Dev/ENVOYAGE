<script>
   import { redirect } from "@sveltejs/kit";

// In the login script
let message = "";

async function handleSubmit(event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());

    try {
        const response = await fetch("http://127.0.0.1:8000/login/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        });

        if (response.ok) {
            const result = await response.json();
            message = "Login successful!";
            localStorage.setItem("authToken", result.token);
            console.log("Success:", result);
            // Fetch and store user info
            fetchUserInfo(result.token);
            // Redirect to the home page  
            window.location.href = '/'
            } else {
            const error = await response.json();
            message = "Login failed!";
            console.error("Error:", error);
        }
    } catch (error) {
        message = "An error occurred!";
        console.error("Error:", error);
    }
}







async function fetchUserInfo(token) {
    try {
        const response = await fetch("http://127.0.0.1:8000/utilisateurs/", {
            headers: {
                "Authorization": `Token ${token}` 
            }
        });

        if (response.ok) {
            const user = await response.json();
            localStorage.setItem("user", JSON.stringify(user));
        } else {
            console.error("Failed to fetch user info.");
        }
    } catch (error) {
        console.error("Error fetching user info:", error);
    }
}

function getToken() {
    return localStorage.getItem("authToken");
}

function getUser() {
    return JSON.parse(localStorage.getItem("user"));
}

function logout() {
    localStorage.removeItem("authToken");
    localStorage.removeItem("user");
}
async function fetchUserByUsername(username) {
   try {
      const response = await fetch(`http://127.0.0.1:8000/users/?username=${username}`, {
         headers: {
            "Authorization": `Token ${getToken()}`
         }
      });
      if (response.ok) {
         const user = await response.json();
         return user;
      } else {
         console.error("Failed to fetch user by username.");
         return null;
      }
   } catch (error) {
      console.error("Error fetching user by username:", error);
      return null;
   }
}

</script>

<main>
  <b>{message}</b>
  <div class="container bd fontPrimary">
     <div class="login card-shadow mx-auto">
        <div class="box p-0">
           <button
              id=""
              class="login-btn sender btn-block bg-primary text-white fw-bolder fs-5 border-0 w-100 py-3 mb-0"
              >Log in</button
           >
        </div>
        <div class="container container-form">
           <form class="box" on:submit={handleSubmit}>
              <div class="form-group">
                 <label for="username">User name :</label>
                 <input
                    type="text"
                    class="snl form-control"
                    name="username"
                    id="username"
                    required
                 />
              </div>
              <div class="form-group">
                 <label for="password">Mot de passe :</label>
                 <input
                    type="password"
                    class="snl form-control"
                    name="password"
                    id="password"
                    required
                 />
              </div>
              <div class="text-center mt-4">
                 <button
                    type="submit"
                    class="submitLogin border-0 bg-primary text-white fw-bolder mt-3"
                    >Log in</button>
              </div>
           </form>
        </div>
     </div>
  </div>
</main>

<style>
  .login {
     background-color: #fff;
  }
  .login label {
     color: black;
     font-weight: 650;
     margin-top: 20px;
  }
  .snl {
     background-color: #f0f0f0;
  }
  .container-form {
     padding: 25px;
  }
  .login-btn {
     border-top-left-radius: 20px;
     border-top-right-radius: 20px;
  }
  .submitLogin {
     border-radius: 20px;
     padding: 7px 50px;
  }
</style>
