# -*- coding: iso-8859-1 -*-
## Api de comparação de selfies 
#

from flask import Flask, request, jsonify
import base64
from face_match import compare
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/imgval', methods=['POST'])
def ValidateImage():    
    data = request.get_json()  
    img1 = data['imagem1']
    img2 = data['imagem2']

    img_bytes = base64.b64decode(img1)

    with open(".pic.jpg", "wb") as f:
        f.write(img_bytes)
    
    img_bytes = base64.b64decode(img2)

    with open(".pic2.jpg", "wb") as f:
        f.write(img_bytes)

    response = jsonify(compare(
        ".pic.jpg",
        ".pic2.jpg"
    ))

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')