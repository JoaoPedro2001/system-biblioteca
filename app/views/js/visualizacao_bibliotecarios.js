async function carregarBibliotecarios() {

            const resposta = await fetch(
                "http://127.0.0.1:5000/bibliotecarios"
            )

            const bibliotecarios = await resposta.json()

            const tabela = document.getElementById(
                "tabela-bibliotecarios"
            )

            tabela.innerHTML = ""

            bibliotecarios.forEach(bibliotecario => {

                tabela.innerHTML += `
                
                    <tr>
                        <td>
                            <input
                                type="radio"
                                name="bibliotecarioSelecionado"
                                value="${bibliotecario.id}"
                            >
                        </td>

                        <td>
                            ${bibliotecario.id}
                        </td>

                        <td>
                            ${bibliotecario.nome}
                        </td>

                        <td>
                            ${bibliotecario.email}
                        </td>

                        <td>
                            ${bibliotecario.admin}
                        </td>

                    </tr>
                
                `
            })

        }

        function obterBibliotecaioSelecionado() {

            const selecionado = document.querySelector(
                'input[name="bibliotecarioSelecionado"]:checked'
            )

            if (!selecionado) {

                alert("Selecione um bibliotecário.")

                return null
            }

            return selecionado.value
        }

        function editarBibliotecario() {

            const id = obterBibliotecaioSelecionado()

            if (!id) return

            window.location.href =`editar_bibliotecario.html?id=${id}`

        }

        async function removerBibliotecario() {

            const bibliotecarioSelecionado = document.querySelector(
                'input[name="bibliotecarioSelecionado"]:checked'
            );

            if (!bibliotecarioSelecionado) {
                alert("Selecione um bibliotecário");
                return;
            }
            
            const bibliotecarioID = bibliotecarioSelecionado.value;

            const confirmar = confirm(
                "Deseja realmente remover este bibliotecário?"
            );

            if (!confirmar) {
                return;
            }

            try {

                const resposta = await fetch(
                    `http://127.0.0.1:5000/bibliotecarios/${bibliotecarioID}`,
                    {
                        method: "DELETE"
                    }
                );

                if (!resposta.ok) {
                    throw new Error("Erro ao remover bibliotecário");
                }

                alert("Bibliotecário removido com sucesso");

                carregarBibliotecarios();

            } catch (erro) {

                console.error(erro);

                alert("Erro ao remover bibliotecário");
            }
        
        }

        carregarBibliotecarios();