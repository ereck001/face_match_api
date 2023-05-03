# Face match api

This is a RESTful API for comparing two images of faces and determining how closely they match. It uses the Flask web framework and the face_match module for the actual image comparison.

## Installation
Clone this repository: git clone https://github.com/example/face-match-api.git
Install the required dependencies: pip install -r requirements.txt
Run the API: python app.py
Usage
Send a POST request to the /imgval endpoint with two images encoded in base64 in the request body. The API will compare the images and return a JSON response with the similarity score.

## Request Format
POST /imgval HTTP/1.1
Content-Type: application/json

{
    "imagem1": "base64-encoded-image1",
    "imagem2": "base64-encoded-image2"
}

## Response Format
HTTP/1.1 200 OK
Content-Type: application/json

{
    "similarity_score": 0.85
}
If there is an error during the image comparison process, the API will return a JSON response with an error message.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
