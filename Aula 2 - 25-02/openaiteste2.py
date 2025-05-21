import openai

# Sua chave da API da OpenAI
openai.api_key = ""  # Substitua pela sua chave real

# Configurações do modelo
modelo = "gpt-4"           # Pode ser "gpt-4", "gpt-4o", "gpt-3.5-turbo", etc.
temperatura = 0.7          # Entre 0.0 (mais determinístico) e 1.0 (mais criativo)
max_tokens = 1000          # Limite de tokens na resposta
top_p = 1.0                # Top-p sampling (nucleus sampling)
frequency_penalty = 0.0    # Penalidade para repetir palavras
presence_penalty = 0.0     # Incentivo para falar de novos assuntos

# Prompt de entrada (pergunta)
mensagem = "Explique de forma simples o que é inteligência artificial."

# Envio da requisição para o modelo
resposta = openai.ChatCompletion.create(
    model=modelo,
    messages=[
        {"role": "system", "content": "Você é um assistente útil e objetivo."},
        {"role": "user", "content": mensagem}
    ],
    temperature=temperatura,
    max_tokens=max_tokens,
    top_p=top_p,
    frequency_penalty=frequency_penalty,
    presence_penalty=presence_penalty
)

# Exibição da resposta
print(resposta['choices'][0]['message']['content'])
