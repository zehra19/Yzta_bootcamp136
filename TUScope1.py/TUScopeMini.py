# TUScopeMini.py
import streamlit as st
import json

with open("veri7bolum.json", "r", encoding="utf-8") as f:
    veri = json.load(f)

st.set_page_config(page_title="TUScope Mini", page_icon="📚", layout="wide")

st.title("📚 TUScope Mini - 7 Bölüm 2 Soru")
st.write("Çalışmak istediğin bölümü seç ve iki soruyu çöz!")

bolum = st.selectbox("📌 Bölüm Seç:", list(veri.keys()))

if bolum:
    st.subheader(f"📖 {bolum} Spot Bilgiler")
    for spot in veri[bolum]["spot_bilgiler"]:
        st.markdown(f"- {spot}")

    st.subheader(f"❓ {bolum} Sorular")
    dogru = 0
    for i, soru in enumerate(veri[bolum]["sorular"]):
        st.markdown(f"**{i+1}. {soru['soru']}** ({soru['yil']})")
        cevap = st.radio("Cevabınızı seçin:", soru["secenekler"], key=f"{bolum}_{i}")
        if cevap == soru["cevap"]:
            st.success("✅ Doğru!")
            dogru += 1
        elif cevap != "":
            st.error(f"❌ Yanlış! Doğru cevap: {soru['cevap']}")

    st.write(f"🎯 **Doğru Sayısı: {dogru}/2**")
