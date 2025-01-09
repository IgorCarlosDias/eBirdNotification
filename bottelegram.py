import requests

TELEGRAM_API_TOKEN = ''

url = f"https://api.telegram.org/bot{TELEGRAM_API_TOKEN}/getUpdates"
response = requests.get(url)
updates = response.json()

# Exibe as atualizações para encontrar o chat_id
print(updates)
