const API = {

    request: async (url, options = {}) => {

        const token = Auth.getToken();

        const headers = {
            "Content-Type": "application/json",
            ...(options.headers || {})
        };

        if (token) {
            headers["Authorization"] = "Bearer " + token;
        }

        const response = await fetch(url, {
            ...options,
            headers
        });

        if (response.status === 401) {
            Auth.logout();
        }

        return response;
    }
};