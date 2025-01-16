from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the Excel data
FILE_PATH = "student data.xlsx"
data_frame = pd.read_excel(FILE_PATH)
data = data_frame.to_dict(orient="records")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data", methods=["GET"])
def get_data():
    return jsonify(data)

@app.route("/search", methods=["POST"])
def search_data():
    query = request.json.get("query", "").lower()
    if not query:
        return jsonify(data)  # Return all data if query is empty

    filtered_data = [row for row in data if any(query in str(value).lower() for value in row.values())]
    return jsonify(filtered_data)

if __name__ == "__main__":
    app.run(debug=True)
