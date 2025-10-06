"""Modern navigation bar component with purple/grey/black theme."""

import reflex as rx

def navbar() -> rx.Component:
    """Modern navigation bar with glassmorphism effect."""
    return rx.box(
        rx.container(
            rx.hstack(
                # Logo/Brand with gradient
                rx.link(
                    rx.hstack(
                        rx.box(
                            rx.text("R", size="6", weight="bold", color="white"),
                            width="40px",
                            height="40px",
                            border_radius="10px",
                            background="linear-gradient(135deg, #8B5CF6, #A855F7)",
                            display="flex",
                            align_items="center",
                            justify_content="center",
                            box_shadow="0 4px 15px rgba(139, 92, 246, 0.3)",
                        ),
                        rx.heading("Resonance", size="6", color="gray.100", font_weight="bold"),
                        spacing="3",
                        align="center",
                    ),
                    href="/",
                    text_decoration="none",
                ),
                
                # Navigation Links with modern styling
                rx.hstack(
                    rx.link(
                        rx.text("Home", size="4", weight="medium", color="gray.300"),
                        href="/",
                        padding="0.5rem 1rem",
                        border_radius="8px",
                        transition="all 0.3s ease",
                        _hover={
                            "color": "white",
                            "background": "rgba(139, 92, 246, 0.2)",
                            "text_decoration": "none",
                            "transform": "translateY(-1px)"
                        },
                    ),
                    rx.link(
                        rx.text("About", size="4", weight="medium", color="gray.300"),
                        href="/about",
                        padding="0.5rem 1rem",
                        border_radius="8px",
                        transition="all 0.3s ease",
                        _hover={
                            "color": "white",
                            "background": "rgba(139, 92, 246, 0.2)",
                            "text_decoration": "none",
                            "transform": "translateY(-1px)"
                        },
                    ),
                    rx.link(
                        rx.text("Services", size="4", weight="medium", color="gray.300"),
                        href="/services",
                        padding="0.5rem 1rem",
                        border_radius="8px",
                        transition="all 0.3s ease",
                        _hover={
                            "color": "white",
                            "background": "rgba(139, 92, 246, 0.2)",
                            "text_decoration": "none",
                            "transform": "translateY(-1px)"
                        },
                    ),
                    rx.link(
                        rx.text("Contact", size="4", weight="medium", color="gray.300"),
                        href="/contact",
                        padding="0.5rem 1rem",
                        border_radius="8px",
                        transition="all 0.3s ease",
                        _hover={
                            "color": "white",
                            "background": "rgba(139, 92, 246, 0.2)",
                            "text_decoration": "none",
                            "transform": "translateY(-1px)"
                        },
                    ),
                    spacing="2",
                ),
                
                # CTA Button
                rx.button(
                    "Get Started",
                    size="3",
                    background="linear-gradient(135deg, #8B5CF6, #A855F7)",
                    color="white",
                    border="none",
                    border_radius="10px",
                    font_weight="bold",
                    padding="0.75rem 1.5rem",
                    box_shadow="0 4px 15px rgba(139, 92, 246, 0.3)",
                    transition="all 0.3s ease",
                    _hover={
                        "transform": "translateY(-2px)",
                        "box_shadow": "0 6px 25px rgba(139, 92, 246, 0.4)"
                    },
                ),
                
                justify="between",
                align="center",
                width="100%",
            ),
            max_width="1200px",
            padding="1rem",
        ),
        # Glassmorphism background
        background="rgba(17, 17, 17, 0.9)",
        backdrop_filter="blur(20px)",
        border_bottom="1px solid rgba(255, 255, 255, 0.1)",
        position="sticky",
        top="0",
        z_index="100",
        width="100%",
        box_shadow="0 8px 32px rgba(0, 0, 0, 0.3)",
    )