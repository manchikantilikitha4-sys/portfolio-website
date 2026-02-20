from flask import Flask, render_template, request

# Create Flask app
app = Flask(__name__)

# Route for home page
@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    # Check if form submitted
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")

        # Show confirmation message
        message = f"Thank you {name}! Your email ({email}) has been received."

    return render_template("index.html", message=message)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)