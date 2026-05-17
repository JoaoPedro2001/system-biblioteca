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
            "http://127.0.0.1:5000/livros",
            {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(livro)

            }
        )

        if (resposta.ok) {

            alert(
                "Livro cadastrado com sucesso!"
            )

            window.location.href =
                "visualizacao_livros.html"

        }

        else {

            alert(
                "Erro ao cadastrar livro."
            )

        }

    }
)