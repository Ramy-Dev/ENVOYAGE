<script>
        import axios from 'axios';
        let email = '';
        let message = '';
    
        const resetPassword = async () => {
            try {
                const response = await axios.post('http://127.0.0.1:8000/reset_password/', { email });
                message = response.data.message;
            } catch (error) {
                message = error.response.data.detail || 'An error occurred';
            }
        };
    </script>
    
    <main>
        <h1>Reset Password</h1>
        <input type="email" bind:value={email} placeholder="Enter your email" />
        <button on:click={resetPassword}>Send Reset Link</button>
        <p>{message}</p>
    </main>
    