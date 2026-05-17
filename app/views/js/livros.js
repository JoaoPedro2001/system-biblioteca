async function carregarLivros() {

            const resposta = await fetch(
                "http://127.0.0.1:5000/livros"
            )

            const livros = await resposta.json()

            const tabela = document.getElementById(
                "tabela-livros"
            )

            tabela.innerHTML = ""

            livros.forEach(livro => {

                tabela.innerHTML += `
                
                    <tr>

                        <td>
                            <input
                                type="radio"
                                name="livroSelecionado"
                                value="${livro.id}"
                            >
                        </td>

                        <td>
                            ${livro.id}
                        </td>

                        <td>
                            ${livro.titulo}
                        </td>

                        <td>
                            ${livro.autor}
                        </td>

                        <td>
                            ${livro.isbn}
                        </td>
                        <td>
                            ${livro.categoria}
                        </td>
                        <td>
                            ${livro.quantidade_total}
                        </td>
                        <td>
                            ${livro.quantidade_disponivel}
                        </td>

                    </tr>
                
                `
            })

        }

        function obterLivroSelecionado() {

            const selecionado = document.querySelector(
                'input[name="livroSelecionado"]:checked'
            )

            if (!selecionado) {

                alert("Selecione um livro.")

                return null
            }

            return selecionado.value
        }

        function editarLivro() {

            const id = obterLivroSelecionado()

            if (!id) return

            window.location.href =`editar_livro.html?id=${id}`

        }

        async function removerLivro() {

            const livroSelecionado = document.querySelector(
                'input[name="livroSelecionado"]:checked'
            );

            if (!livroSelecionado) {
                alert("Selecione um livro");
                return;
            }

            const livroId = livroSelecionado.value;

            const confirmar = confirm(
                "Deseja realmente remover este livro?"
            );

            if (!confirmar) {
                return;
            }

            try {

                const resposta = await fetch(
                    `http://127.0.0.1:5000/livros/${livroId}`,
                    {
                        method: "DELETE"
                    }
                );

                if (!resposta.ok) {
                    throw new Error("Erro ao remover livro");
                }

                alert("Livro removido com sucesso");

                carregarLivros();

            } catch (erro) {

                console.error(erro);

                alert("Erro ao remover livro");
            }

        }

        carregarLivros()