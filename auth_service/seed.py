from database import SessionLocal
from app.models.bibliotecario import Bibliotecario
from app.services.password_service import gerar_hash

db = SessionLocal()

print("Limpando dados antigos de autenticação...")
db.query(Bibliotecario).delete()
db.commit()

bibliotecarios = [
    Bibliotecario(nome="Administrador", email="admin@biblioteca.com", senha=gerar_hash("admin123"), admin=True),
    Bibliotecario(nome="Funcionário", email="funcionario@biblioteca.com", senha=gerar_hash("func123"), admin=False)
]

print("Populando tabelas do Auth Service...")
db.add_all(bibliotecarios)
db.commit()
db.close()
print("Auth Service populado com sucesso!")