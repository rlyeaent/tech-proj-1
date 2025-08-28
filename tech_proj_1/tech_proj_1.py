"""Main Reflex application file."""

import reflex as rx
from rxconfig import config

# Import pages
from Frontend.pages.home import home_page
from Frontend.pages.about import about_page
# from Frontend.pages.services import services_page
# from Frontend.pages.contact import contact_page

# Import components
from Frontend.components.navbar import navbar
from Frontend.components.footer import footer

class State(rx.State):
    """Global app state."""
    current_page: str = "home"

def base_layout(page_content: rx.Component) -> rx.Component:
    """Base layout wrapper for all pages."""
    return rx.box(
        navbar(),
        rx.container(
            page_content,
            max_width="1200px",
            padding="2rem",
            min_height="70vh",
        ),
        footer(),
        width="100%",
    )

def index() -> rx.Component:
    """Home page."""
    return base_layout(home_page())

def about() -> rx.Component:
    """About page."""
    return base_layout(about_page())

# def services() -> rx.Component:
    """Services page."""
    return base_layout(services_page())

# def contact() -> rx.Component:
    """Contact page."""
    return base_layout(contact_page())

# Create the app
app = rx.App(
    style={
        "font_family": "Inter, sans-serif",
    }
)

# Add pages with routes
app.add_page(index, route="/", title="Home")
app.add_page(about, route="/about", title="About Us")
# app.add_page(services, route="/services", title="Our Services")
# app.add_page(contact, route="/contact", title="Contact Us")