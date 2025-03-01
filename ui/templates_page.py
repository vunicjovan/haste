import streamlit as st

from ui.base.base_page import BasePage


class TemplatesPage(BasePage):

    def __init__(self) -> None:
        super().__init__()

        with st.container():
            st.write("This is a template app page")
