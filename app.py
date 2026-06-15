import streamlit as st
from products import products

st.set_page_config(
    page_title="MiniStore",
    page_icon="🛍️",
    layout="wide"
)

# -------------------------
# Floating Assistant Button
# -------------------------
st.markdown("""
<style>

.support-button {
    position: fixed;
    bottom: 30px;
    right: 30px;
    background: #4f46e5;
    color: white;
    padding: 15px 22px;
    border-radius: 50px;
    font-size: 18px;
    font-weight: bold;
    text-decoration: none;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
    z-index: 999;
}

.support-button:hover {
    background: #4338ca;
}

.product-card{
    border:1px solid #ddd;
    padding:20px;
    border-radius:15px;
    margin-bottom:15px;
    background:white;
}

</style>

<a class="support-button"
href="/MiniStore_Assistant"
target="_self">
🤖 Ask MiniStore AI
</a>
""",
unsafe_allow_html=True)

st.title("🛍️ MiniStore")

st.subheader("Modern Shopping Experience")

st.write(
"""
Browse our collection of premium products.
Need help choosing?
Our AI assistant can recommend products,
answer support questions, and help track orders.
"""
)

st.markdown("## Featured Products")

cols = st.columns(3)

for i, product in enumerate(products):

    with cols[i % 3]:

        st.markdown(
            f"""
            <div class="product-card">
                <h3>{product['name']}</h3>
                <p>{product['description']}</p>
                <b>Category:</b> {product['category']}<br>
                <b>Price:</b> ${product['price']}
            </div>
            """,
            unsafe_allow_html=True
        )