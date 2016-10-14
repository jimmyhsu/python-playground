from flask import Flask, request, render_template, json
app = Flask(__name__)

# Best for access speed; array requires us looping over O(n) while hash table is a single action O(1)
# However, this isn't the best on space complexity as I'm duplicating the pet name entry
pet_list = {}

# Routes should also work for just /hello or /pets, but chrome append / bug makes this frustrating
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
        # Data Validation
        if 'name' in json_pet and 'age' in json_pet and 'species' in json_pet:
            pet_list[json_pet['name']] = json_pet
            return json.jsonify(json_pet)
        else:
            return json.jsonify({'message': 'Missing: name, age, or species'}), 400

    # Give full list of pets if just GET /pets
    return json.jsonify(pet_list)

@app.route('/pets/<name>', methods=['GET'])
def get_pet(name):
    """
    Get Specific Pet
    """
    if name in pet_list:
        return json.jsonify(pet_list[name])
    else:
        return json.jsonify({'message': 'Can\'t find this specific pet' }), 404


if __name__ == "__main__":
    app.run()
