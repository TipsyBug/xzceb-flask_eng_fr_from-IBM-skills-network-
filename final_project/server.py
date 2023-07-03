from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/final_project/machinetranslation/englishToFrench", methods=['GET'])
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    french_text = translator.english_to_french(textToTranslate)
    return "Translated text to French: " + french_text

@app.route("/final_project/machinetranslation/frenchToEnglish", methods=['GET'])
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    english_text = translator.french_to_english(textToTranslate)
    return "Translated text to English: " + english_text

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
