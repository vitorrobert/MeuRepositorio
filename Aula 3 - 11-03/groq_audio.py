# groq_audio.py
import os
from groq import Groq
import sys

# Você pode definir sua chave API diretamente aqui (não é a prática mais segura, mas facilita testes)
GROQ_API_KEY = "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"  # Coloque sua chave API entre as aspas

def transcribe(filename):
    """
    Transcreve um arquivo de áudio usando a API Groq.
    
    Args:
        filename: Caminho para o arquivo de áudio
    
    Returns:
        str: Texto transcrito
    """
    try:
        # Initialize the Groq client
        # Primeiro tenta usar a chave definida acima, depois tenta da variável de ambiente
        api_key = GROQ_API_KEY or os.environ.get("GROQ_API_KEY")
        
        if not api_key:
            return "Erro: API key do Groq não configurada. Defina GROQ_API_KEY no código ou como variável de ambiente."
            
        client = Groq(api_key=api_key)

        # Open the audio file
        with open(filename, "rb") as file:
            # Create a transcription of the audio file
            transcription = client.audio.transcriptions.create(
                file=(filename, file.read()),  # Required audio file
                model="whisper-large-v3-turbo",  # Required model
                prompt="",  # Optional
                response_format="json",  # Optional
                language="pt",  # Português
                temperature=0.0  # Optional
            )
            # Return the transcription text
            return transcription.text
            
    except Exception as e:
        return f"Erro na transcrição: {str(e)}"

# Este bloco permite que o script seja executado diretamente
if __name__ == "__main__":
    # Verifica se foi fornecido um caminho de arquivo como argumento
    if len(sys.argv) < 2:
        print("Uso: python groq_audio.py [caminho_do_arquivo_audio]")
        sys.exit(1)
    
    # Obtém o caminho do arquivo do argumento da linha de comando
    audio_file = sys.argv[1]
    
    # Verifica se o arquivo existe
    if not os.path.exists(audio_file):
        print(f"Arquivo não encontrado: {audio_file}")
        sys.exit(1)
    
    # Transcreve o áudio e imprime o resultado
    result = transcribe(audio_file)
    print(result)