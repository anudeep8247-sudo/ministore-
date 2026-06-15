import streamlit as st
from products import products

st.set_page_config(
    page_title="MiniStore Assistant",
    page_icon="🤖",
    layout="wide"
)

st.markdown(
    """
    <style>
    :root {
        --panel: rgba(9, 18, 31, 0.78);
        --panel-2: rgba(15, 28, 47, 0.82);
        --text: #ecf4ff;
        --muted: #a7bbd8;
        --accent: #52d6c5;
        --border: rgba(255,255,255,0.1);
    }

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(82, 214, 197, 0.18), transparent 28%),
            radial-gradient(circle at top right, rgba(124, 156, 255, 0.16), transparent 30%),
            linear-gradient(180deg, #06101d 0%, #0d1a2e 100%);
        color: var(--text);
    }

    .assistant-shell {
        padding: 2rem;
        border-radius: 28px;
        border: 1px solid var(--border);
        background: linear-gradient(180deg, var(--panel), var(--panel-2));
        box-shadow: 0 30px 90px rgba(0,0,0,0.28);
    }

    .assistant-kicker {
        display: inline-block;
        padding: 0.35rem 0.8rem;
        border-radius: 999px;
        background: rgba(82, 214, 197, 0.14);
        color: var(--accent);
        font-size: 0.84rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }

    .assistant-shell h1 {
        margin: 0 0 0.5rem 0;
        color: var(--text);
    }

    .hint-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 0.8rem;
        margin: 1.2rem 0 1.6rem;
    }

    .hint-chip {
        padding: 0.9rem 1rem;
        border-radius: 18px;
        border: 1px solid var(--border);
        background: rgba(255,255,255,0.05);
        color: var(--text);
    }

    .assistant-note {
        margin-top: 0.75rem;
        color: var(--muted);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.link_button("← Back to MiniStore", "/")

st.markdown(
    """
    <div class="assistant-shell">
        <span class="assistant-kicker">MiniStore AI</span>
        <h1>Shopping support, without the wait</h1>
        <p>Ask about products, delivery, refunds, returns, payments, or order status. The assistant is tuned for quick, specific answers.</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="hint-grid">
        <div class="hint-chip">Recommend a product for me</div>
        <div class="hint-chip">What is the delivery time?</div>
        <div class="hint-chip">Tell me the return policy</div>
        <div class="hint-chip">Check my order status</div>
    </div>
    """,
    unsafe_allow_html=True
)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi! I’m MiniStore AI. Ask me about products, orders, refunds, delivery, or recommendations."
        }
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input("Ask me anything about MiniStore...")


def get_response(user_input):
    text = user_input.lower()

    if any(word in text for word in ["recommend", "suggest", "best"]):
        return (
            "I’d start with the Smart Watch ($129.99) if you want a daily-use upgrade, "
            "or the Wireless Headphones ($79.99) for the best balance of value and quality."
        )

    for product in products:
        if product["name"].lower() in text:
            return (
                f"{product['name']} costs ${product['price']:.2f}.\n\n"
                f"Category: {product['category']}\n\n"
                f"{product['description']}"
            )

    if any(word in text for word in ["delivery", "shipping"]):
        return "Standard delivery takes 3-5 business days. Express delivery takes 1-2 business days."

    if "refund" in text:
        return "Refunds are processed within 5-7 business days after approval."

    if "return" in text:
        return "Products can be returned within 30 days if unused and in original packaging."

    if any(word in text for word in ["payment", "upi", "card"]):
        return "We accept UPI, Credit Cards, Debit Cards, Net Banking, and PayPal."

    if "order" in text:
        return (
            "Demo Order Status:\n\n"
            "Order #MS1024\n"
            "Status: In Transit 🚚\n"
            "Expected Delivery: 2 Days"
        )

    return "I can help with products, recommendations, delivery, refunds, returns, payments, and order tracking."


if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.write(prompt)

    response = get_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.write(response)

st.markdown(
    '<div class="assistant-note">Tip: try asking for a recommendation or the return policy to see the assistant respond instantly.</div>',
    unsafe_allow_html=True
)
