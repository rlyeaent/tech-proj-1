"""Navigation bar component."""

import reflex as rx

def navbar() -> rx.Component:
    """Navigation bar with links to all pages."""
    return rx.box(
        rx.container(
            rx.hstack(
                # Logo/Brand
                rx.link(
                    rx.heading("Resonance", size="6", color="blue.500"),
                    href="/",
                    text_decoration="none",
                ),
                
                # Navigation Links
                rx.hstack(
                    rx.link(
                        rx.text("Home", size="4", weight="medium"),
                        href="/",
                        color="gray.700",
                        _hover={"color": "blue.500", "text_decoration": "none"},
                    ),
                    rx.link(
                        rx.text("About", size="4", weight="medium"),
                        href="/about",
                        color="gray.700",
                        _hover={"color": "blue.500", "text_decoration": "none"},
                    ),
                    rx.link(
                        rx.text("Services", size="4", weight="medium"),
                        href="/services",
                        color="gray.700",
                        _hover={"color": "blue.500", "text_decoration": "none"},
                    ),
                    rx.link(
                        rx.text("Contact", size="4", weight="medium"),
                        href="/contact",
                        color="gray.700",
                        _hover={"color": "blue.500", "text_decoration": "none"},
                    ),
                    spacing="6",
                ),
                
                # Theme toggle button
                rx.color_mode.button(),
                
                justify="between",
                align="center",
                width="100%",
            ),
            max_width="1200px",
            padding="1rem",
        ),
        background="white",
        border_bottom="1px solid",
        border_color="gray.200",
        position="sticky",
        top="0",
        z_index="100",
        width="100%",
    )