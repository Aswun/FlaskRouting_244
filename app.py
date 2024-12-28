from flask import Flask, render_template, request

app = Flask(__name__)

# Route untuk menampilkan form
@app.route("/")
def index():
    return render_template("form.html")

# Route untuk menerima data dari form
@app.route("/login", methods=["POST"])
def login():
    name = request.form.get("nm")
    return f"Selamat datang, {name}!"

if __name__ == "__main__":
    app.run(debug=True)