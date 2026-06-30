async function login() {

    const email = document.getElementById("email").value;
    const senha = document.getElementById("senha").value;

    const erroDiv = document.getElementById("erro");
    erroDiv.innerText = "";

    try {
        const response = await fetch("http://localhost:5001/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ email, senha })
        });

        const data = await response.json();
        
        if (response.ok) {
            Auth.setToken(data.token);
            window.location.href = "pages/menu.html";
        } else {
            erroDiv.innerText = data.erro || "Erro ao fazer login";
        }

    } catch (err) {
        erroDiv.innerText = "Erro de conexão com o servidor";
    }
}