from flask import Flask, request, jsonify
from flask_cors import CORS

APP_NAME = "SAGAR V DASARI The Embroidery Designer"
app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({
        "message": f"Welcome to {APP_NAME} API",
        "note": "This API helps you calculate embroidery stitch rates efficiently. Created by SAGAR V DASARI."
    })

@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        data = request.get_json()
        stitch = int(data.get("stitch", 0))
        stitch_price = float(data.get("stitch_price", 0))
        machine_head = float(data.get("machine_head", 0))

        if stitch <= 0 or stitch_price <= 0 or machine_head <= 0:
            return jsonify({"error": "All values must be positive numbers"}), 400

        one_head = (stitch / 1000) * stitch_price
        final_price = one_head * machine_head

        return jsonify({"final_price_per_meter": f"₹{final_price:.2f}"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
