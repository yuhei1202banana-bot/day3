import streamlit as st

# =============================
# Page Settings
# =============================
st.set_page_config(page_title="Vietnam Shop Website", layout="wide")

# =============================
# Custom CSS
# =============================
custom_css = """
<style>
body {
    background: #fafafa;
    font-family: Arial, sans-serif;
}

header {
    background: #ff7f32;
    color: white;
    padding: 25px;
    text-align: center;
    font-size: 30px;
    border-radius: 8px;
    margin-bottom: 25px;
}

.block {
    background: #ffffff;
    padding: 22px;
    border-radius: 12px;
    margin-bottom: 22px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.07);
}

h2 {
    color: #ff7f32;
    margin-bottom: 10px;
}

footer {
    text-align: center;
    padding: 15px;
    margin-top: 30px;
    color: #777;
    font-size: 13px;
}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)


# =============================
# Header
# =============================
st.markdown(
    "<header>Welcome to Our Shop in Vietnam</header>",
    unsafe_allow_html=True
)


# =============================
# Main Content
# =============================
st.markdown('<div class="block">', unsafe_allow_html=True)
st.markdown("## About Our Shop")
st.write(
    "We provide high-quality products at fair prices. "
    "Our shop is located in Vietnam and we welcome both locals and tourists."
)
st.markdown('</div>', unsafe_allow_html=True)


st.markdown('<div class="block">', unsafe_allow_html=True)
st.markdown("## Why Choose Us?")
st.write("""
• Transparent pricing  
• Friendly service  
• Reliable quality  
• Easy communication in English  
""")
st.markdown('</div>', unsafe_allow_html=True)


st.markdown('<div class="block">', unsafe_allow_html=True)
st.markdown("## Catalog (Text Only)")
st.write("""
- Product A — Description / Price  
- Product B — Description / Price  
- Product C — Description / Price  
- Custom orders available  
""")
st.markdown('</div>', unsafe_allow_html=True)


# =============================
# Google Maps Block
# =============================
st.markdown('<div class="block">', unsafe_allow_html=True)
st.markdown("## Find Us on Google Maps")

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
st.markdown("## Developed in Japan")
st.write(
    "This website was fully designed and developed by a Japanese engineer. "
    "We ensure clean design, stable performance, and professional communication."
)
st.markdown('</div>', unsafe_allow_html=True)


# =============================
# Footer
# =============================
st.markdown('<footer>© 2025 Vietnam Shop Website — Developed in Japan</footer>', unsafe_allow_html=True)