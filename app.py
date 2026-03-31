import streamlit as st

st.set_page_config(
    page_title="Bank Churn MLP",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 Predicting Customer Churn Using MLP")
st.markdown("An end-to-end deep learning project using PyTorch on banking data.")
st.divider()

# Read and display the exported notebook
with open("AppliedMLP.html", "r", encoding="utf-8") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=8000, scrolling=True)
```

Save it as `app.py`.

---

## Step 3 — Your GitHub repo should have these 3 files
```
your-repo/
├── app.py
├── AppliedMLP.html        ← upload this (downloaded in Step 1)
└── requirements.txt       ← create this with the content below
```

**requirements.txt** contents:
```
streamlit