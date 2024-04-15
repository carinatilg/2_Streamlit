import streamlit as st
import read_data 

person_dict = read_data.load_person_data()
person_names = read_data.get_person_list(person_dict)
# Eine Überschrift der ersten Ebene
st.write("# EKG APP")

# Eine Überschrift der zweiten Ebene
st.write("## Versuchsperson auswählen")

# Eine Auswahlbox
st.session_state.current_user = st.selectbox(
    'Versuchsperson',
    options = person_names, key="sbVersuchsperson")