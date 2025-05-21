import requests

API_TOKEN = ""
API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/c0645994d92ebf22e3b2c8c677dd02b2/ai/run/"
headers = {"Authorization": f"Bearer {API_TOKEN}"}  # <- aqui está corrigido

def run(model, inputs):
    input_data = {"messages": inputs}
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input_data)
    return response.json()

inputs = [
    {"role": "system", "content": "Você é um especialista em Turismo na Amazônia"},
    {"role": "user", "content": "Qual o local para ter banho com o boto?"}
]

output = run("@cf/meta/llama-3-8b-instruct", inputs)
print(output)
