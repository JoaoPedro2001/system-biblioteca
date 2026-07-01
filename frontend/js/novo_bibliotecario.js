const formulario = document.getElementById(
    "form-bibliotecario"
)

formulario.addEventListener(
    "submit",
    async function(event) {

        event.preventDefault()

        const senha = document.getElementById(
            "senha"
        ).value

        const confirmarSenha = document.getElementById(
            "confirmar-senha"
        ).value

        if (senha !== confirmarSenha) {
            alert(
                "Senha e confirmação de senha não coincidem."
            )

            return
        }

        const adminSelecionado =
            document.querySelector(
                'input[name="admin"]:checked'
            ).value

        const bibliotecario = {

            nome: document.getElementById(
                "nome"
            ).value,

            email: document.getElementById(
                "email"
            ).value,

            senha: senha,

            admin: adminSelecionado === "true"

        }

        const resposta = await fetch(
            "http://127.0.0.1:5001/bibliotecarios",
            {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(bibliotecario)

            }
        )

        if (resposta.ok) {

            alert(
                "Bibliotecário cadastrado com sucesso!"
            )

            window.location.href =
                "visualizacao_bibliotecarios.html"

        }

        else {

            const erro = await resposta.json();

            alert(erro.erro);

        }

    }
)