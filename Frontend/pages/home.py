"""Modern home page component with contemporary design."""

import reflex as rx

def hero_section() -> rx.Component:
    """Modern hero section with animated elements."""
    return rx.box(
        # Background gradient overlay
        rx.box(
            position="absolute",
            top="0",
            left="0",
            right="0",
            bottom="0",
            background="radial-gradient(circle at 30% 20%, rgba(139, 92, 246, 0.3) 0%, transparent 50%), radial-gradient(circle at 70% 80%, rgba(168, 85, 247, 0.2) 0%, transparent 50%)",
            z_index="1",
        ),
        
        rx.vstack(
            # Main heading with gradient text
            rx.heading(
                "Welcome to",
                size="6",
                color="gray.400",
                text_align="center",
                margin_bottom="0.5rem",
                z_index="2",
                position="relative",
            ),
            rx.heading(
                "Resonance",
                size="9",
                text_align="center",
                background="linear-gradient(135deg, #8B5CF6, #A855F7, #EC4899)",
                background_clip="text",
                color="transparent",
                margin_bottom="1rem",
                z_index="2",
                position="relative",
                font_weight="bold",
            ),
            
            # Subtitle
            rx.text(
                "Perfect for an app that analyzes your musical patterns and resonates with your listening habits",
                size="5",
                text_align="center",
                color="gray.300",
                max_width="700px",
                margin_bottom="3rem",
                line_height="1.6",
                z_index="2",
                position="relative",
            ),
            
            # CTA Buttons with modern styling
            rx.hstack(
                rx.button(
                    rx.hstack(
                        rx.text("Get Started", weight="bold"),
                        rx.icon("arrow_right", size=18),
                        spacing="2",
                        align="center",
                    ),
                    size="4",
                    background="linear-gradient(135deg, #8B5CF6, #A855F7)",
                    color="white",
                    border="none",
                    border_radius="12px",
                    padding="1rem 2rem",
                    box_shadow="0 8px 25px rgba(139, 92, 246, 0.4)",
                    transition="all 0.3s ease",
                    _hover={
                        "transform": "translateY(-3px)",
                        "box_shadow": "0 12px 35px rgba(139, 92, 246, 0.5)"
                    },
                ),
                rx.button(
                    rx.hstack(
                        rx.icon("play", size=18),
                        rx.text("Watch Demo", weight="bold"),
                        spacing="2",
                        align="center",
                    ),
                    size="4",
                    background="rgba(255, 255, 255, 0.1)",
                    color="white",
                    border="1px solid rgba(139, 92, 246, 0.3)",
                    border_radius="12px",
                    padding="1rem 2rem",
                    backdrop_filter="blur(10px)",
                    transition="all 0.3s ease",
                    _hover={
                        "background": "rgba(139, 92, 246, 0.2)",
                        "border_color": "rgba(139, 92, 246, 0.5)",
                        "transform": "translateY(-2px)"
                    },
                ),
                spacing="5",
                z_index="2",
                position="relative",
            ),
            
            spacing="4",
            align="center",
            z_index="2",
            position="relative",
        ),
        
        padding="6rem 0",
        text_align="center",
        position="relative",
        overflow="hidden",
    )

