from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
from groq_audio import transcribe  # Importa diretamente a função transcribe

app = Flask(__name__)

# Configuração para upload de arquivos
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'mp3', 'wav', 'ogg', 'm4a'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limite de 16MB para upload

# Garantir que a pasta de uploads exista
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Função para transcrever áudio usando a função importada do groq_audio.py
def transcribe_audio(file_path):
    try:
        result = transcribe(file_path)
        return result
    except Exception as e:
        return f"Erro ao transcrever o áudio: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'Nenhum arquivo selecionado'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Transcrever o áudio
        transcription = transcribe_audio(file_path)
        
        # Retornar o caminho do arquivo e a transcrição
        return jsonify({
            'file_path': '/'.join([UPLOAD_FOLDER, filename]),
            'transcription': transcription
        })
    
    return jsonify({'error': 'Tipo de arquivo não permitido'}), 400

if __name__ == '__main__':
    app.run(debug=True)