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
    --bg: #f6efe6;
    --card: rgba(255, 252, 247, 0.88);
    --text: #14213d;
    --muted: #667085;
    --accent: #0f766e;
    --accent-2: #c0562b;
    --accent-3: #1d4ed8;
    --border: rgba(20, 33, 61, 0.08);
}

body {
    background:
        radial-gradient(circle at top left, rgba(15, 118, 110, 0.12), transparent 30%),
        radial-gradient(circle at top right, rgba(192, 86, 43, 0.14), transparent 28%),
        linear-gradient(180deg, #fffaf4 0%, #f2e9dd 100%);
    color: var(--text);
}

.stApp {
    background: transparent;
}

.hero {
    padding: 2rem 2.2rem;
    border: 1px solid var(--border);
    border-radius: 28px;
    background:
        linear-gradient(135deg, rgba(255, 252, 247, 0.94), rgba(249, 244, 236, 0.84)),
        linear-gradient(135deg, rgba(15, 118, 110, 0.08), rgba(192, 86, 43, 0.08));
    box-shadow: 0 24px 80px rgba(20, 33, 61, 0.08);
}

.hero-kicker {
    display: inline-block;
    padding: 0.35rem 0.8rem;
    border-radius: 999px;
    background: rgba(15, 118, 110, 0.14);
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
    box-shadow: 0 14px 40px rgba(20, 33, 61, 0.05);
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
    background: linear-gradient(135deg, var(--accent-2), var(--accent-3));
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
    filter: brightness(1.06);
}

.product-card {
    height: 100%;
    border: 1px solid var(--border);
    padding: 1.25rem;
    border-radius: 22px;
    background:
        linear-gradient(180deg, rgba(255, 252, 247, 0.96), rgba(249, 244, 236, 0.92));
    box-shadow: 0 14px 40px rgba(20, 33, 61, 0.06);
    position: relative;
    overflow: hidden;
}

.product-card::before {
    content: "";
    position: absolute;
    inset: 0 auto auto 0;
    width: 100%;
    height: 4px;
    background: linear-gradient(90deg, var(--accent), var(--accent-2));
}

.product-card h3 {
    margin: 0 0 0.35rem 0;
    color: var(--text);
}

.product-card p {
    color: var(--muted);
}

a[data-testid="stLinkButton"] {
    border-radius: 999px;
    border: 1px solid rgba(20, 33, 61, 0.12);
    background: linear-gradient(135deg, rgba(15, 118, 110, 0.08), rgba(192, 86, 43, 0.08));
    color: var(--text);
}

a[data-testid="stLinkButton"]:hover {
    border-color: rgba(20, 33, 61, 0.18);
    transform: translateY(-1px);
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