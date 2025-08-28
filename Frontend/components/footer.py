"""Footer component."""

import reflex as rx

def footer() -> rx.Component:
    """Site footer with links and information."""
    return rx.box(
        rx.container(
            rx.vstack(
                # Main footer content
                rx.grid(
                    # Company info
                    rx.vstack(
                        rx.heading("MyApp", size="5", color="white", margin_bottom="1rem"),
                        rx.text(
                            "Building amazing web applications with Reflex. "
                            "Empowering developers with modern tools and frameworks.",
                            color="gray.300",
                            size="3",
                            line_height="1.5",
                        ),
                        align="start",
                        spacing="2",
                    ),
                    
                    # Quick links
                    rx.vstack(
                        rx.heading("Quick Links", size="4", color="white", margin_bottom="1rem"),
                        rx.vstack(
                            rx.link("Home", href="/", color="gray.300"),
                            rx.link("About", href="/about", color="gray.300"),
                            rx.link("Services", href="/services", color="gray.300"),
                            rx.link("Contact", href="/contact", color="gray.300"),
                            spacing="2",
                            align="start",
                        ),
                        align="start",
                        spacing="2",
                    ),
                    
                    # Services
                    rx.vstack(
                        rx.heading("Services", size="4", color="white", margin_bottom="1rem"),
                        rx.vstack(
                            rx.text("Web Development", color="gray.300", size="3"),
                            rx.text("Mobile Development", color="gray.300", size="3"),
                            rx.text("Cloud Solutions", color="gray.300", size="3"),
                            rx.text("Consulting", color="gray.300", size="3"),
                            spacing="2",
                            align="start",
                        ),
                        align="start",
                        spacing="2",
                    ),
                    
                    # Contact info
                    rx.vstack(
                        rx.heading("Contact", size="4", color="white", margin_bottom="1rem"),
                        rx.vstack(
                            rx.hstack(
                                rx.icon("mail", size=16, color="gray.300"),
                                rx.text("contact@myapp.com", color="gray.300", size="3"),
                                spacing="2",
                            ),
                            rx.hstack(
                                rx.icon("phone", size=16, color="gray.300"),
                                rx.text("+1 (555) 123-4567", color="gray.300", size="3"),
                                spacing="2",
                            ),
                            rx.hstack(
                                rx.icon("map_pin", size=16, color="gray.300"),
                                rx.text("City, State 12345", color="gray.300", size="3"),
                                spacing="2",
                            ),
                            spacing="2",
                            align="start",
                        ),
                        align="start",
                        spacing="2",
                    ),
                    
                    columns="4",
                    spacing="4",
                    width="100%",
                ),
                
                # Divider
                rx.divider(color="gray.600", margin="2rem 0"),
                
                # Bottom footer
                rx.hstack(
                    rx.text(
                        f"© 2025 Resonance. All rights reserved.",
                        color="gray.400",
                        size="3",
                    ),
                    rx.hstack(
                        rx.link(
                            rx.icon("github", size=20),
                            href="https://github.com",
                            color="gray.400",
                            _hover={"color": "white"},
                        ),
                        rx.link(
                            rx.icon("twitter", size=20),
                            href="https://twitter.com",
                            color="gray.400",
                            _hover={"color": "white"},
                        ),
                        rx.link(
                            rx.icon("linkedin", size=20),
                            href="https://linkedin.com",
                            color="gray.400",
                            _hover={"color": "white"},
                        ),
                        spacing="3",
                    ),
                    justify="between",
                    align="center",
                    width="100%",
                ),
                
                spacing="0",
            ),
            max_width="1200px",
            padding="2rem",
        ),
        background="gray.900",
        width="100%",
        margin_top="auto",
    )