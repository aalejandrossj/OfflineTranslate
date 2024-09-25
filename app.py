from flask import Flask, render_template, request, redirect, url_for
from translate import Translator

app = Flask(__name__)

@app.route('/')
def index():
    # Renderiza la página principal
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    # Obtiene el texto y los idiomas de origen y destino del formulario
    text = request.form['text']
    source_language = request.form['source_language']
    target_language = request.form['language']
    
    # Crea un traductor con los idiomas especificados
    translator = Translator(from_lang=source_language, to_lang=target_language)
    
    # Divide el texto en bloques de 500 caracteres
    blocks = [text[i:i+500] for i in range(0, len(text), 500)]
    
    # Traduce cada bloque y concatena los resultados
    translated_blocks = [translator.translate(block) for block in blocks]
    translated_text = ''.join(translated_blocks)
    
    # Renderiza la página principal con el texto traducido
    return render_template('index.html', translated_text=translated_text, original_text=text, target_language=target_language)

@app.route('/restart')
def restart():
    # Redirige a la página principal
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Ejecuta la aplicación Flask en modo de depuración
    app.run(debug=True)