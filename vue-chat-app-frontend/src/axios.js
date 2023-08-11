//CUSTOM axios.js
import axios from 'axios';
import {toast, ToastPosition, ToastType} from 'bulma-toast'
import router from './router';
import store from './store'; // Import your Vuex store

const axiosInstance = axios.create({
    // Your Axios configuration here
    baseURL: 'http://localhost:7070',
    // headers: {
    //     common: {
    //         'Authorization': `Bearer ${store.state.token}`
    //     }
    // }
});

axiosInstance.interceptors.response.use(
    response => response,
    error => {
        // Handle 401 Unauthorized response here
        if (error.response && error.response.status === 401) {
            // router.push('/login'); // Assuming you use Vue Router
            // NotifyUser('You are not authenticated', 'error'); // Show a notification
            localStorage.removeItem('user-info');
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
