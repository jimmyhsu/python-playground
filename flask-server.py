from flask import Flask, request, render_template, json
app = Flask(__name__)

pet_array = []

@app.route('/hello/', methods=['GET'])
def hello():
    """
    Return string "Hello World!"
    """
    return "Hello World!"

@app.route('/pets/', methods=['GET', 'POST'])
def pets():
    """
    List or create pets
    """
    if request.method == 'POST':
        json_pet = request.get_json()
        print(json_pet)
        if 'name' in json_pet and 'age' in json_pet and 'species' in json_pet:
            pet_array.append(json_pet)
            return json.jsonify(json_pet)
        else:
            return json.jsonify({'message': 'Missing: name, age, or species'}), 400

    return jsonify(pet_array)

if __name__ == "__main__":
    app.run()
