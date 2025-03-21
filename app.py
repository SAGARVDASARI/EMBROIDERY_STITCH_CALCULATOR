from flask import Flask , request ,jsonify
from flask_cors import CORS
APP_NAME = "SAGAR V DASARI The Embroidery Designer"
app = Flask(__name__)
CORS(app)

stitch = int(input("Enter Embroidery stitch: "))
stitch_price = float(input("Enter 1000 stitch price per meter: "))
machine_head = float(input("Enter meter divisions asper head area: "))

one_head = (stitch/1000)*stitch_price
final_price = one_head * machine_head

print(f"\nYour final price per meter is: ₹{final_price:.2f}")

def home() :
    return jsonify({
    "message":f"Welcome to {APP_NAME} API","note":"This API helps you calculate embroidery stitch rates efficiently . create by SAGAR V DASARI."
    })
if __name__ == '__main__':
    app.run(debug=True)