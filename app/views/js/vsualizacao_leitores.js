async function carregarLeitores() {

            const resposta = await fetch(
                "http://127.0.0.1:5000/leitores"
            )

            const livros = await resposta.json()

            const tabela = document.getElementById(
                "tabela-leitores"
            )

            tabela.innerHTML = ""

            livros.forEach(leitor => {

                tabela.innerHTML += `
                
                    <tr>
                        <td>
                            <input
                                type="radio"
                                name="leitorSelecionado"
                                value="${leitor.id}"
                            >
                        </td>

                        <td>
                            ${leitor.id}
                        </td>

                        <td>
                            ${leitor.nome}
                        </td>

                        <td>
                            ${leitor.email}
                        </td>

                        <td>
                            ${leitor.telefone}
                        </td>
                        <td>
                            ${leitor.data_cadastro}
                        </td>

                    </tr>
                
                `
            })

        }

        function obterLeitorSelecionado() {

            const selecionado = document.querySelector(
                'input[name="leitorSelecionado"]:checked'
            )

            if (!selecionado) {

                alert("Selecione um leitor.")

                return null
            }

            return selecionado.value
        }

        function editarLeitor() {

            const id = obterLeitorSelecionado()

            if (!id) return

            window.location.href =`editar_leitor.html?id=${id}`

        }

        async function removerLeitor() {

            const leitorSelecionado = document.querySelector(
                'input[name="leitorSelecionado"]:checked'
            );

            if (!leitorSelecionado) {
                alert("Selecione um leitor");
                return;
            }

            const leitorId = leitorSelecionado.value;

            const confirmar = confirm(
                "Deseja realmente remover este leitor?"
            );

            if (!confirmar) {
                return;
            }

            try {

                const resposta = await fetch(
                    `http://127.0.0.1:5000/leitores/${leitorId}`,
                    {
                        method: "DELETE"
                    }
                );

                if (!resposta.ok) {
                    throw new Error("Erro ao remover leitor");
                }

                alert("Leitor removido com sucesso");

                carregarLeitores();

            } catch (erro) {

                console.error(erro);

                alert("Erro ao remover leitor");
            }

        }

        carregarLeitores()