import streamlit as st
import load_person_data from read_data

# Eine Überschrift der ersten Ebene
st.write("# EKG APP")

# Eine Überschrift der zweiten Ebene
st.write("## Versuchsperson auswählen")

# Eine Auswahlbox
current_user = st.selectbox(
    'Versuchsperson',
    options = ["Nutzer1", "Nutzer2"], key="sbVersuchsperson")

st.button("hit me")

print(read_data)