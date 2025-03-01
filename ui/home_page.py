import streamlit as st

from ui.base.base_page import BasePage


class HomePage(BasePage):

    def __init__(self) -> None:
        super().__init__()

        with st.container():
            st.write("This is a custom app page")
