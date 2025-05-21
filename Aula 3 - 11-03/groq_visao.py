import requests
import base64

# URL do Worker AI da Cloudflare
API_URL = "https://api.cloudflare.com/client/v4/accounts/c0645994d92ebf22e3b2c8c677dd02b2/ai/run/@cf/black-forest-labs/flux-1-schnell"

# Substitua pela sua chave de API (se necessário)
HEADERS = {
    "Authorization": "Bearer Gn9rP82OhTfEwXN4jm1pDNk7Zr6oyQtCKMP-A27k",
    "Content-Type": "application/json"
}

# Prompt para gerar a imagem
DATA = {
    "prompt": " Crie uma imagem de Papel de Parede do Pinguim do Linux com roupa do exercito e jogando a bandeira do windows no lixo",
    "width": 1024,
    "height": 1024,
    "num_inference_steps": 30
}

# Faz a requisição para gerar a imagem
response = requests.post(API_URL, json=DATA, headers=HEADERS)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    result = response.json()
    
    image_base64 = result["result"]["image"]
    
    if image_base64:
        # Converte Base64 para imagem
        try:
            with open("output.png", "wb") as img_file:
                img_file.write(base64.b64decode(image_base64))
            print("Imagem salva como output.png")
        except Exception as e:
            print(f"Erro ao decodificar a imagem: {e}")
else:
    print(f"Erro: {response.status_code}, {response.text}")