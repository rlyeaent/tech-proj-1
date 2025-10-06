"""Modern footer component with dark theme."""

import reflex as rx

def footer() -> rx.Component:
    """Modern site footer with glassmorphism and gradient effects."""
    return rx.box(
        # Background gradient
        rx.box(
            position="absolute",
            top="0",
            left="0",
            right="0",
            bottom="0",
            background="linear-gradient(135deg, rgba(139, 92, 246, 0.1) 0%, rgba(168, 85, 247, 0.05) 100%)",
            z_index="1",
        ),
        
        rx.container(
            rx.vstack(
                # Main footer content
                rx.grid(
                    # Company info with modern branding
                    rx.vstack(
                        rx.hstack(
                            rx.box(
                                rx.text("R", size="5", weight="bold", color="white"),
                                width="35px",
                                height="35px",
                                border_radius="8px",
                                background="linear-gradient(135deg, #8B5CF6, #A855F7)",
                                display="flex",
                                align_items="center",
                                justify_content="center",
                                box_shadow="0 4px 15px rgba(139, 92, 246, 0.3)",
                            ),
                            rx.heading("Resonance", size="5", color="white", font_weight="bold"),
                            spacing="3",
                            align="center",
                            margin_bottom="1.5rem",
                        ),
                        rx.text(
                            "Transforming how you discover and experience music through advanced AI analysis and personalized recommendations.",
                            color="gray.400",
                            size="3",
                            line_height="1.6",
                            max_width="300px",
                        ),
                        # Social links
                        rx.hstack(
                            rx.link(
                                rx.box(
                                    rx.icon("github", size=18, color="gray.400"),
                                    padding="0.5rem",
                                    border_radius="8px",
                                    background="rgba(255, 255, 255, 0.05)",
                                    transition="all 0.3s ease",
                                    _hover={
                                        "background": "rgba(139, 92, 246, 0.2)",
                                        "color": "white"
                                    },
                                ),
                                href="https://github.com",
                            ),
                            rx.link(
                                rx.box(
                                    rx.icon("twitter", size=18, color="gray.400"),
                                    padding="0.5rem",
                                    border_radius="8px",
                                    background="rgba(255, 255, 255, 0.05)",
                                    transition="all 0.3s ease",
                                    _hover={
                                        "background": "rgba(139, 92, 246, 0.2)",
                                        "color": "white"
                                    },
                                ),
                                href="https://twitter.com",
                            ),
                            rx.link(
                                rx.box(
                                    rx.icon("linkedin", size=18, color="gray.400"),
                                    padding="0.5rem",
                                    border_radius="8px",
                                    background="rgba(255, 255, 255, 0.05)",
                                    transition="all 0.3s ease",
                                    _hover={
                                        "background": "rgba(139, 92, 246, 0.2)",
                                        "color": "white"
                                    },
                                ),
                                href="https://linkedin.com",
                            ),
                            spacing="3",
                            margin_top="1.5rem",
                        ),
                        align="start",
                        spacing="3",
                    ),
                    
                    # Quick links
                    rx.vstack(
                        rx.heading("Navigation", size="4", color="white", margin_bottom="1.5rem", font_weight="bold"),
                        rx.vstack(
                            rx.link(
                                "Home", 
                                href="/", 
                                color="gray.400",
                                transition="color 0.3s ease",
                                _hover={"color": "purple.400"}
                            ),
                            rx.link(
                                "About", 
                                href="/about", 
                                color="gray.400",
                                transition="color 0.3s ease",
                                _hover={"color": "purple.400"}
                            ),
                            rx.link(
                                "Services", 
                                href="/services", 
                                color="gray.400",
                                transition="color 0.3s ease",
                                _hover={"color": "purple.400"}
                            ),
                            rx.link(
                                "Contact", 
                                href="/contact", 
                                color="gray.400",
                                transition="color 0.3s ease",
                                _hover={"color": "purple.400"}
                            ),
                            spacing="3",
                            align="start",
                        ),
                        align="start",
                        spacing="3",
                    ),
                    
                    # Services
                    rx.vstack(
                        rx.heading("Services", size="4", color="white", margin_bottom="1.5rem", font_weight="bold"),
                        rx.vstack(
                            rx.text("Music Analysis", color="gray.400", size="3"),
                            rx.text("Personalized Playlists", color="gray.400", size="3"),
                            rx.text("Trend Discovery", color="gray.400", size="3"),
                            rx.text("API Integration", color="gray.400", size="3"),
                            spacing="3",
                            align="start",
                        ),
                        align="start",
                        spacing="3",
                    ),
                    
                    # Contact info with modern icons
                    rx.vstack(
                        rx.heading("Get in Touch", size="4", color="white", margin_bottom="1.5rem", font_weight="bold"),
                        rx.vstack(
                            rx.hstack(
                                rx.box(
                                    rx.icon("mail", size=16, color="purple.400"),
                                    padding="0.3rem",
                                    border_radius="6px",
                                    background="rgba(139, 92, 246, 0.1)",
                                ),
                                rx.text("hello@resonance.com", color="gray.400", size="3"),
                                spacing="3",
                                align="center",
                            ),
                            rx.hstack(
                                rx.box(
                                    rx.icon("phone", size=16, color="purple.400"),
                                    padding="0.3rem",
                                    border_radius="6px",
                                    background="rgba(139, 92, 246, 0.1)",
                                ),
                                rx.text("+1 (555) 123-4567", color="gray.400", size="3"),
                                spacing="3",
                                align="center",
                            ),
                            rx.hstack(
                                rx.box(
                                    rx.icon("map_pin", size=16, color="purple.400"),
                                    padding="0.3rem",
                                    border_radius="6px",
                                    background="rgba(139, 92, 246, 0.1)",
                                ),
                                rx.vstack(
                                    rx.text("San Francisco, CA", color="gray.400", size="3"),
                                    rx.text("United States", color="gray.400", size="3"),
                                    spacing="1",
                                    align="start",
                                ),
                                spacing="3",
                                align="start",
                            ),
                            spacing="4",
                            align="start",
                        ),
                        align="start",
                        spacing="3",
                    ),
                    
                    columns="4",
                    spacing="8",
                    width="100%",
                ),
                
                # Elegant divider
                rx.box(
                    height="1px",
                    background="linear-gradient(90deg, transparent 0%, rgba(139, 92, 246, 0.5) 50%, transparent 100%)",
                    margin="3rem 0",
                    width="100%",
                ),
                
                # Bottom footer with modern styling
                rx.hstack(
                    rx.text(
                        "© 2025 Resonance. All rights reserved.",
                        color="gray.500",
                        size="3",
                    ),
                    rx.hstack(
                        rx.link("Privacy Policy", href="#", color="gray.500", size="3", _hover={"color": "purple.400"}),
                        rx.text("•", color="gray.600"),
                        rx.link("Terms of Service", href="#", color="gray.500", size="3", _hover={"color": "purple.400"}),
                        rx.text("•", color="gray.600"),
                        rx.link("Cookie Policy", href="#", color="gray.500", size="3", _hover={"color": "purple.400"}),
                        spacing="2",
                        align="center",
                    ),
                    justify="between",
                    align="center",
                    width="100%",
                ),
                
                spacing="0",
            ),
            max_width="1200px",
            padding="3rem",
            z_index="2",
            position="relative",
        ),
        
        background="rgba(10, 10, 10, 0.95)",
        backdrop_filter="blur(20px)",
        border_top="1px solid rgba(255, 255, 255, 0.1)",
        width="100%",
        margin_top="auto",
        position="relative",
        overflow="hidden",
    )