"""Modern about page component with dark theme."""

import reflex as rx

def about_hero() -> rx.Component:
    """Modern about page hero section."""
    return rx.box(
        # Background gradient overlay
        rx.box(
            position="absolute",
            top="0",
            left="0",
            right="0",
            bottom="0",
            background="radial-gradient(circle at 50% 50%, rgba(139, 92, 246, 0.2) 0%, transparent 70%)",
            z_index="1",
        ),
        
        rx.vstack(
            rx.text(
                "ABOUT US",
                size="3",
                color="purple.400",
                font_weight="bold",
                letter_spacing="0.2em",
                text_align="center",
                margin_bottom="1rem",
            ),
            rx.heading(
                "Revolutionizing Music Discovery", 
                size="8", 
                text_align="center", 
                color="white",
                font_weight="bold",
                margin_bottom="1rem",
            ),
            rx.text(
                "We're on a mission to transform how people discover, understand, and connect with music through cutting-edge AI technology and intuitive design.",
                size="5",
                text_align="center",
                color="gray.300",
                max_width="700px",
                line_height="1.6",
            ),
            spacing="3",
            align="center",
            z_index="2",
            position="relative",
        ),
        padding="6rem 0",
        text_align="center",
        position="relative",
        overflow="hidden",
    )

def mission_vision_section() -> rx.Component:
    """Modern mission and vision section."""
    return rx.grid(
        # Mission Card
        rx.box(
            rx.vstack(
                rx.box(
                    rx.icon("target", size=40, color="white"),
                    width="80px",
                    height="80px",
                    border_radius="20px",
                    background="linear-gradient(135deg, #8B5CF6, #A855F7)",
                    display="flex",
                    align_items="center",
                    justify_content="center",
                    margin_bottom="2rem",
                    box_shadow="0 10px 30px rgba(139, 92, 246, 0.3)",
                ),
                rx.heading("Our Mission", size="6", color="white", margin_bottom="1.5rem", font_weight="bold"),
                rx.text(
                    "To democratize music discovery by leveraging advanced AI algorithms that understand individual listening patterns, emotions, and preferences to create deeply personalized musical experiences.",
                    color="gray.300",
                    line_height="1.7",
                    text_align="center",
                    size="4",
                ),
                spacing="3",
                align="center",
            ),
            padding="3rem",
            background="rgba(255, 255, 255, 0.05)",
            border="1px solid rgba(139, 92, 246, 0.2)",
            border_radius="25px",
            backdrop_filter="blur(20px)",
            transition="all 0.3s ease",
            _hover={
                "transform": "translateY(-8px)",
                "background": "rgba(255, 255, 255, 0.08)",
                "border_color": "rgba(139, 92, 246, 0.4)",
                "box_shadow": "0 20px 40px rgba(139, 92, 246, 0.2)"
            },
        ),
        
        # Vision Card
        rx.box(
            rx.vstack(
                rx.box(
                    rx.icon("eye", size=40, color="white"),
                    width="80px",
                    height="80px",
                    border_radius="20px",
                    background="linear-gradient(135deg, #A855F7, #EC4899)",
                    display="flex",
                    align_items="center",
                    justify_content="center",
                    margin_bottom="2rem",
                    box_shadow="0 10px 30px rgba(168, 85, 247, 0.3)",
                ),
                rx.heading("Our Vision", size="6", color="white", margin_bottom="1.5rem", font_weight="bold"),
                rx.text(
                    "To become the world's leading platform for intelligent music curation, fostering deeper connections between artists and listeners while supporting music discovery across all genres and cultures.",
                    color="gray.300",
                    line_height="1.7",
                    text_align="center",
                    size="4",
                ),
                spacing="3",
                align="center",
            ),
            padding="3rem",
            background="rgba(255, 255, 255, 0.05)",
            border="1px solid rgba(168, 85, 247, 0.2)",
            border_radius="25px",
            backdrop_filter="blur(20px)",
            transition="all 0.3s ease",
            _hover={
                "transform": "translateY(-8px)",
                "background": "rgba(255, 255, 255, 0.08)",
                "border_color": "rgba(168, 85, 247, 0.4)",
                "box_shadow": "0 20px 40px rgba(168, 85, 247, 0.2)"
            },
        ),
        
        columns="2",
        spacing="6",
        width="100%",
        margin="4rem 0",
    )

