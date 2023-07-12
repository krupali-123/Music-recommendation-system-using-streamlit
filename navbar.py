import streamlit as st


def navigation():
    try:
        path = st.experimental_get_query_params()['p'][0]
    except Exception as e:
        st.error('Please use the main app.')
        return None
    return path

if navigation() == "home":
    st.title('Home')
    st.write('This is the home page.')

elif navigation() == "download music":
    st.title('Background Music Free Download')


elif navigation() == "analysis":
    st.title('Analysis')
    x, y = st.number_input('Input X'), st.number_input('Input Y')
    st.write('Result: ' + str(x+y))

elif navigation() == "examples":
    st.title('Examples Menu')
    st.write('Select an example.')