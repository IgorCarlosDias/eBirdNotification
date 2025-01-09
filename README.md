eBird Notification - Monitoramento de Observações de Aves 🦜

Uma aplicação que integra a API do eBird para monitorar observações de aves em tempo real e notificar usuários sobre espécies de interesse. Ideal para pesquisadores, conservacionistas e observadores de aves.

Recursos

Consulta automática de observações recentes de aves.

Filtros para espécies e regiões específicas.

Notificações automáticas via Telegram.

Interface amigável para visualização de dados.

Tecnologias Utilizadas

Backend: Flask

Frontend: HTML, CSS, JavaScript

API: eBird

Banco de Dados: Nenhum armazenamento local utilizado (dados consultados diretamente da API do eBird)

Servidor: Waitress

Notificação: Telegram Bot

Instalação e Configuração

1. Clone o Repositório
https://github.com/seu-usuario/eBirdNotification.git cd ebird-notification

2. Crie e Ative o Ambiente Virtual

python -m venv venv
# Ative o venv:
# Windows
venv\Scripts\activate
# Linux/MacOS
source venv/bin/activate

3. Instale as Dependências

pip install -r requirements.txt

4. Configure as Variáveis

Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:

TELEGRAM_API_TOKEN=seu_token_do_telegram
CHAT_ID=seu_chat_id

5. Execute a Aplicação

python run.py

A aplicação estará disponível em: http://127.0.0.1:8080

6. Acesse a Interface Web

Abra o navegador e acesse http://127.0.0.1:8080. Insira o token da API do eBird para iniciar o monitoramento.

Uso

Insira o token da API do eBird na interface web.

Visualize as observações recentes de aves na interface.

Receba notificações automáticas via Telegram quando a espécie configurada for identificada.

Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.
