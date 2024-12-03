from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock database
data_store = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"}
]

# Home endpoint
@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Basic API!"})

# Get all items
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(data_store)

# Get a single item by ID
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next((item for item in data_store if item["id"] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

# Create a new item
@app.route("/items", methods=["POST"])
def create_item():
    new_item = request.json
    if "id" not in new_item or "name" not in new_item:
        return jsonify({"error": "ID and name are required"}), 400
    data_store.append(new_item)
    return jsonify(new_item), 201

# Update an existing item
@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    item = next((item for item in data_store if item["id"] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    updated_data = request.json
    item.update(updated_data)
    return jsonify(item)

# Delete an item
@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    global data_store
    data_store = [item for item in data_store if item["id"] != item_id]
    return jsonify({"message": "Item deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8089)  # Change port to 8089