def features_section() -> rx.Component:
    """Modern features section with glassmorphism cards."""
    return rx.box(
        rx.vstack(
            rx.text(
                "FEATURES",
                size="3",
                color="purple.400",
                font_weight="bold",
                letter_spacing="0.2em",
                text_align="center",
                margin_bottom="1rem",
            ),
            rx.heading(
                "Why Choose Resonance?", 
                size="8", 
                text_align="center", 
                color="white",
                margin_bottom="4rem",
                font_weight="bold",
            ),
            
            rx.grid(
                # Feature Card 1
                rx.box(
                    rx.vstack(
                        rx.box(
                            rx.icon("zap", size=32, color="white"),
                            width="60px",
                            height="60px",
                            border_radius="15px",
                            background="linear-gradient(135deg, #8B5CF6, #A855F7)",
                            display="flex",
                            align_items="center",
                            justify_content="center",
                            margin_bottom="1.5rem",
                            box_shadow="0 8px 25px rgba(139, 92, 246, 0.3)",
                        ),
                        rx.heading("Lightning Fast", size="5", color="white", margin_bottom="1rem"),
                        rx.text(
                            "Optimized performance with cutting-edge algorithms for instant music analysis",
                            color="gray.300",
                            text_align="center",
                            line_height="1.6",
                        ),
                        spacing="3",
                        align="center",
                    ),
                    padding="2.5rem",
                    background="rgba(255, 255, 255, 0.05)",
                    border="1px solid rgba(255, 255, 255, 0.1)",
                    border_radius="20px",
                    backdrop_filter="blur(20px)",
                    transition="all 0.3s ease",
                    _hover={
                        "transform": "translateY(-5px)",
                        "background": "rgba(255, 255, 255, 0.08)",
                        "border_color": "rgba(139, 92, 246, 0.3)"
                    },
                ),
                
                # Feature Card 2
                rx.box(
                    rx.vstack(
                        rx.box(
                            rx.icon("brain", size=32, color="white"),
                            width="60px",
                            height="60px",
                            border_radius="15px",
                            background="linear-gradient(135deg, #A855F7, #EC4899)",
                            display="flex",
                            align_items="center",
                            justify_content="center",
                            margin_bottom="1.5rem",
                            box_shadow="0 8px 25px rgba(168, 85, 247, 0.3)",
                        ),
                        rx.heading("AI-Powered", size="5", color="white", margin_bottom="1rem"),
                        rx.text(
                            "Advanced machine learning to understand and predict your music preferences",
                            color="gray.300",
                            text_align="center",
                            line_height="1.6",
                        ),
                        spacing="3",
                        align="center",
                    ),
                    padding="2.5rem",
                    background="rgba(255, 255, 255, 0.05)",
                    border="1px solid rgba(255, 255, 255, 0.1)",
                    border_radius="20px",
                    backdrop_filter="blur(20px)",
                    transition="all 0.3s ease",
                    _hover={
                        "transform": "translateY(-5px)",
                        "background": "rgba(255, 255, 255, 0.08)",
                        "border_color": "rgba(168, 85, 247, 0.3)"
                    },
                ),
                
                # Feature Card 3
                rx.box(
                    rx.vstack(
                        rx.box(
                            rx.icon("shield", size=32, color="white"),
                            width="60px",
                            height="60px",
                            border_radius="15px",
                            background="linear-gradient(135deg, #10B981, #059669)",
                            display="flex",
                            align_items="center",
                            justify_content="center",
                            margin_bottom="1.5rem",
                            box_shadow="0 8px 25px rgba(16, 185, 129, 0.3)",
                        ),
                        rx.heading("Privacy First", size="5", color="white", margin_bottom="1rem"),
                        rx.text(
                            "Your music data stays secure with end-to-end encryption and privacy protection",
                            color="gray.300",
                            text_align="center",
                            line_height="1.6",
                        ),
                        spacing="3",
                        align="center",
                    ),
                    padding="2.5rem",
                    background="rgba(255, 255, 255, 0.05)",
                    border="1px solid rgba(255, 255, 255, 0.1)",
                    border_radius="20px",
                    backdrop_filter="blur(20px)",
                    transition="all 0.3s ease",
                    _hover={
                        "transform": "translateY(-5px)",
                        "background": "rgba(255, 255, 255, 0.08)",
                        "border_color": "rgba(16, 185, 129, 0.3)"
                    },
                ),
                
                columns="3",
                spacing="6",
                width="100%",
            ),
            
            spacing="4",
            align="center",
        ),
        padding="6rem 0",
        background="rgba(0, 0, 0, 0.2)",
        margin="4rem 0",
        border_radius="30px",
    )

def stats_section() -> rx.Component:
    """Modern stats section."""
    return rx.box(
        rx.grid(
            rx.vstack(
                rx.text("1M+", size="8", color="white", font_weight="bold"),
                rx.text("Songs Analyzed", color="gray.400", size="4"),
                spacing="2",
                align="center",
            ),
            rx.vstack(
                rx.text("50K+", size="8", color="white", font_weight="bold"),
                rx.text("Active Users", color="gray.400", size="4"),
                spacing="2",
                align="center",
            ),
            rx.vstack(
                rx.text("99.9%", size="8", color="white", font_weight="bold"),
                rx.text("Uptime", color="gray.400", size="4"),
                spacing="2",
                align="center",
            ),
            rx.vstack(
                rx.text("24/7", size="8", color="white", font_weight="bold"),
                rx.text("Support", color="gray.400", size="4"),
                spacing="2",
                align="center",
            ),
            columns="4",
            spacing="8",
            width="100%",
        ),
        padding="4rem 0",
        text_align="center",
    )

def home_page() -> rx.Component:
    """Complete modern home page."""
    return rx.vstack(
        hero_section(),
        features_section(),
        stats_section(),
        spacing="0",
    )