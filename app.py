import streamlit as st
import requests
import mods

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []
placeholder = st.empty()

st.sidebar.image("peace.png")
st.sidebar.markdown("<h1 style='text-align: center;'>MINDSCAPE</h1>", unsafe_allow_html=True)
chat = st.sidebar.button(":woman: Aimee the Chat-Bot")
medi = st.sidebar.button(":person_in_lotus_position: Meditation / Yoga")
with st.sidebar:
    with st.expander(":musical_note: Music"):
        calm = st.button(":ocean: calm")
        motivative = st.button(":muscle: motivational")
        nature = st.button(":sunny: nature")
        freq = st.button(":bell: frequency-specific")
        slee = st.button(":zzz: sleep")

relx = st.sidebar.button(":peace_symbol: Relaxation Exercises")
appo = st.sidebar.button(":pushpin: Meet a counselor")


if medi:
    placeholder.empty()
    mods.meditation()

if slee:
    placeholder.empty()
    mods.sleep()

if calm:
    placeholder.empty()
    mods.calm()

if motivative:
    placeholder.empty()
    mods.motivation()

if nature:
    placeholder.empty()
    mods.nature()

if freq:
    placeholder.empty()
    mods.freq()

if relx:
    placeholder.empty()
    mods.relax()

if appo:
    with st.form('form1'):
        st.title("Schedule an Appointment")
        st.write("Please fill out the form below to schedule an appointment.")
        name = st.text_input("Name:")
        phno = st.text_input("Phone:")
        date = st.date_input("Appointment Date:")
        time = st.selectbox("Appointment Time:", (
            "10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM", "3:00 PM", "4:00 PM", "5:00 PM", "6:00 PM"))
        reason = st.text_area("Reason for Appointment:")


        def send_telegram_message(a, b, c, d, e):
            text = f"name:{a}\nphone no:{b}\ndate:{c}\ntime:{d}\nreason:{e}"
            token = "6763513952:AAGuEmIhIDmxFBxd1ZFArsRZmGrTdZGZOoo"
            chat_id = "5607653518"
            url_req = "https://api.telegram.org/bot" + token + "/sendMessage"
            data = {'chat_id': chat_id, 'text': text}
            requests.post(url_req, data)


        submit = st.form_submit_button(on_click=send_telegram_message, args=(name, phno, date, time, reason))

if medi == False and slee == False and calm == False and motivative == False and nature == False and freq == False and relx == False and appo == False :
    placeholder.empty()
    mods.chat_bot()
