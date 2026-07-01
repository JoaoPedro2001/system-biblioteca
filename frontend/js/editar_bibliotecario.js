const parametros = new URLSearchParams(
    window.location.search
)

const bibliotecarioId = parametros.get("id")

async function carregarBibliotecario() {

    const resposta = await fetch(
        `http://127.0.0.1:5001/bibliotecarios/${bibliotecarioId}`
    )

    const bibliotecario = await resposta.json()

    document.getElementById(
        "nome"
    ).value = bibliotecario.nome

    document.getElementById(
        "email"
    ).value = bibliotecario.email

    if (bibliotecario.admin === true) {
        document.getElementById(
            "admin-sim"
        ).checked = true
    }else{
        document.getElementById(
            "admin-nao"
        ).checked = true
    }
}

carregarBibliotecario()

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

        if (senha !== "" && senha !== confirmarSenha) {
            alert(
                "Senha e confirmação de senha não coincidem"
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

            admin: adminSelecionado === "true"

        }

        if (senha !== "") {

            bibliotecario.senha = senha

        }

        const resposta = await fetch(
            `http://127.0.0.1:5001/bibliotecarios/${bibliotecarioId}`,
            {

                method: "PUT",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(bibliotecario)

            }
        )

        if (resposta.ok) {

            alert(
                "Bibliotecário atualizado com sucesso!"
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