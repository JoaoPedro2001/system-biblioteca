const parametros = new URLSearchParams(
    window.location.search
)

const livroId = parametros.get("id")

async function carregarLivro() {

    const resposta = await fetch(
        `http://127.0.0.1:5000/livros/${livroId}`
    )

    const livro = await resposta.json()

    document.getElementById(
        "titulo"
    ).value = livro.titulo

    document.getElementById(
        "autor"
    ).value = livro.autor

    document.getElementById(
        "isbn"
    ).value = livro.isbn

    document.getElementById(
        "categoria"
    ).value = livro.categoria

    document.getElementById(
        "quantidade"
    ).value = livro.quantidade_total

}

carregarLivro()

const formulario = document.getElementById(
    "form-livro"
)

formulario.addEventListener(
    "submit",
    async function(event) {

        event.preventDefault()

        const livro = {

            titulo: document.getElementById(
                "titulo"
            ).value,

            autor: document.getElementById(
                "autor"
            ).value,

            isbn: document.getElementById(
                "isbn"
            ).value,

            categoria: document.getElementById(
                "categoria"
            ).value,

            quantidade_total: parseInt(
                document.getElementById(
                    "quantidade"
                ).value
            ),

            quantidade_disponivel: parseInt(
                document.getElementById(
                    "quantidade"
                ).value
            )

        }

        const resposta = await fetch(
            `http://127.0.0.1:5000/livros/${livroId}`,
            {

                method: "PUT",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(livro)

            }
        )

        if (resposta.ok) {

            alert(
                "Livro atualizado com sucesso!"
            )

            window.location.href =
                "visualizacao_livros.html"

        }

        else {

            alert(
                "Erro ao atualizar livro."
            )

        }

    }
)