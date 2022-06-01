import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def sentiment_score(sentence):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)

    print(f'Overall sentiment dictionary: {sentiment_dict}')
    polarity = (sentiment_dict["neg"]*100, sentiment_dict["pos"]*100)
    print(f'Neutral: {sentiment_dict["neu"]*100}')
    print(f'Negative: {sentiment_dict["neg"]*100}')
    print(f'Positive: {sentiment_dict["pos"]*100}')
    return polarity


def feedback_page():
    st.header('Recent guests')
    with st.expander('Sandy, Oregon'):
        user, detail = st.columns((2, 1))
        with user:
            st.image('Resources/batman.jpg')
        with detail:
            st.header('Batman')
            st.subheader('Length of stay: 2 days')
            st.subheader('Feedback')
            host_comment_1 = st.text_input('Your experience with this guest', key='BATMAN')
            if st.button('Check discount', key='batman'):
                sentiment_comment = sentiment_score(host_comment_1)
                if sentiment_comment[1] > 40:
                    st.info('20% off ticket delivered!')
                elif sentiment_comment[0] > 50:
                    st.warning('Sorry for that experience! We will talk with this guest')

    with st.expander('Wellsville, Pennsylvania'):
        user_2, detail_2 = st.columns((2, 1))
        with user_2:
            st.image('Resources/Spider-Man.jpg')
        with detail_2:
            st.header('Spiderman')
            st.subheader('Length of stay: 4 days')
            st.subheader('Feedback')
            host_comment_2 = st.text_input('Your experience with this guest', key='SPIDERMAN')
            if st.button('Check discount', key='SPIDERMAN'):
                sentiment_comment = sentiment_score(host_comment_2)
                if sentiment_comment[1] > 40:
                    st.info('20% off ticket delivered!')
                elif sentiment_comment[0] > 50:
                    st.warning('Sorry for that experience! We will talk with this guest')
