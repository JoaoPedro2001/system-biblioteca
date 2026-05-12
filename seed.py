from datetime import date

from database import SessionLocal

from app.models.bibliotecario import Bibliotecario
from app.models.leitor import Leitor
from app.models.livro import Livro
from app.models.emprestimo import Emprestimo

# Criar sessão
db = SessionLocal()

# Apagar dados se existirem para evitar duplicação
db.query(Emprestimo).delete()
db.query(Livro).delete()
db.query(Leitor).delete()
db.query(Bibliotecario).delete()

# Salvar alterações
db.commit()

# Dados iniciais da tabela bibliotecario
bibliotecarios = [
    Bibliotecario(
        nome="Administrador",
        email="admin@biblioteca.com",
        senha="admin123",
        admin=True
    ),

    Bibliotecario(
        nome="Funcionário",
        email="funcionario@biblioteca.com",
        senha="func123",
        admin=False
    )
]

# Dados iniciais da tabela leitor
leitores = [
    Leitor(
        nome="João Silva",
        email="joao@email.com",
        telefone="81999990001",
        data_cadastro=date.today()
    ),

    Leitor(
        nome="Maria Souza",
        email="maria@email.com",
        telefone="81999990002",
        data_cadastro=date.today()
    ),

    Leitor(
        nome="Carlos Lima",
        email="carlos@email.com",
        telefone="81999990003",
        data_cadastro=date.today()
    )
]

# Dados iniciais da tabela livro
livros = [    
    Livro(
        titulo="Dom Casmurro",
        autor="Machado de Assis",
        isbn="8525406791",
        categoria="Romance",
        quantidade_total=5,
        quantidade_disponivel=5
    ),

    Livro(
        titulo="Capitães da Areia",
        autor="Jorge Amado",
        isbn="8501005304",
        categoria="Romance",
        quantidade_total=4,
        quantidade_disponivel=4
    ),

    Livro(
        titulo="Vidas Secas",
        autor="Graciliano Ramos",
        isbn="8501067342",
        categoria="Romance",
        quantidade_total=3,
        quantidade_disponivel=3
    ),

    Livro(
        titulo="O Cortiço",
        autor="Aluísio Azevedo",
        isbn="8500714905",
        categoria="Romance",
        quantidade_total=4,
        quantidade_disponivel=4
    ),

    Livro(
        titulo="A Hora da Estrela",
        autor="Clarice Lispector",
        isbn="9727086535",
        categoria="Romance",
        quantidade_total=3,
        quantidade_disponivel=3
    ),

    Livro(
        titulo="Sistemas Operacionais Modernos",
        autor="Andrew S. Tanenbaum",
        isbn="9788576052371",
        categoria="Sistemas Operacionais",
        quantidade_total=6,
        quantidade_disponivel=6
    ),

    Livro(
        titulo="Redes de Computadores",
        autor="Andrew S. Tanenbaum",
        isbn="8535211853",
        categoria="Redes",
        quantidade_total=5,
        quantidade_disponivel=5
    ),

    Livro(
        titulo="Estruturas de Dados e Algoritmos em Java",
        autor="Robert Lafore",
        isbn="8573933755",
        categoria="Estruturas de Dados",
        quantidade_total=4,
        quantidade_disponivel=4
    ),

    Livro(
        titulo="1984",
        autor="George Orwell",
        isbn="6587034209",
        categoria="Ficção",
        quantidade_total=3,
        quantidade_disponivel=3
    ),

    Livro(
        titulo="O Hobbit",
        autor="J.R.R. Tolkien",
        isbn="8595086087",
        categoria="Fantasia",
        quantidade_total=4,
        quantidade_disponivel=4
    )
]

# Adicionar no banco
db.add_all(bibliotecarios)
db.add_all(leitores)
db.add_all(livros)

# Salvar alterações
db.commit()

# Fechar sessão
db.close()

print("Banco populado com sucesso!")