from flask import Flask, jsonify, render_template
import download_script

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

#@app.route('/download', methods=['POST'])
@app.route('curl -X POST https://ProjetosPython.pythonanywhere.com/download', methods=['POST'])

def download():
    message = download_script.download_files()
    return jsonify({"message": message})

if __name__ == '__main__':
    app.run(debug=True)
