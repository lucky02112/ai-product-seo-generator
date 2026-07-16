def generate_title(product, brand, material, color, category):
    return f"{brand} {color} {material} {product} | Premium {category}"

def generate_description(product, brand, material, color, category):
    return (
        f"The {brand} {product} is made from premium {material}. "
        f"It features a stylish {color} finish and is ideal for daily use."
    )

def generate_keywords(product, brand, material, color, category):
    return [
        product,
        brand,
        material,
        color,
        category,
        f"{brand} {product}",
        f"{color} {product}",
        f"{material} {category}"
    ]
