async function carregarEmprestimos() {

            const resposta = await fetch(
                "http://127.0.0.1:5000/emprestimos"
            )

            const bibliotecarios = await resposta.json()

            const tabela = document.getElementById(
                "tabela-emprestimos"
            )

            tabela.innerHTML = ""

            bibliotecarios.forEach(emprestimo => {

                tabela.innerHTML += `
                
                    <tr>
                        <td>
                            <input
                                type="radio"
                                name="bibliotecarioSelecionado"
                                value="${emprestimo.id}"
                            >
                        </td>

                        <td>
                            ${emprestimo.id}
                        </td>

                    </tr>
                
                `
            })

        }

        function obterEmprestimoSelecionado() {

            const selecionado = document.querySelector(
                'input[name="bibliotecarioSelecionado"]:checked'
            )

            if (!selecionado) {

                alert("Selecione um bibliotecário.")

                return null
            }

            return selecionado.value
        }

        function editarEmprestimo() {

            const id = obterBibliotecaioSelecionado()

            if (!id) return

            window.location.href =`editar_emprestimo.html?id=${id}`

        }

        async function removerEmprestimo() {

            const emprestimoSelecionado = document.querySelector(
                'input[name="emprestimoSelecionado"]:checked'
            );

            if (!emprestimoSelecionado) {
                alert("Selecione um bibliotecário");
                return;
            }
            
            const emprestimoID = emprestimoSelecionado.value;

            const confirmar = confirm(
                "Deseja realmente remover este empréstimo?"
            );

            if (!confirmar) {
                return;
            }

            try {

                const resposta = await fetch(
                    `http://127.0.0.1:5000/emprestimos/${emprestimoID}`,
                    {
                        method: "DELETE"
                    }
                );

                if (!resposta.ok) {
                    throw new Error("Erro ao remover empréstimo");
                }

                alert("Empréstimo removido com sucesso");

                carregarEmprestimos();

            } catch (erro) {

                console.error(erro);

                alert("Erro ao remover empréstimo");
            }
        
        }

        carregarEmprestimos();