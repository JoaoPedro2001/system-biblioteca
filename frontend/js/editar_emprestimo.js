const parametros = new URLSearchParams(
    window.location.search
)

const emprestimoId = parametros.get("id")

async function carregarEmprestimo() {

    const resposta = await fetch(
        `http://127.0.0.1:5003/emprestimos/${emprestimoId}`
    )

    const emprestimo = await resposta.json()

    document.getElementById(
        "status"
    ).value = emprestimo.status

}

carregarEmprestimo()

const formulario = document.getElementById(
    "form-emprestimo"
)

formulario.addEventListener(
    "submit",
    async function(event) {

        event.preventDefault()

        const emprestimo = {

            renovar: document.getElementById(
                "renovar"
            ).checked,

            status: document.getElementById(
                "status"
            ).value

        }

        const resposta = await fetch(
            `http://127.0.0.1:5003/emprestimos/${emprestimoId}`,
            {

                method: "PUT",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(emprestimo)

            }
        )

        if (resposta.ok) {

            alert(
                "Empréstimo atualizado com sucesso!"
            )

            window.location.href =
                "visualizacao_emprestimos.html"

        }

        else {

            alert(
                "Erro ao atualizar empréstimo."
            )

        }

    }
)