from database import SessionLocal
from app.models.bibliotecario import Bibliotecario

db = SessionLocal()

print("Limpando dados antigos de autenticação...")
db.query(Bibliotecario).delete()
db.commit()

bibliotecarios = [
    Bibliotecario(nome="Administrador", email="admin@biblioteca.com", senha="admin123", admin=True),
    Bibliotecario(nome="Funcionário", email="funcionario@biblioteca.com", senha="func123", admin=False)
]

print("Populando tabelas do Auth Service...")
db.add_all(bibliotecarios)
db.commit()
db.close()
print("Auth Service populado com sucesso!")