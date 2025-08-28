"""Home page component."""

import reflex as rx

def hero_section() -> rx.Component:
    """Hero section for the home page."""
    return rx.box(
        rx.vstack(
            rx.heading(
                "Welcome to Resonance",
                size="9",
                text_align="center",
                color="gray.800",
                margin_bottom="1rem",
            ),
            rx.text(
                "Perfect for an app that analyzes your musical patterns and ""resonates"" with your listening habits",
                size="5",
                text_align="center",
                color="gray.600",
                max_width="600px",
                margin_bottom="2rem",
            ),
            rx.hstack(
                rx.link(
                    rx.button(
                        "Get Started",
                        size="3",
                        variant="solid",
                        color_scheme="blue",
                    ),
                    href="/services",
                ),
                rx.link(
                    rx.button(
                        "Learn More",
                        size="3",
                        variant="outline",
                        color_scheme="blue",
                    ),
                    href="/about",
                ),
                spacing="4",
            ),
            spacing="4",
            align="center",
        ),
        padding="4rem 0",
        text_align="center",
    )

def features_section() -> rx.Component:
    """Features section."""
    return rx.box(
        rx.vstack(
            rx.heading("Why Choose MyApp?", size="7", text_align="center", margin_bottom="3rem"),
            rx.grid(
                rx.box(
                    rx.icon("zap", size=48, color="blue.500", margin_bottom="1rem"),
                    rx.heading("Fast", size="5", margin_bottom="0.5rem"),
                    rx.text("Lightning fast performance with optimized code", color="gray.600"),
                    text_align="center",
                    padding="2rem",
                    border="1px solid",
                    border_color="gray.200",
                    border_radius="lg",
                ),
                rx.box(
                    rx.icon("shield", size=48, color="green.500", margin_bottom="1rem"),
                    rx.heading("Secure", size="5", margin_bottom="0.5rem"),
                    rx.text("Built with security best practices in mind", color="gray.600"),
                    text_align="center",
                    padding="2rem",
                    border="1px solid",
                    border_color="gray.200",
                    border_radius="lg",
                ),
                rx.box(
                    rx.icon("users", size=48, color="purple.500", margin_bottom="1rem"),
                    rx.heading("User-Friendly", size="5", margin_bottom="0.5rem"),
                    rx.text("Intuitive interface designed for everyone", color="gray.600"),
                    text_align="center",
                    padding="2rem",
                    border="1px solid",
                    border_color="gray.200",
                    border_radius="lg",
                ),
                columns="3",
                spacing="4",
                width="100%",
            ),
            spacing="4",
        ),
        padding="4rem 0",
    )

def home_page() -> rx.Component:
    """Complete home page."""
    return rx.vstack(
        hero_section(),
        features_section(),
        spacing="0",
    )