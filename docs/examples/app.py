from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():

    product = request.form.get("product")
    brand = request.form.get("brand")
    material = request.form.get("material")
    color = request.form.get("color")
    category = request.form.get("category")

    title = f"{brand} {color} {material} {product} | Premium {category}"

    description = (
        f"The {brand} {product} is made from high-quality {material}. "
        f"This {color} {category} is designed for durability, comfort, "
        f"and everyday use."
    )

    keywords = (
        f"{product}, {brand}, {material}, "
        f"{color}, {category}, premium {product}"
    )

    return render_template(
        "index.html",
        title=title,
        description=description,
        keywords=keywords
    )

if __name__ == "__main__":
    app.run(debug=True)
