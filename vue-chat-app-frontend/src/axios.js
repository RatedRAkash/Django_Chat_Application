//CUSTOM axios.js
import axios from 'axios';
import {toast, ToastPosition, ToastType} from 'bulma-toast'
import router from './router';

const axiosInstance = axios.create({
    // Your Axios configuration here
});

axiosInstance.interceptors.response.use(
    response => response,
    error => {
        // Handle 401 Unauthorized response here
        if (error.response && error.response.status === 401) {
            // router.push('/login'); // Assuming you use Vue Router
            // NotifyUser('You are not authenticated', 'error'); // Show a notification
            toast({
                message: 'Please Login',
                type: 'is-danger',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'top-center',
            })
            router.push('/login')
        }
        return Promise.reject(error);
    }
);

export default axiosInstance;
