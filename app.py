import streamlit as st # pyright: ignore[reportMissingImports]

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="MiniStore",
    page_icon="🛍️",
    layout="wide"
)

# --------------------------------------------------
# Custom CSS Styling
# --------------------------------------------------
st.markdown("""
<style>
    .main {
        background-color: #f8fafc;
    }

    .hero {
        background: linear-gradient(135deg, #2563eb, #7c3aed);
        padding: 40px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
    }

    .hero h1 {
        font-size: 3rem;
        margin-bottom: 10px;
    }

    .hero p {
        font-size: 1.1rem;
    }

    .product-card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
        margin-bottom: 20px;
        height: 280px;
    }

    .product-title {
        font-size: 1.2rem;
        font-weight: bold;
        color: #111827;
        margin-bottom: 8px;
    }

    .product-category {
        color: #6b7280;
        font-size: 0.9rem;
        margin-bottom: 10px;
    }

    .product-price {
        font-size: 1.3rem;
        color: #16a34a;
        font-weight: bold;
        margin-top: 12px;
    }

    .section-title {
        font-size: 2rem;
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    .footer {
        text-align: center;
        color: gray;
        margin-top: 30px;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Sample Product Data
# --------------------------------------------------
products = [
    {
        "name": "Wireless Headphones",
        "price": 79.99,
        "category": "Electronics",
        "description": "Premium noise-cancelling headphones with 30-hour battery life."
    },
    {
        "name": "Smart Watch",
        "price": 129.99,
        "category": "Electronics",
        "description": "Track fitness, monitor health, and receive notifications."
    },
    {
        "name": "Gaming Mouse",
        "price": 49.99,
        "category": "Accessories",
        "description": "Ergonomic RGB gaming mouse with customizable DPI settings."
    },
    {
        "name": "Laptop Backpack",
        "price": 39.99,
        "category": "Fashion",
        "description": "Water-resistant backpack designed for work and travel."
    },
    {
        "name": "Bluetooth Speaker",
        "price": 59.99,
        "category": "Electronics",
        "description": "Portable speaker delivering crystal-clear audio quality."
    },
    {
        "name": "Coffee Mug",
        "price": 14.99,
        "category": "Home",
        "description": "Stylish ceramic mug perfect for coffee and tea lovers."
    }
]

# --------------------------------------------------
# Initialize Cart in Session State
# --------------------------------------------------
if "cart" not in st.session_state:
    st.session_state.cart = []

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
st.sidebar.title("🛒 MiniStore")

categories = ["All"] + sorted(list(set(p["category"] for p in products)))

selected_category = st.sidebar.selectbox(
    "Browse Categories",
    categories
)

# Cart Summary
st.sidebar.markdown("---")
st.sidebar.subheader("Shopping Cart")

cart_count = len(st.session_state.cart)
cart_total = sum(item["price"] for item in st.session_state.cart)

st.sidebar.metric("Items", cart_count)
st.sidebar.metric("Total", f"${cart_total:.2f}")

# --------------------------------------------------
# Hero Section
# --------------------------------------------------
st.markdown("""
<div class="hero">
    <h1>🛍️ MiniStore</h1>
    <p>Your one-stop destination for quality products at amazing prices.</p>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Welcome Section
# --------------------------------------------------
st.header("Welcome to MiniStore")

st.write("""
Discover premium products across electronics, accessories,
fashion, and home essentials. Browse our featured collection
and add products to your cart.
""")

# --------------------------------------------------
# Filter Products
# --------------------------------------------------
if selected_category == "All":
    filtered_products = products
else:
    filtered_products = [
        p for p in products
        if p["category"] == selected_category
    ]

# --------------------------------------------------
# Featured Products Section
# --------------------------------------------------
st.markdown(
    '<div class="section-title">Featured Products</div>',
    unsafe_allow_html=True
)

# --------------------------------------------------
# Product Cards Layout using Columns
# --------------------------------------------------
cols = st.columns(3)

for index, product in enumerate(filtered_products):

    with cols[index % 3]:

        st.markdown(f"""
        <div class="product-card">
            <div class="product-title">{product['name']}</div>
            <div class="product-category">{product['category']}</div>
            <div>{product['description']}</div>
            <div class="product-price">${product['price']}</div>
        </div>
        """, unsafe_allow_html=True)

        # Add to Cart Button
        if st.button(
            f"Add to Cart",
            key=product["name"]
        ):
            st.session_state.cart.append(product)
            st.success(f"{product['name']} added to cart!")

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("""
<div class="footer">
    <hr>
    <p>© 2026 MiniStore | Demo E-Commerce Website Built with Streamlit</p>
</div>
""", unsafe_allow_html=True)