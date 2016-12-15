from flask import Flask, request, render_template, json
app = Flask(__name__)

# Best for access speed; array requires us looping over O(n) while hash table is a single action O(1)
# However, this isn't the best on space complexity as I'm duplicating the pet name entry
pet_list = {}


# allow for / or none at all
@app.route('/hello/', methods=['GET'])
@app.route('/hello', methods=['GET'])
def hello():
    """
    Return string "Hello World!"
    """
    return "Hello World!"


@app.route('/pets/', methods=['GET', 'POST'])
@app.route('/pets', methods=['GET', 'POST'])
def pets_route():
    """
    List all pets or add a new pet
    """
    if request.method == 'POST':
        json_pet = request.get_json()
        # data validation
        if validate_pet(json_pet):
            # data normalization with .lower() and check if already exists
            if json_pet['name'].lower() not in pet_list:
                pet_list[json_pet['name'].lower()] = json_pet
                return json.jsonify(json_pet), 201
            # else:
            return json.jsonify({'message': '%s is already in database' % (json_pet['name'].lower())}), 409
        # else:
        return json.jsonify({'message': 'Missing: name, age, or species'}), 400

    # Give full list of pets if just GET /pets
    return json.jsonify(pet_list)


@app.route('/pets/<name>/', methods=['GET', 'PUT', 'DELETE'])
@app.route('/pets/<name>', methods=['GET', 'PUT', 'DELETE'])
def pet_name_route(nameInput):
    """
    Retrieve, Update, or Remove a specific pet
    """
    # Normalize data to prevent extra variations
    name = nameInput.lower()
    if name in pet_list:

        if request.method == 'PUT':
            json_pet = request.get_json()

            # validate test
            if validate_pet(json_pet):
                pet_list[name] = json_pet
                return json.jsonify(json_pet)
            # pet is not valid
            return json.jsonify({'message': 'Missing: name, age, or species'}), 400

        if request.method == 'DELETE':
            return json.jsonify(pet_list.pop(name))
        # GET end catch all
        return json.jsonify(pet_list[name])

    # pet can't be found for any of the methods
    return json.jsonify({'message': 'Can\'t find this specific pet'}), 404


def validate_pet(json):
    """
    Check if valid pet
    """
    if 'name' in json and 'age' in json and 'species' in json:
        return True
    return False


if __name__ == "__main__":
    app.run()
