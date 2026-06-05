import streamlit as st
from PyPDF2 import PdfReader
from medical_dictionary import medical_terms

st.set_page_config(
    page_title="Biomedical Report Simplifier",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 Biomedical Report Simplifier")
st.write(
    "Upload a medical report or paste medical text to get a simpler version."
)

# Sidebar
st.sidebar.header("About")
st.sidebar.write(
    "This application converts complex biomedical terms into simple English."
)

# Function to simplify text
def simplify_text(text):

    new_text = text
    detected_terms = []

    for term, meaning in medical_terms.items():

        if term.lower() in text.lower():

            detected_terms.append((term, meaning))

            new_text = new_text.replace(term, meaning)
            new_text = new_text.replace(
                term.capitalize(),
                meaning.capitalize()
            )

    return new_text, detected_terms


# Upload PDF
uploaded_file = st.file_uploader(
    "Upload a PDF report",
    type=["pdf"]
)

text = ""

if uploaded_file:

    reader = PdfReader(uploaded_file)

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text

else:

    text = st.text_area(
        "Or paste medical text here",
        height=200
    )

# Simplify button
if st.button("Simplify"):

    if text.strip() == "":
        st.warning("Please upload a report or enter text.")

    else:

        simplified_text, terms_found = simplify_text(text)

        st.subheader("Results")

        col1, col2 = st.columns(2)

        with col1:
            st.write("### Original Text")
            st.text_area(
                "",
                text,
                height=300
            )

        with col2:
            st.write("### Simplified Text")
            st.text_area(
                "",
                simplified_text,
                height=300
            )

        st.write("### Statistics")

        word_count = len(text.split())

        st.write(f"Total Words: {word_count}")
        st.write(f"Medical Terms Found: {len(terms_found)}")

        st.write("### Detected Terms")

        if len(terms_found) > 0:

            for term, meaning in terms_found:

                st.write(
                    f"{term} → {meaning}"
                )

        else:

            st.write(
                "No medical terms were detected."
            )

        st.download_button(
            "Download Simplified Report",
            simplified_text,
            file_name="simplified_report.txt"
        )