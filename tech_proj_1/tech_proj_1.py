"""Main Reflex application file with modern dark theme."""

import reflex as rx
from rxconfig import config

# Import pages
from Frontend.pages.home import home_page
from Frontend.pages.about import about_page
from Frontend.pages.services import services_page
from Frontend.pages.contact import contact_page

# Import components
from Frontend.components.navbar import navbar
from Frontend.components.footer import footer

class State(rx.State):
    """Global app state."""
    current_page: str = "home"

def base_layout(page_content: rx.Component) -> rx.Component:
    """Base layout wrapper for all pages with modern dark theme."""
    return rx.box(
        # Background with subtle pattern
        rx.box(
            position="fixed",
            top="0",
            left="0",
            right="0",
            bottom="0",
            background="linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 50%, #0f0f0f 100%)",
            z_index="-2",
        ),
        
        # Animated background elements
        rx.box(
            position="fixed",
            top="0",
            left="0",
            right="0",
            bottom="0",
            background="radial-gradient(circle at 20% 80%, rgba(139, 92, 246, 0.1) 0%, transparent 50%), radial-gradient(circle at 80% 20%, rgba(168, 85, 247, 0.08) 0%, transparent 50%)",
            z_index="-1",
        ),
        
        navbar(),
        rx.container(
            page_content,
            max_width="1200px",
            padding="0 2rem",
            min_height="80vh",
            position="relative",
            z_index="1",
        ),
        footer(),
        width="100%",
        min_height="100vh",
        color="white",
    )

def index() -> rx.Component:
    """Home page."""
    return base_layout(home_page())

def about() -> rx.Component:
    """About page."""
    return base_layout(about_page())

def services() -> rx.Component:
    """Services page."""
    return base_layout(services_page())

def contact() -> rx.Component:
    """Contact page."""
    return base_layout(contact_page())

# Create the app with modern styling
app = rx.App(
    style={
        "font_family": "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
        "background": "#0a0a0a",
        "color": "#ffffff",
        # Global CSS for smooth scrolling and modern effects
        "*": {
            "box_sizing": "border-box",
            "margin": "0",
            "padding": "0",
        },
        "html": {
            "scroll_behavior": "smooth",
        },
        "body": {
            "background": "#0a0a0a",
            "overflow_x": "hidden",
        },
        # Custom scrollbar styling
        "::-webkit-scrollbar": {
            "width": "8px",
        },
        "::-webkit-scrollbar-track": {
            "background": "rgba(255, 255, 255, 0.1)",
        },
        "::-webkit-scrollbar-thumb": {
            "background": "linear-gradient(135deg, #8B5CF6, #A855F7)",
            "border_radius": "4px",
        },
        "::-webkit-scrollbar-thumb:hover": {
            "background": "linear-gradient(135deg, #7C3AED, #9333EA)",
        },
    }
)

# Add pages with routes
app.add_page(index, route="/", title="Resonance - Home")
app.add_page(about, route="/about", title="Resonance - About Us")
app.add_page(services, route="/services", title="Resonance - Our Services")
app.add_page(contact, route="/contact", title="Resonance - Contact Us")