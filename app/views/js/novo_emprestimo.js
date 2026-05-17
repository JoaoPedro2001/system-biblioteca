async function carregarLivros() {
    const resposta = await fetch("http://127.0.0.1:5000/livros")

    const livros = await resposta.json()

    const selectLivro = document.getElementById("livro")

    livros.forEach(livro => {
        selectLivro.innerHTML += `<option value="${livro.id}">${livro.titulo}</option>`
    })
}

async function carregarLeitores() {
    const resposta = await fetch("http://127.0.0.1:5000/leitores")

    const leitores = await resposta.json()

    const selectLeitor = document.getElementById("leitor")

    leitores.forEach(leitor => {
        selectLeitor.innerHTML += `<option value="${leitor.id}">${leitor.nome}</option>`
    })
}

async function carregarBibliotecarios() {
    const resposta = await fetch("http://127.0.0.1:5000/bibliotecarios")

    const bibliotecarios = await resposta.json()

    const selectBibliotecario = document.getElementById("bibliotecario")

    bibliotecarios.forEach(bibliotecario => {
        selectBibliotecario.innerHTML += `<option value="${bibliotecario.id}">${bibliotecario.nome}</option>`
    })
}

carregarLivros()
carregarLeitores()
carregarBibliotecarios()

const formulario = document.getElementById(
    "form-emprestimo"
)

formulario.addEventListener(
    "submit",
    async function(event) {
        event.preventDefault()

        const emprestimo = {

            livro_id: document.getElementById(
                "livro"
            ).value,

            leitor_id: document.getElementById(
                "leitor"
            ).value,

            bibliotecario_id: document.getElementById(
                "bibliotecario"
            ).value
        }
        

        const resposta = await fetch(
           "http://127.0.0.1:5000/emprestimos",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(emprestimo)

            } 
        )

        if (resposta.ok) {
            alert(
                "Empréstimo cadastrado com sucesso!"
            )

            window.location.href = "visualizacao_emprestimos.html"
        }

        else {
            alert(
                "Erro ao cadastrar empréstimo."
            )

        }
        
    }
)