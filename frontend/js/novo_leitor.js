const formulario = document.getElementById(
    "form-leitor"
)

formulario.addEventListener(
    "submit",
    async function(event) {

        event.preventDefault()

        const leitor = {

            nome: document.getElementById(
                "nome"
            ).value,

            email: document.getElementById(
                "email"
            ).value,

            telefone: document.getElementById(
                "telefone"
            ).value,

        }

        const resposta = await fetch(
            "http://127.0.0.1:5002/leitores",
            {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(leitor)

            }
        )

        if (resposta.ok) {

            alert(
                "Leitor cadastrado com sucesso!"
            )

            window.location.href =
                "visualizacao_leitores.html"

        }

        else {

            const erro = await resposta.json();

            alert(erro.erro);

        }

    }
)