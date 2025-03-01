import streamlit as st

from enumerations.frameworks import Framework
from enumerations.virtual_environments import VirtualEnvironment
from ui.base.base_page import BasePage


class CustomAppPage(BasePage):

    def __init__(self) -> None:
        super().__init__()

        with st.container():
            selected_framework = st.selectbox(
                label="Framework Choice",
                options=Framework.values(),
            )

            selected_virtual_environment = st.selectbox(
                label="Virtual Environment Choice",
                options=VirtualEnvironment.values(),
            )

            auth_support = st.toggle(label="Basic Authentication & Authorization Support")

        # NOTE: A simple text file with selected values
        # TODO: A ZIP file containing the wholly generated project
        content = (
            f"Framework: {selected_framework}\n"
            f"Virtual Environment: {selected_virtual_environment}\n"
            f"Basic Authentication & Authentication Support: {auth_support}"
        )

        st.download_button(
            label="Generate & Download Your Project",
            data=content,
        )
