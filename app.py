from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

# Variável para armazenar o token do eBird
ebird_token = None
TELEGRAM_API_TOKEN = ''  # Substitua pelo seu Token
CHAT_ID = ''  # Substitua pelo seu chat_id

# Função para obter aves de São Paulo
def obter_aves():
    if not ebird_token:
        return {"error": "Token do eBird não fornecido."}

    url = "https://api.ebird.org/v2/data/obs/BR-SP/recent"
    headers = {
        'X-eBirdApiToken': ebird_token
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        aves = response.json()

        # Verificar se a espécie "Sporophila lineola" foi observada
        for ave in aves:
            if ave.get('sciName') == 'Sporophila lineola':
                # Enviar mensagem de notificação via Telegram
                enviar_mensagem_telegram(f"A espécie Sporophila lineola foi observada em {ave.get('locName')}")
                break  # Para evitar múltiplas mensagens, interrompe após a primeira ocorrência
        return aves
    else:
        print(f"Erro ao obter dados: {response.status_code} - {response.text}")
        return {"error": "Não foi possível obter as aves."}

# Função para enviar uma mensagem via Telegram
def enviar_mensagem_telegram(mensagem):
    url = f'https://api.telegram.org/bot{TELEGRAM_API_TOKEN}/sendMessage'
    params = {
        'chat_id': CHAT_ID,
        'text': mensagem
    }
    response = requests.post(url, params=params)
    if response.status_code == 200:
        print("Mensagem enviada com sucesso!")
    else:
        print(f"Erro ao enviar mensagem: {response.status_code}")

# Rota para a página principal
@app.route('/')
def index():
    return render_template('index.html')

# Rota para obter as aves
@app.route('/aves', methods=['GET'])
def aves():
    aves_data = obter_aves()
    return jsonify(aves_data)

# Rota para salvar o token do eBird
@app.route('/salvar-token', methods=['POST'])
def salvar_token():
    global ebird_token
    try:
        # Obter o token do corpo da requisição
        token = request.json.get('token')
        
        # Verificar se o token foi enviado
        if token:
            ebird_token = token
            return jsonify({"message": "Token salvo com sucesso!"}), 200
        else:
            return jsonify({"error": "Token não fornecido!"}), 400
    except Exception as e:
        print(f"Erro ao processar o JSON: {e}")
        return jsonify({"error": "Falha ao processar a requisição."}), 400

if __name__ == '__main__':
    app.run(debug=True)