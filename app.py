import streamlit as st

st.set_page_config(page_title="Xhamia e Bardhë – Hotël", page_icon="🕌", layout="centered")

st.markdown("""
<style>
.title{ text-align:center; font-size:36px; font-weight:800; margin-top:10px; }
.card{ background:#fff; padding:16px; border-radius:14px; margin:10px 0;
       box-shadow:0 6px 18px rgba(0,0,0,.08); }
.small{ opacity:.8; }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🕌 Xhamia e Bardhë – Hotël</div>", unsafe_allow_html=True)
st.markdown("<div class='small' style='text-align:center;'>Faqe zyrtare • Njoftime • Oraret • Kontakt</div>", unsafe_allow_html=True)
st.write("")

st.markdown("<div class='card'><b>📢 Njoftime</b><br>Së shpejti do të publikohen njoftime nga këshilli i xhamisë.</div>", unsafe_allow_html=True)
st.markdown("<div class='card'><b>⏰ Oraret e Namazit</b><br>Oraret do të përditësohen rregullisht.</div>", unsafe_allow_html=True)
st.markdown("<div class='card'><b>📍 Vendndodhja</b><br>Hotël – Lipkovë</div>", unsafe_allow_html=True)
st.markdown("<div class='card'><b>📞 Kontakt</b><br>Këshilli i Xhamisë së Bardhë</div>", unsafe_allow_html=True)

st.markdown("<hr>")
st.markdown("<center>© Xhamia e Bardhë – Hotël</center>", unsafe_allow_html=True)