def team_section() -> rx.Component:
    """Modern team members section."""
    return rx.box(
        rx.vstack(
            rx.text(
                "MEET THE TEAM",
                size="3",
                color="purple.400",
                font_weight="bold",
                letter_spacing="0.2em",
                text_align="center",
                margin_bottom="1rem",
            ),
            rx.heading("The People Behind Resonance", size="7", text_align="center", color="white", margin_bottom="4rem", font_weight="bold"),
            
            rx.grid(
                # Ryan Lee Card
                rx.box(
                    rx.vstack(
                        # Profile image placeholder with gradient
                        rx.box(
                            rx.text("RL", size="7", weight="bold", color="white"),
                            width="120px",
                            height="120px",
                            border_radius="25px",
                            background="linear-gradient(135deg, #8B5CF6, #A855F7)",
                            display="flex",
                            align_items="center",
                            justify_content="center",
                            margin_bottom="1.5rem",
                            box_shadow="0 15px 35px rgba(139, 92, 246, 0.4)",
                        ),
                        
                        rx.heading("Ryan Lee", size="6", color="white", margin_bottom="0.5rem", font_weight="bold"),
                        rx.text("CEO & Founder", color="purple.400", margin_bottom="0.5rem", font_weight="medium"),
                        rx.text(
                            "Visionary leader with 10+ years in music tech, passionate about building products that transform how we experience music.",
                            size="3", 
                            color="gray.400",
                            text_align="center",
                            line_height="1.6",
                        ),
                        
                        # Social links
                        rx.hstack(
                            rx.link(
                                rx.box(
                                    rx.icon("linkedin", size=16),
                                    padding="0.5rem",
                                    border_radius="8px",
                                    background="rgba(139, 92, 246, 0.2)",
                                    color="white",
                                    transition="all 0.3s ease",
                                    _hover={"background": "rgba(139, 92, 246, 0.4)"}
                                ),
                                href="#",
                            ),
                            rx.link(
                                rx.box(
                                    rx.icon("twitter", size=16),
                                    padding="0.5rem",
                                    border_radius="8px",
                                    background="rgba(139, 92, 246, 0.2)",
                                    color="white",
                                    transition="all 0.3s ease",
                                    _hover={"background": "rgba(139, 92, 246, 0.4)"}
                                ),
                                href="#",
                            ),
                            spacing="2",
                            margin_top="1rem",
                        ),
                        
                        spacing="3",
                        align="center",
                    ),
                    padding="2.5rem",
                    background="rgba(255, 255, 255, 0.05)",
                    border="1px solid rgba(255, 255, 255, 0.1)",
                    border_radius="25px",
                    backdrop_filter="blur(20px)",
                    text_align="center",
                    transition="all 0.3s ease",
                    _hover={
                        "transform": "translateY(-5px)",
                        "background": "rgba(255, 255, 255, 0.08)",
                        "border_color": "rgba(139, 92, 246, 0.3)"
                    },
                ),
                
                # Noah Lee Card
                rx.box(
                    rx.vstack(
                        # Profile image placeholder with gradient
                        rx.box(
                            rx.text("NL", size="7", weight="bold", color="white"),
                            width="120px",
                            height="120px",
                            border_radius="25px",
                            background="linear-gradient(135deg, #A855F7, #EC4899)",
                            display="flex",
                            align_items="center",
                            justify_content="center",
                            margin_bottom="1.5rem",
                            box_shadow="0 15px 35px rgba(168, 85, 247, 0.4)",
                        ),
                        
                        rx.heading("Noah Lee", size="6", color="white", margin_bottom="0.5rem", font_weight="bold"),
                        rx.text("CTO & Co-Founder", color="purple.400", margin_bottom="0.5rem", font_weight="medium"),
                        rx.text(
                            "Machine learning expert and full-stack developer specializing in audio processing and recommendation systems.",
                            size="3", 
                            color="gray.400",
                            text_align="center",
                            line_height="1.6",
                        ),
                        
                        # Social links
                        rx.hstack(
                            rx.link(
                                rx.box(
                                    rx.icon("linkedin", size=16),
                                    padding="0.5rem",
                                    border_radius="8px",
                                    background="rgba(168, 85, 247, 0.2)",
                                    color="white",
                                    transition="all 0.3s ease",
                                    _hover={"background": "rgba(168, 85, 247, 0.4)"}
                                ),
                                href="#",
                            ),
                            rx.link(
                                rx.box(
                                    rx.icon("github", size=16),
                                    padding="0.5rem",
                                    border_radius="8px",
                                    background="rgba(168, 85, 247, 0.2)",
                                    color="white",
                                    transition="all 0.3s ease",
                                    _hover={"background": "rgba(168, 85, 247, 0.4)"}
                                ),
                                href="#",
                            ),
                            spacing="2",
                            margin_top="1rem",
                        ),
                        
                        spacing="3",
                        align="center",
                    ),
                    padding="2.5rem",
                    background="rgba(255, 255, 255, 0.05)",
                    border="1px solid rgba(255, 255, 255, 0.1)",
                    border_radius="25px",
                    backdrop_filter="blur(20px)",
                    text_align="center",
                    transition="all 0.3s ease",
                    _hover={
                        "transform": "translateY(-5px)",
                        "background": "rgba(255, 255, 255, 0.08)",
                        "border_color": "rgba(168, 85, 247, 0.3)"
                    },
                ),
                
                columns="2",
                spacing="6",
                width="100%",
                justify_items="center",
            ),
            
            spacing="4",
        ),
        padding="6rem 0",
    )

