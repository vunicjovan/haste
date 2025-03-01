import streamlit as st

from ui.custom_app_page import CustomAppPage
from ui.home_page import HomePage
from ui.templates_page import TemplatesPage


def render_home_page() -> None:
    HomePage()


def render_custom_app_page() -> None:
    CustomAppPage()


def render_templates_page() -> None:
    TemplatesPage()


if __name__ == '__main__':
    page_navigator = st.navigation(
        [
            st.Page(render_home_page, title="Home"),
            st.Page(render_custom_app_page, title="Build A Custom Application"),
            st.Page(render_templates_page, title="Create An Application From Template"),
        ]
    )

    page_navigator.run()
