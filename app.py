import streamlit as st
from products import products

st.set_page_config(
    page_title="MiniStore",
    page_icon="🛍️",
    layout="wide"
)

st.markdown("""
<style>

:root {
    --bg: #f5f7ff;
    --card: rgba(255, 255, 255, 0.82);
    --text: #10233f;
    --muted: #56657f;
    --accent: #0f766e;
    --accent-2: #2563eb;
    --border: rgba(16, 35, 63, 0.08);
}

body {
    background:
        radial-gradient(circle at top left, rgba(37, 99, 235, 0.14), transparent 32%),
        radial-gradient(circle at top right, rgba(15, 118, 110, 0.12), transparent 28%),
        linear-gradient(180deg, #f7f9ff 0%, #eef4ff 100%);
    color: var(--text);
}

.stApp {
    background: transparent;
}

.hero {
    padding: 2rem 2.2rem;
    border: 1px solid var(--border);
    border-radius: 28px;
    background: linear-gradient(135deg, rgba(255,255,255,0.92), rgba(240,245,255,0.78));
    box-shadow: 0 24px 80px rgba(16, 35, 63, 0.08);
}

.hero-kicker {
    display: inline-block;
    padding: 0.35rem 0.8rem;
    border-radius: 999px;
    background: rgba(15, 118, 110, 0.12);
    color: var(--accent);
    font-size: 0.85rem;
    font-weight: 700;
    letter-spacing: 0.02em;
    margin-bottom: 1rem;
}

.hero h1 {
    margin: 0 0 0.5rem 0;
    font-size: 3rem;
    line-height: 1;
    color: var(--text);
}

.hero p {
    margin: 0;
    max-width: 58ch;
    color: var(--muted);
    font-size: 1.05rem;
}

.metric {
    border: 1px solid var(--border);
    background: var(--card);
    border-radius: 22px;
    padding: 1rem 1.1rem;
    box-shadow: 0 14px 40px rgba(16, 35, 63, 0.05);
}

.metric-value {
    display: block;
    color: var(--text);
    font-weight: 800;
    font-size: 1.35rem;
}

.metric-label {
    color: var(--muted);
    font-size: 0.92rem;
}

.support-button {
    position: fixed;
    bottom: 28px;
    right: 28px;
    background: linear-gradient(135deg, var(--accent-2), var(--accent));
    color: white !important;
    padding: 14px 20px;
    border-radius: 999px;
    font-size: 16px;
    font-weight: 700;
    text-decoration: none;
    box-shadow: 0 18px 40px rgba(37, 99, 235, 0.28);
    z-index: 999;
}

.support-button:hover {
    transform: translateY(-1px);
    filter: brightness(1.02);
}

.product-card {
    height: 100%;
    border: 1px solid var(--border);
    padding: 1.25rem;
    border-radius: 22px;
    background: linear-gradient(180deg, rgba(255,255,255,0.96), rgba(245,248,255,0.92));
    box-shadow: 0 14px 40px rgba(16, 35, 63, 0.06);
}

.product-card h3 {
    margin: 0 0 0.35rem 0;
    color: var(--text);
}

.product-card p {
    color: var(--muted);
}

</style>
""",
unsafe_allow_html=True)

st.markdown(
    """
    <div class="hero">
        <span class="hero-kicker">Curated shopping, faster support</span>
        <h1>MiniStore</h1>
        <p>Browse a sharper storefront, compare featured products, and jump straight into the assistant for recommendations, delivery help, and order tracking.</p>
    </div>
    """,
    unsafe_allow_html=True
)

top_left, top_middle, top_right = st.columns(3)
with top_left:
    st.markdown('<div class="metric"><span class="metric-value">6 products</span><span class="metric-label">featured in the catalog</span></div>', unsafe_allow_html=True)
with top_middle:
    st.markdown('<div class="metric"><span class="metric-value">24/7 assistant</span><span class="metric-label">for product and order questions</span></div>', unsafe_allow_html=True)
with top_right:
    st.markdown('<div class="metric"><span class="metric-value">Fast checkout</span><span class="metric-label">simple browsing experience</span></div>', unsafe_allow_html=True)

st.link_button("🤖 Open MiniStore AI Assistant", "/assistant")

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
                <b>Price:</b> ${product['price']:.2f}
            </div>
            """,
            unsafe_allow_html=True
        )

st.link_button("🤖 Ask MiniStore AI", "/assistant")