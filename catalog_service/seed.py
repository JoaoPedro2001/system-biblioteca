# catalog_service/seed.py
from datetime import date
from database import SessionLocal
from app.models.leitor import Leitor
from app.models.livro import Livro

db = SessionLocal()

print("Limpando dados antigos do catálogo...")
db.query(Livro).delete()
db.query(Leitor).delete()
db.commit()

leitores = [
    Leitor(nome="João Silva", email="joao@email.com", telefone="81999990001", data_cadastro=date.today()),
    Leitor(nome="Maria Souza", email="maria@email.com", telefone="81999990002", data_cadastro=date.today()),
    Leitor(nome="Carlos Lima", email="carlos@email.com", telefone="81999990003", data_cadastro=date.today())
]

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

livros_exemplares = []
for dados in dados_livros:
    for i in range(1, 4):
        exemplar = Livro(
            titulo=dados["titulo"],
            autor=dados["autor"],
            isbn=dados["isbn"],
            categoria=dados["categoria"],
            status="disponivel",
            observacoes=f"Exemplar {i}"
        )
        livros_exemplares.append(exemplar)

print("Populando tabelas do Catalog Service...")
db.add_all(leitores)
db.add_all(livros_exemplares)
db.commit()
db.close()
print("Catalog Service populado com sucesso!")