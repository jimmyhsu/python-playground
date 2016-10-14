from flask import Flask, request, render_template, json
app = Flask(__name__)

pet_list = {}

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
        if 'name' in json_pet and 'age' in json_pet and 'species' in json_pet:
            pet_list[json_pet['name']] = json_pet
            return json.jsonify(json_pet)
        else:
            return json.jsonify({'message': 'Missing: name, age, or species'}), 400

    return json.jsonify(pet_list)

@app.route('/pets/<name>', methods=['GET'])
def get_pet(name):
    """
    Get Specific Pet
    """
    print(pet_list)
    print(name)
    if name in pet_list:
        return json.jsonify(pet_list[name])
    else:
        return json.jsonify({'message': 'Can\'t find this specific pet' }), 404


if __name__ == "__main__":
    app.run()