def values_section() -> rx.Component:
    """Company values section."""
    return rx.box(
        rx.vstack(
            rx.text(
                "OUR VALUES",
                size="3",
                color="purple.400",
                font_weight="bold",
                letter_spacing="0.2em",
                text_align="center",
                margin_bottom="1rem",
            ),
            rx.heading("What Drives Us", size="7", text_align="center", color="white", margin_bottom="4rem", font_weight="bold"),
            
            rx.grid(
                rx.box(
                    rx.vstack(
                        rx.box(
                            rx.icon("heart", size=32, color="white"),
                            width="60px",
                            height="60px",
                            border_radius="15px",
                            background="linear-gradient(135deg, #EF4444, #DC2626)",
                            display="flex",
                            align_items="center",
                            justify_content="center",
                            margin_bottom="1.5rem",
                            box_shadow="0 8px 25px rgba(239, 68, 68, 0.3)",
                        ),
                        rx.heading("Passion", size="5", color="white", margin_bottom="1rem"),
                        rx.text("We're driven by our love for music and technology", color="gray.300", text_align="center"),
                        spacing="2",
                        align="center",
                    ),
                    padding="2rem",
                    background="rgba(255, 255, 255, 0.03)",
                    border="1px solid rgba(255, 255, 255, 0.1)",
                    border_radius="20px",
                    backdrop_filter="blur(10px)",
                ),
                
                rx.box(
                    rx.vstack(
                        rx.box(
                            rx.icon("users", size=32, color="white"),
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
                        rx.heading("Community", size="5", color="white", margin_bottom="1rem"),
                        rx.text("Building connections between artists and listeners worldwide", color="gray.300", text_align="center"),
                        spacing="2",
                        align="center",
                    ),
                    padding="2rem",
                    background="rgba(255, 255, 255, 0.03)",
                    border="1px solid rgba(255, 255, 255, 0.1)",
                    border_radius="20px",
                    backdrop_filter="blur(10px)",
                ),
                
                rx.box(
                    rx.vstack(
                        rx.box(
                            rx.icon("sparkles", size=32, color="white"),
                            width="60px",
                            height="60px",
                            border_radius="15px",
                            background="linear-gradient(135deg, #F59E0B, #D97706)",
                            display="flex",
                            align_items="center",
                            justify_content="center",
                            margin_bottom="1.5rem",
                            box_shadow="0 8px 25px rgba(245, 158, 11, 0.3)",
                        ),
                        rx.heading("Innovation", size="5", color="white", margin_bottom="1rem"),
                        rx.text("Constantly pushing boundaries in music technology", color="gray.300", text_align="center"),
                        spacing="2",
                        align="center",
                    ),
                    padding="2rem",
                    background="rgba(255, 255, 255, 0.03)",
                    border="1px solid rgba(255, 255, 255, 0.1)",
                    border_radius="20px",
                    backdrop_filter="blur(10px)",
                ),
                
                columns="3",
                spacing="4",
                width="100%",
            ),
            
            spacing="4",
        ),
        padding="4rem 0",
        background="rgba(0, 0, 0, 0.2)",
        border_radius="30px",
        margin="2rem 0",
    )

def about_page() -> rx.Component:
    """Complete modern about page."""
    return rx.vstack(
        about_hero(),
        mission_vision_section(),
        team_section(),
        values_section(),
        spacing="0",
    )