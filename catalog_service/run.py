import os
from app import create_app

app = create_app()

if __name__ == "__main__":
    # Pega a porta das variáveis de ambiente (injetadas pelo docker-compose)
    # Se não encontrar, usa 5000 como fallback padrão
    port = int(os.environ.get("PORT", 5000))
    
    app.run(
        host="0.0.0.0",
        port=port,
        debug=True
    )