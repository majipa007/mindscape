import streamlit as st
from streamlit_player import st_player
# from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage
from streamlit_chat import message
from langchain_community.chat_models import ChatOpenAI

key = st.secrets["key"]
chatllm = ChatOpenAI(openai_api_key=key, temperature=0.8, model='gpt-3.5-turbo')
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


def ans(inp, opt, ch):
    response = chatllm([
        SystemMessage(
            content=f"Act as a professional psychiatrist whos name is Aimee with 30 years of experience "
                    f"the patient has {opt} condition"
                    f"and this is what the patient has to say {inp}"
                    f"respond in a responsible manner empathizesing the problem liberal mindedly without any judgement and making it motivative"
                    f"in about {ch} word length"
                    f" making it friendly wihtout revealing that you have 30 years of experience"
                    f"and in any case of a serious condidition always recommend to meet a counceler"
                    f"and suggest them to book an appointment using our app")
    ])
    content = response.content
    return content


def chat_bot():
    img_url = "peace.png"
    st.markdown("<h3 style='text-align: center;'>ONE BREATH AT A TIME!</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>MINDSCAPE</h1>", unsafe_allow_html=True)
    st.image(img_url, use_column_width=True)
    st.markdown("<h3 style='text-align: center;'>' A REHABILITATIVE SITE FOR ANXIETY '</h1>",
                unsafe_allow_html=True)

    st.write("\n\n\n")
    # st.markdown("<h3 style='text-align: center;'>CONDITION</h1>", unsafe_allow_html=True)

    st.markdown("<h3 style='text-align: center;'>HI, THIS IS AIMEE!</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>HOW CAN I HELP YOU?</h3>", unsafe_allow_html=True)
    option = st.selectbox('',
                          ('Generalized anxiety', 'Phobia disorder', 'Traumatic anxiety', 'PTSD induced anxiety',
                           'Social anxiety')
                          )
    st.write("")
    st.markdown("<h5 style='text-align: center;'>RESPONSE MODE</h5>", unsafe_allow_html=True)

    length = st.selectbox('',
                          ('Short', 'Medium', 'Long', 'Counseling')
    )

    if length == 'Short':
        ch = 30

    elif length == 'Medium':
        ch = 100
    elif length == 'Long':
        ch = 200
    else:
        ch = 500

    if 'generated' not in st.session_state:
        st.session_state['generated'] = []

    if 'past' not in st.session_state:
        st.session_state['past'] = []

    def get_text():
        input_text = st.text_input("", key="input")
        return input_text

    user_input = get_text()

    if user_input:
        output = ans(user_input, option, ch)
        # store output
        st.session_state.past.append(user_input)
        st.session_state.generated.append(output)

    if st.session_state["generated"]:
        for i in range(len(st.session_state['generated']) - 1, -1, -1):
            message(st.session_state['generated'][i], key=str(i))
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')


def nature():
    st.title("Natural sounds at your finger tips")
    v1 = "https://youtu.be/wKnS8VPxpHI?si=w1hWmjOQ4R3AoiEZ"
    v2 = "https://youtu.be/oA_LD4xMg08?si=kNKP9HR0ajpomvMp"
    v3 = 'https://youtu.be/y615vOsiG5w?si=hG6iM40l3cQTwadn'
    v4 = 'https://youtu.be/CpS5Ex1Wx-4?si=lQeprNa605mnc0-E'
    st_player(v1)
    st_player(v2)
    st_player(v3)
    st_player(v4)


def calm():
    st.title("Calm songs at your finger tips")
    v1 = 'https://youtube.com/playlist?list=PL7v1FHGMOadDghZ1m-jEIUnVUsGMT9jbH&si=TISmC1ATW9IS_wK0'
    v2 = "https://youtu.be/UVQREpxmN_U?si=2bm7CXkFvJqlLw9P"
    v3 = 'https://youtu.be/GPEc2LHhmwA?si=vd-fN1Wpmx-qhWBk'
    v4 = 'https://youtu.be/d_HlPboLRL8?si=fnW-gYdfYOwiaZsN'
    st_player(v1)
    st_player(v2)
    st_player(v3)
    st_player(v4)


def motivation():
    st.title("Motivative songs at your finger tips")
    v1 = "https://www.youtube.com/watch?v=UBBHpoW3AKA&list=PLmgutjZvzLyryoakC3VAlDptXy4ChQGC3"
    v2 = "https://youtube.com/playlist?list=PLIdy0pK8PQg__cryoPjU_rwvlhXw3gTG3&si=MTeOmjcACEGA0P8w"
    st_player(v1)
    st_player(v2)


def freq():
    st.title("Frequency-specific music at your finger tips")
    v2 = "https://youtu.be/NACJwvt1dHI?si=rGPWwyfgzTN-8T79"
    v3 = 'https://youtu.be/fD5d8Q-Kzew?si=Y45zDKsJOoDmu7ju'
    st_player(v2)
    st_player(v3)


def sleep():
    v1 = "https://www.youtube.com/watch?v=mPZkdNFkNps"
    v2 = "https://www.youtube.com/watch?v=qBAPsQkS8QI"

    st.title("Sleep music for you")

    st.subheader("Rain and thunder sounds")
    st_player(v1)

    st.subheader("Wind")
    st_player(v2)


def meditation():
    video_url = "https://www.youtube.com/watch?v=nlEoLYREbXo"
    st.header("Meditation for you")
    st.subheader("5 minutes of meditation")
    st_player(video_url)
    video_url1 = "https://youtu.be/O-6f5wQXSu8?si=DF7aX_rkTN4uzhWA"
    st.subheader("10 minutes of meditation")
    st_player(video_url1)
    video_url2 = "https://youtu.be/V8EsdlI-eos?si=akl-7JJdsapUha0a"
    st.subheader("15 minutes of meditation")
    st_player(video_url2)
    video_url3 = "https://youtu.be/mK-kGgypeI0?si=VoiQ7dj_maiKoheN"
    st.subheader("20 minutes of meditation")
    st_player(video_url3)

    st.header("YOGA")
    video_url4 = "https://youtu.be/eqH9Dp8r14A?si=vddwpNZxPJPh9Sf_"
    st_player(video_url4)
    video_url5 = "https://youtu.be/hJbRpHZr_d0?si=GxyAGUrwTuvnFlVv"
    st_player(video_url5)


def relax():
    video_url = "https://youtu.be/tEmt1Znux58?si=_pbUi9ATMrFNO7CA"
    st.header("Breathing Exercises for you")
    st_player(video_url)
    video_url2 = "https://youtube.com/watch?v=30VMIEmA114&feature=shared"
    st_player(video_url2)
