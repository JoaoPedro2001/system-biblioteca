const Auth = {

    setToken: (token) => {
        localStorage.setItem("token", token);
    },

    getToken: () => {
        return localStorage.getItem("token");
    },

    logout: () => {
        localStorage.removeItem("token");
        window.location.href = "../index.html";
    },

    isAuthenticated: () => {
        return !!localStorage.getItem("token");
    }
};