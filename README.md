# Instagram Agent

Um agente automático para gerenciar seu Instagram.

## Funcionalidades
- 📱 Publicar posts automaticamente
- 💬 Responder comentários
- ❤️ Dar likes em posts relacionados
- 📊 Análise de métricas
- ⏰ Agendamento de publicações

## Instalação

### Requisitos
- Python 3.8+
- Pip

### Setup
```bash
git clone https://github.com/aj311281aj-create/instagram-agent.git
cd instagram-agent
pip install -r requirements.txt
```

### Configuração
1. Crie um arquivo `.env` na raiz do projeto
2. Adicione suas credenciais do Instagram:
```
INSTAGRAM_USERNAME=seu_usuario
INSTAGRAM_PASSWORD=sua_senha
```

## Uso

```python
from instagram_agent import InstagramAgent

agent = InstagramAgent()
ag1ent.login()
ag1ent.post_content("Sua mensagem aqui")
```

## Estrutura do Projeto
```
instagram-agent/
├── main.py
├── instagram_agent.py
├── requirements.txt
├── .env.example
└── README.md
```

## Licença
MIT