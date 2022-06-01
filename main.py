import streamlit as st
import hydralit_components as hc

# Custom imports
from feedback import feedback_page
from post import post_page

menu_data = [
    {'icon': "bi bi-arrow-bar-up", 'label': "Feedback"}
]


def main():
    # --------------------------------
    # Global variables
    # --------------------------------
    transport_option = None
    # --------------------------------
    # Session state
    # --------------------------------
    if 'auth_host' not in st.session_state:
        st.session_state.auth_host = False
    if 'auth_guest' not in st.session_state:
        st.session_state.auth_guest = False
    # --------------------------------
    # Side Bar
    # --------------------------------
    side = st.sidebar
    side.image('Resources/logo.png')

    side.header('Log in')
    user = side.text_input('User')
    pwd = side.text_input('Password', type='password')
    if user and pwd:
        if side.button('Enter'):
            if user == 'host' and pwd == 'host':
                st.session_state.auth_host = True
                st.session_state.auth_guest = False
            elif user == 'guest' and pwd == 'guest':
                st.session_state.auth_host = False
                st.session_state.auth_guest = True

    if not st.session_state.auth_host and not st.session_state.auth_guest:
        st.header('Trending')
        image_1, detail_1 = st.columns(2)
        with image_1:
            st.image('Resources/House1.jpg')
        with detail_1:
            st.subheader('Sandy, Oregon')
            st.write('Located on a secluded plot of 23 acres, this tiny home provides you with your own private view of'
                     ' Oregon’s Mount Hood. With cedar furnishings surrounded by lush greenery, this tiny house serves'
                     ' up major cozy vibes. ')
            st.metric(label='Night price', value=f'$123.435', delta='1%')

        image_2, detail_2 = st.columns(2)
        with image_2:
            st.image('Resources/House2.jpg')
        with detail_2:
            st.subheader('Wellsville, Pennsylvania')
            st.write('Complete with a patio, porch, grill and hammock, this tiny home in Wellsville, Pennsylvania has'
                     ' all the ingredients to help you enjoy the great outdoors.')
            st.metric(label='Night price', value=f'$678.901', delta='5%')

        image_3, detail_3 = st.columns(2)
        with image_3:
            st.image('Resources/House3.jpg')
        with detail_3:
            st.subheader('Anacortes, Washington')
            st.write('This tiny home on Guemes Island is beautifully curated by local artists and craftsmen. After your'
                     ' voyage is over, fall asleep peacefully in the elevated loft.')
            st.metric(label='Night price', value=f'$234.456', delta='-4%')
    elif st.session_state.auth_host:
        if side.button('Log out'):
            st.session_state.auth_host = False
            st.experimental_rerun()
        st.header('Welcome host!')
        menu_id = hc.nav_bar(
            menu_definition=menu_data,
            home_name='My posts',
            hide_streamlit_markers=False,  # will show the st hamburger as well as the navbar now!
            sticky_nav=True,  # at the top or not
            sticky_mode='pinned',  # jumpy or not-jumpy, but sticky or pinned
        )
        # get page
        if menu_id == 'My posts':
            post_page()
        elif menu_id == 'Feedback':
            feedback_page()
    elif st.session_state.auth_guest:
        if side.button('Log out'):
            st.session_state.auth_guest = False
            st.experimental_rerun()
        st.header('Welcome guest!')
        image_1, detail_1 = st.columns(2)
        with image_1:
            st.image('Resources/House1.jpg')
        with detail_1:
            st.subheader('Sandy, Oregon')
            st.write('Located on a secluded plot of 23 acres, this tiny home provides you with your own private view of'
                     ' Oregon’s Mount Hood. With cedar furnishings surrounded by lush greenery, this tiny house serves'
                     ' up major cozy vibes. ')
            st.metric(label='Night price', value=f'$123.435', delta='1%')
            days = st.slider('How many days you will stay?', 1, 20, key='Sandy')
            if days:
                if st.checkbox('Include transport', key='Sandy'):
                    transport_option = st.radio('Which transport do you want to have?', ('Car', 'Truck', 'Motorcycle'),
                                                key='Sandy')
                    extra_price = 20 if transport_option == 'Car' else (30 if transport_option == 'Truck' else 10)
                    st.warning(f'The extra price for {transport_option} is {extra_price}. Do you want to book anyway?')
                if transport_option:
                    if st.button('Book!', key='Sandy'):
                        st.success(f'You booked Sandy, Oregon with {transport_option} as transport for {days} days')
                else:
                    if st.button('Book!', key='Sandy_book'):
                        st.success(f'You booked Sandy, Oregon for {days} days')
        image_2, detail_2 = st.columns(2)
        with image_2:
            st.image('Resources/House2.jpg')
        with detail_2:
            st.subheader('Wellsville, Pennsylvania')
            st.write('Complete with a patio, porch, grill and hammock, this tiny home in Wellsville, Pennsylvania has'
                     ' all the ingredients to help you enjoy the great outdoors.')
            st.metric(label='Night price', value=f'$678.901', delta='5%')
            days = st.slider('How many days you will stay?', 1, 20, key='Wellsville')
            if days:
                if st.checkbox('Include transport', key='Wellsville'):
                    transport_option = st.radio('Which transport do you want to have?', ('Car', 'Truck', 'Motorcycle'),
                                                key='Sandy')
                    extra_price = 20 if transport_option == 'Car' else (30 if transport_option == 'Truck' else 10)
                    st.warning(f'The extra price for {transport_option} is {extra_price}. Do you want to book anyway?')
                if transport_option:
                    if st.button('Book!', key='Wellsville'):
                        st.success(f'You booked Wellsville, Pennsylvania with {transport_option} as transport for {days} days')
                else:
                    if st.button('Book!', key='Wellsville_book'):
                        st.success(f'You booked Wellsville, Pennsylvania for {days} days')

        image_3, detail_3 = st.columns(2)
        with image_3:
            st.image('Resources/House3.jpg')
        with detail_3:
            st.subheader('Anacortes, Washington')
            st.write('This tiny home on Guemes Island is beautifully curated by local artists and craftsmen. After your'
                     ' voyage is over, fall asleep peacefully in the elevated loft.')
            st.metric(label='Night price', value=f'$234.456', delta='-4%')
            days = st.slider('How many days you will stay?', 1, 20, key='Anacortes')
            if days:
                if st.checkbox('Include transport', key='Anacortes'):
                    transport_option = st.radio('Which transport do you want to have?', ('Car', 'Truck', 'Motorcycle'),
                                                key='Anacortes')
                    extra_price = 20 if transport_option == 'Car' else (30 if transport_option == 'Truck' else 10)
                    st.warning(f'The extra price for {transport_option} is {extra_price}. Do you want to book anyway?')
                if transport_option:
                    if st.button('Book!', key='Anacortes'):
                        st.success(f'You booked Anacortes, Washington with {transport_option} as transport for {days} days')
                else:
                    if st.button('Book!', key='Anacortes_book'):
                        st.success(f'You booked Anacortes, Washington for {days} days')


if __name__ == '__main__':
    st.set_page_config(
        page_title='Airbnb',
        layout='wide',
        initial_sidebar_state='collapsed'
    )
    main()
