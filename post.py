import streamlit as st


def post_page():
    st.header('My posts')
    image_1, detail_1 = st.columns(2)
    with image_1:
        st.image('Resources/House1.jpg')
    with detail_1:
        st.subheader('Sandy, Oregon')
        st.write('Located on a secluded plot of 23 acres, this tiny home provides you with your own private view of'
                 ' Oregon’s Mount Hood. With cedar furnishings surrounded by lush greenery, this tiny house serves'
                 ' up major cozy vibes. ')
        st.metric(label='Attendance', value='10', delta='1%')

    image_2, detail_2 = st.columns(2)
    with image_2:
        st.image('Resources/House2.jpg')
    with detail_2:
        st.subheader('Wellsville, Pennsylvania')
        st.write('Complete with a patio, porch, grill and hammock, this tiny home in Wellsville, Pennsylvania has'
                 ' all the ingredients to help you enjoy the great outdoors.')
        st.metric(label='Attendance', value='13', delta='5%')

    image_3, detail_3 = st.columns(2)
    with image_3:
        st.image('Resources/House3.jpg')
    with detail_3:
        st.subheader('Anacortes, Washington')
        st.write('This tiny home on Guemes Island is beautifully curated by local artists and craftsmen. After your'
                 ' voyage is over, fall asleep peacefully in the elevated loft.')
        st.metric(label='Attendance', value='14', delta='-4%')
