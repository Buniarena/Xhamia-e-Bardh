import streamlit as st
from io import BytesIO
import textwrap

# PDF (ReportLab)
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

# OPTIONAL: lexo rregulloren nga .docx nëse e ngarkon në repo
try:
    from docx import Document
except Exception:
    Document = None


# ===================== SETTINGS =====================
st.set_page_config(
    page_title="Xhamia e Bardhë – Rregullorja",
    page_icon="🕌",
    layout="centered"
)

st.markdown("""
<style>
.main { background: #ffffff; }
.block-container { padding-top: 18px; padding-bottom: 30px; max-width: 880px; }
h1,h2,h3 { letter-spacing: 0.2px; }
.card {
  border: 1px solid #e5e7eb;
  border-radius: 14px;
  padding: 18px 18px;
  background: #fafafa;
}
.small {
  color: #6b7280;
  font-size: 13px;
}
</style>
""", unsafe_allow_html=True)


# ===================== DATA: RREGULLORJA =====================
DEFAULT_RREGULLORE = """
Neni 1 – Qëllimi
Kjo rregullore përcakton mënyrën e funksionimit, vendimmarrjes dhe përgjegjësitë e Këshillit të Xhamisë së Bardhë.

Neni 2 – Përbërja e Këshillit
Këshilli përbëhet nga anëtarë të zgjedhur sipas rregullave dhe traditës së xhamisë.

Neni 3 – Mbledhjet
Mbledhjet thirren nga Kryetari dhe janë të vlefshme kur merr pjesë shumica e anëtarëve.

Neni 4 – Vendimmarrja
Vendimet merren me shumicë votash dhe regjistrohen në procesverbal.

Neni 5 – Transparenca
Këshilli informon rregullisht xhematin për vendimet dhe aktivitetet.

Neni 6 – Financat
Menaxhimi financiar bëhet me përgjegjësi dhe transparencë.

Neni 7 – Etika dhe Disiplina
Anëtarët janë të obliguar të respektojnë etikën islame.

Neni 8 – Fuqia Juridike
Kjo rregullore hyn në fuqi me miratimin e Këshillit të Xhamisë.
""".strip()


def load_rregullore_from_docx(path: str) -> str | None:
    """Lexon tekstin nga një docx në repo (p.sh. 'rregullorja.docx')"""
    if Document is None:
        return None
    try:
        doc = Document(path)
        parts = []
        for p in doc.paragraphs:
            t = (p.text or "").strip()
            if t:
                parts.append(t)
        text = "\n".join(parts).strip()
        return text if text else None
    except Exception:
        return None


# Nëse e ngarkon docx në repo me emrin "rregullorja.docx", app-i do e lexojë automatikisht.
DOCX_PATH = "rregullorja.docx"
rregullore_text = load_rregullore_from_docx(DOCX_PATH) or DEFAULT_RREGULLORE


# ===================== PDF BUILDER =====================
def make_pdf_bytes(title: str, body_text: str) -> bytes:
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    left = 2.0 * cm
    right = 2.0 * cm
    top = 2.0 * cm
    bottom = 2.0 * cm

    y = height - top

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(left, y, title)
    y -= 1.0 * cm

    c.setFont("Helvetica", 11)

    # Wrap lines (afërsisht për A4)
    max_chars = 95  # mund ta rrisësh/ulësh nëse do
    paragraphs = [p.strip() for p in body_text.split("\n")]

    for p in paragraphs:
        if not p:
            y -= 0.35 * cm
            continue

        # Nëse duket si titull "Neni ...", bëje bold
        is_neni = p.lower().startswith("neni ")
        if is_neni:
            c.setFont("Helvetica-Bold", 11)
        else:
            c.setFont("Helvetica", 11)

        lines = textwrap.wrap(p, width=max_chars)
        for line in lines:
            if y < bottom:
                c.showPage()
                y = height - top
                c.setFont("Helvetica", 11)
            c.drawString(left, y, line)
            y -= 0.5 * cm

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer.getvalue()


# ===================== UI =====================
st.title("🕌 Xhamia e Bardhë")
st.markdown('<div class="small">Rregullorja e Këshillit – e lexueshme edhe në telefon, me shkarkim PDF.</div>', unsafe_allow_html=True)
st.markdown("---")

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("📜 Rregullorja")
st.markdown(rregullore_text.replace("\n", "\n\n"))
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

pdf_bytes = make_pdf_bytes("Rregullorja e Këshillit – Xhamia e Bardhë", rregullore_text)

st.download_button(
    label="⬇️ Shkarko Rregulloren (PDF)",
    data=pdf_bytes,
    file_name="Rregullorja_Xhamia_e_Bardhe.pdf",
    mime="application/pdf",
)

st.markdown('<div class="small">Nëse do, mund ta ngarkosh në repo edhe si <b>rregullorja.docx</b> që ta lexojë automatikisht.</div>', unsafe_allow_html=True)
