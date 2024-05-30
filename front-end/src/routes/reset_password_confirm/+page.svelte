<script>
        import { onMount } from 'svelte';
        import axios from 'axios';
        import { page } from '$app/stores';
    
        let new_password = '';
        let confirm_password = '';
        let message = '';
    
        let uidb64 = '';
        let token = '';
    
        $: {
            const query = $page.query;
            uidb64 = query.get('uidb64');
            token = query.get('token');
        }
    
        const resetPassword = async () => {
            try {
                const response = await axios.post(`/http://127.0.0.1:8000/reset_password_confirm/${uidb64}/${token}/`, {
                    new_password,
                    confirm_password
                });
                message = response.data.message;
            } catch (error) {
                message = error.response.data;
            }
        };
    </script>
    
    <main>
        <h1>Set New Password</h1>
        <input type="password" bind:value={new_password} placeholder="New Password" />
        <input type="password" bind:value={confirm_password} placeholder="Confirm Password" />
        <button on:click={resetPassword}>Reset Password</button>
        <p>{message}</p>
    </main>
    