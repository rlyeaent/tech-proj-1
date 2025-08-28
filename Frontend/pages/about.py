"""About page component."""

import reflex as rx

def about_hero() -> rx.Component:
    """About page hero section."""
    return rx.box(
        rx.vstack(
            rx.heading("About Us", size="8", text_align="center", color="gray.800"),
            rx.text(
                "Learn more about our mission, vision, and the team behind MyApp",
                size="4",
                text_align="center",
                color="gray.600",
                max_width="500px",
            ),
            spacing="3",
            align="center",
        ),
        padding="3rem 0",
        text_align="center",
    )

def mission_section() -> rx.Component:
    """Mission and vision section."""
    return rx.grid(
        rx.box(
            rx.icon("target", size=40, color="blue.500", margin_bottom="1rem"),
            rx.heading("Our Mission", size="6", margin_bottom="1rem"),
            rx.text(
                "To empower developers and businesses by providing cutting-edge web application solutions that are both powerful and easy to use.",
                color="gray.600",
                line_height="1.6",
            ),
            padding="2rem",
            border_radius="lg",
            background="blue.50",
        ),
        rx.box(
            rx.icon("eye", size=40, color="green.500", margin_bottom="1rem"),
            rx.heading("Our Vision", size="6", margin_bottom="1rem"),
            rx.text(
                "To become the leading platform for Python-based web development, making it accessible to developers of all skill levels.",
                color="gray.600",
                line_height="1.6",
            ),
            padding="2rem",
            border_radius="lg",
            background="green.50",
        ),
        columns="2",
        spacing="4",
        width="100%",
        margin="2rem 0",
    )

def team_section() -> rx.Component:
    """Team members section."""
    return rx.box(
        rx.vstack(
            rx.heading("Meet Our Team", size="7", text_align="center", margin_bottom="2rem"),
            rx.grid(
                rx.box(
                    rx.box(
                        rx.text("RL", size="6", weight="bold", color="white"),
                        width="80px",
                        height="80px",
                        border_radius="50%",
                        background="blue.500",
                        display="flex",
                        align_items="center",
                        justify_content="center",
                        margin="0 auto 1rem auto",
                    ),
                    rx.heading("Ryan Lee", size="5", margin_bottom="0.5rem"),
                    rx.text("CEO & Founder", color="gray.600", margin_bottom="0.5rem"),
                    rx.text("Passionate about building great products", size="3", color="gray.500"),
                    text_align="center",
                ),
                rx.box(
                    rx.box(
                        rx.text("NL", size="6", weight="bold", color="white"),
                        width="80px",
                        height="80px",
                        border_radius="50%",
                        background="green.500",
                        display="flex",
                        align_items="center",
                        justify_content="center",
                        margin="0 auto 1rem auto",
                    ),
                    rx.heading("Noah Lee", size="5", margin_bottom="0.5rem"),
                    rx.text("CTO", color="gray.600", margin_bottom="0.5rem"),
                    rx.text("Expert in Python and web technologies", size="3", color="gray.500"),
                    text_align="center",
                ),
                columns="3",
                spacing="4",
                width="100%",
            ),
            spacing="4",
        ),
        padding="3rem 0",
    )

def about_page() -> rx.Component:
    """Complete about page."""
    return rx.vstack(
        about_hero(),
        mission_section(),
        team_section(),
        spacing="0",
    )