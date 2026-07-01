const parametros = new URLSearchParams(
    window.location.search
)

const leitorId = parametros.get("id")

async function carregarLeitor() {

    const resposta = await fetch(
        `http://127.0.0.1:5002/leitores/${leitorId}`
    )

    const leitor = await resposta.json()

    document.getElementById(
        "nome"
    ).value = leitor.nome

    document.getElementById(
        "email"
    ).value = leitor.email

    document.getElementById(
        "telefone"
    ).value = leitor.telefone

}

carregarLeitor()

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
            `http://127.0.0.1:5002/leitores/${leitorId}`,
            {

                method: "PUT",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(leitor)

            }
        )

        if (resposta.ok) {

            alert(
                "Leitor atualizado com sucesso!"
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