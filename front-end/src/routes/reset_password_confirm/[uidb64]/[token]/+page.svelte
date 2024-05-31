<script>
    import axios from 'axios';
    import { onMount } from 'svelte';
    import { page } from '$app/stores';

// Get the query parameters from the $page store
const { uidb64, token } = $page.params;

// Display the query parameters
console.log('uidb64:', uidb64);
console.log('token:', token);
  
    let new_password = '';
    let confirm_password = '';
    let message = '';
  
    const resetPassword = async () => {
      if (new_password !== confirm_password) {
        message = 'Passwords do not match';
        return;
      }
  
      try {
        const response = await axios.post(`http://127.0.0.1:8000/reset_password_confirm/${uidb64}/${token}/`, {
          new_password,
          confirm_password
        });
        message = response.data.message;
      } catch (error) {
        message = error.response?.data || 'An error occurred';
      }
    };
  
    onMount(() => {
      console.log('UIDB64:', uidb64);
      console.log('Token:', token);
    });
  </script>
  
  <main>
    <h1>Set New Password</h1>
    <input type="password" bind:value={new_password} placeholder="New Password" />
    <input type="password" bind:value={confirm_password} placeholder="Confirm Password" />
    <button on:click={resetPassword}>Reset Password</button>
    <p>{message}</p>
  </main>
  
  <style>
    main {
      padding: 20px;
    }
    h1 {
      font-size: 24px;
      margin-bottom: 20px;
    }
    input {
      display: block;
      margin-bottom: 10px;
      padding: 10px;
      width: 100%;
      max-width: 300px;
    }
    button {
      padding: 10px 20px;
      background-color: #007bff;
      color: white;
      border: none;
      cursor: pointer;
    }
    p {
      margin-top: 20px;
      font-size: 16px;
    }
  </style>
  