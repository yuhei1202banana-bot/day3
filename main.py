import streamlit as st

# =============================
# Page Settings
# =============================
st.set_page_config(page_title="Vietnam Shop Website", layout="wide")

# =============================
# Custom CSS - Stylish Modern Theme
# =============================
custom_css = """
<style>
/* Global Background Gradient */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(to bottom right, #f6f2ec, #f0e7dd);
    font-family: 'Helvetica', sans-serif;
}

/* Main Header */
.header-box {
    background: #ff8a3d;
    padding: 40px;
    border-radius: 16px;
    text-align: center;
    color: white;
    font-size: 36px;
    font-weight: bold;
    letter-spacing: 1px;
    margin-bottom: 35px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
}

/* Content Blocks */
.block {
    background: #ffffffdd;
    padding: 28px;
    border-radius: 18px;
    margin-bottom: 28px;
    backdrop-filter: blur(4px);
    box-shadow: 0 4px 18px rgba(0,0,0,0.1);
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}

.block:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.15);
}

/* Titles */
.block-title {
    color: #ff8a3d;
    font-size: 26px;
    font-weight: bold;
    margin-bottom: 10px;
}

/* Footer */
.footer {
    text-align: center;
    color: #666;
    margin-top: 35px;
    padding: 20px;
    font-size: 14px;
}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# =============================
# Header
# =============================
st.markdown('<div class="header-box">Welcome to Our Shop in Vietnam</div>', unsafe_allow_html=True)

# =============================
# Main Content Blocks
# =============================
st.markdown('<div class="block">', unsafe_allow_html=True)
st.markdown('<div class="block-title">About Our Shop</div>', unsafe_allow_html=True)
st.write(
    "We offer high-quality products at fair and honest prices. "
    "Our shop welcomes both local customers and international visitors with warm service and reliability."
)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="block">', unsafe_allow_html=True)
st.markdown('<div class="block-title">Why Choose Us?</div>', unsafe_allow_html=True)
st.write("""
• Transparent and fair pricing  
• Friendly and reliable staff  
• High-quality, trusted products  
• Smooth English communication  
• Support for tourists and local customers  
""")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="block">', unsafe_allow_html=True)
st.markdown('<div class="block-title">Catalog</div>', unsafe_allow_html=True)
st.write("""
Here is our text-based catalog (image-free version):
- Product A — Description / Price  
- Product B — Description / Price  
- Product C — Description / Price  
- Custom orders available upon request  
""")
st.markdown('</div>', unsafe_allow_html=True)

# =============================
# Google Maps Block
# =============================
st.markdown('<div class="block">', unsafe_allow_html=True)
st.markdown('<div class="block-title">Find Us on Google Maps</div>', unsafe_allow_html=True)

st.components.v1.html(
    """
    <iframe 
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3724.656208648692!2d105.84117037588606!3d21.00638298884039!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3135ab76fd6e6cdf%3A0xb68ab8d9ac7a5905!2sHanoi!5e0!3m2!1sen!2s!4v1700000000000"
        width="100%" height="350" style="border:0;" allowfullscreen="" loading="lazy">
    </iframe>
    """,
    height=370
)

st.markdown('</div>', unsafe_allow_html=True)

# =============================
# Developed in Japan
# =============================
st.markdown('<div class="block">', unsafe_allow_html=True)
st.markdown('<div class="block-title">Developed in Japan</div>', unsafe_allow_html=True)
st.write(
    "This website was fully designed and developed by a Japanese engineer. "
    "We deliver clean UI, stable performance, and trustworthy development quality."
)
st.markdown('</div>', unsafe_allow_html=True)

# =============================
# Footer
# =============================
st.markdown('<div class="footer">© 2025 Vietnam Shop Website — Developed in Japan</div>', unsafe_allow_html=True)