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

# Salvar alterações da limpeza
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

# Definição dos dados base dos livros (sem instanciar ainda)
dados_livros = [    
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "isbn": "8525406791", "categoria": "Romance"},
    {"titulo": "Capitães da Areia", "autor": "Jorge Amado", "isbn": "8501005304", "categoria": "Romance"},
    {"titulo": "Vidas Secas", "autor": "Graciliano Ramos", "isbn": "8501067342", "categoria": "Romance"},
    {"titulo": "O Cortiço", "autor": "Aluísio Azevedo", "isbn": "8500714905", "categoria": "Romance"},
    {"titulo": "A Hora da Estrela", "autor": "Clarice Lispector", "isbn": "9727086535", "categoria": "Romance"},
    {"titulo": "Sistemas Operacionais Modernos", "autor": "Andrew S. Tanenbaum", "isbn": "9788576052371", "categoria": "Sistemas Operacionais"},
    {"titulo": "Redes de Computadores", "autor": "Andrew S. Tanenbaum", "isbn": "8535211853", "categoria": "Redes"},
    {"titulo": "Estruturas de Dados e Algoritmos em Java", "autor": "Robert Lafore", "isbn": "8573933755", "categoria": "Estruturas de Dados"},
    {"titulo": "1984", "autor": "George Orwell", "isbn": "6587034209", "categoria": "Ficção"},
    {"titulo": "O Hobbit", "autor": "J.R.R. Tolkien", "isbn": "8595086087", "categoria": "Fantasia"}
]

# Lista que vai guardar as instâncias de objetos Livro que serão salvas
livros_exemplares = []

# Loop para gerar 3 cópias distintas de cada livro
for dados in dados_livros:
    for i in range(1, 4):  # Vai rodar 3 vezes (1, 2 e 3)
        exemplar = Livro(
            titulo=dados["titulo"],
            autor=dados["autor"],
            isbn=dados["isbn"],
            categoria=dados["categoria"],
            status="disponivel",  # Padrão para novos exemplares
            observacoes=f"Exemplar {i}"  # Opcional: ajuda a identificar a cópia visualmente
        )
        livros_exemplares.append(exemplar)

# Adicionar no banco
db.add_all(bibliotecarios)
db.add_all(leitores)
db.add_all(livros_exemplares)

# Salvar alterações finais
db.commit()

# Fechar sessão
db.close()

print("Banco populado com sucesso com 3 exemplares de cada livro!")