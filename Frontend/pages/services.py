"""Modern services page component with dark theme."""

import reflex as rx

def services_hero() -> rx.Component:
    """Modern services page hero section."""
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
                "OUR SERVICES",
                size="3",
                color="purple.400",
                font_weight="bold",
                letter_spacing="0.2em",
                text_align="center",
                margin_bottom="1rem",
            ),
            rx.heading(
                "Transform Your Music Experience", 
                size="8", 
                text_align="center", 
                color="white",
                font_weight="bold",
                margin_bottom="1rem",
            ),
            rx.text(
                "Comprehensive AI-powered solutions for music analysis, discovery, and personalization tailored to your unique listening patterns.",
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

def service_card(icon: str, title: str, description: str, features: list, price: str, gradient: str, shadow_color: str) -> rx.Component:
    """Modern service card component with glassmorphism."""
    return rx.box(
        rx.vstack(
            # Icon with gradient background
            rx.box(
                rx.icon(icon, size=40, color="white"),
                width="80px",
                height="80px",
                border_radius="20px",
                background=gradient,
                display="flex",
                align_items="center",
                justify_content="center",
                margin_bottom="2rem",
                box_shadow=f"0 10px 30px {shadow_color}",
            ),
            
            rx.heading(title, size="6", color="white", margin_bottom="1rem", font_weight="bold", text_align="center"),
            rx.text(description, color="gray.300", text_align="center", margin_bottom="2rem", line_height="1.6", size="4"),
            
            # Features list with modern styling
            rx.vstack(
                *[rx.hstack(
                    rx.box(
                        rx.icon("check", size=14, color="white"),
                        width="24px",
                        height="24px",
                        border_radius="50%",
                        background="linear-gradient(135deg, #10B981, #059669)",
                        display="flex",
                        align_items="center",
                        justify_content="center",
                        flex_shrink="0",
                    ),
                    rx.text(feature, size="3", color="gray.300"),
                    spacing="3",
                    align="center",
                    width="100%",
                ) for feature in features],
                spacing="3",
                align="start",
                margin_bottom="2rem",
                width="100%",
            ),
            
            # Price with modern styling
            rx.text(price, size="6", font_weight="bold", color="white", margin_bottom="2rem", text_align="center"),
            
            # CTA Button with hover effects
            rx.button(
                "Get Started",
                size="3",
                background=gradient,
                color="white",
                border="none",
                border_radius="12px",
                width="100%",
                padding="0.75rem",
                font_weight="bold",
                box_shadow=f"0 8px 25px {shadow_color}",
                transition="all 0.3s ease",
                _hover={
                    "transform": "translateY(-3px)",
                    "box_shadow": f"0 12px 35px {shadow_color}"
                },
            ),
            
            spacing="3",
            align="center",
            width="100%",
        ),
        padding="2.5rem",
        background="rgba(255, 255, 255, 0.05)",
        border="1px solid rgba(255, 255, 255, 0.1)",
        border_radius="25px",
        backdrop_filter="blur(20px)",
        transition="all 0.3s ease",
        height="100%",
        _hover={
            "transform": "translateY(-8px)",
            "background": "rgba(255, 255, 255, 0.08)",
            "border_color": "rgba(139, 92, 246, 0.3)",
            "box_shadow": "0 20px 40px rgba(0, 0, 0, 0.3)"
        },
    )

def services_grid() -> rx.Component:
    """Grid of service offerings with modern design."""
    return rx.grid(
        service_card(
            "music",
            "Music Analysis",
            "Deep AI-powered analysis of your music preferences and listening patterns",
            [
                "Audio fingerprinting technology",
                "Mood and genre classification",
                "Tempo and key detection",
                "Personal listening insights",
            ],
            "Starting at $29/mo",
            "linear-gradient(135deg, #8B5CF6, #A855F7)",
            "rgba(139, 92, 246, 0.3)"
        ),
        service_card(
            "brain",
            "Smart Recommendations",
            "Personalized music suggestions powered by machine learning algorithms",
            [
                "AI-driven discovery engine",
                "Collaborative filtering",
                "Real-time preference learning",
                "Cross-platform integration",
            ],
            "Starting at $49/mo",
            "linear-gradient(135deg, #A855F7, #EC4899)",
            "rgba(168, 85, 247, 0.3)"
        ),
        service_card(
            "trending_up",
            "Trend Analytics",
            "Stay ahead with comprehensive music trend analysis and predictions",
            [
                "Global music trend tracking",
                "Emerging artist detection",
                "Genre popularity forecasting",
                "Cultural impact analysis",
            ],
            "Starting at $79/mo",
            "linear-gradient(135deg, #EC4899, #BE185D)",
            "rgba(236, 72, 153, 0.3)"
        ),
        service_card(
            "code",
            "Developer API",
            "Integrate our music intelligence into your own applications",
            [
                "RESTful API endpoints",
                "Real-time data streaming",
                "Comprehensive documentation",
                "24/7 developer support",
            ],
            "Starting at $199/mo",
            "linear-gradient(135deg, #10B981, #059669)",
            "rgba(16, 185, 129, 0.3)"
        ),
        service_card(
            "users",
            "Enterprise Solutions",
            "Custom music intelligence solutions for businesses and organizations",
            [
                "Custom model training",
                "Dedicated infrastructure",
                "Advanced analytics dashboard",
                "Priority support",
            ],
            "Custom Pricing",
            "linear-gradient(135deg, #F59E0B, #D97706)",
            "rgba(245, 158, 11, 0.3)"
        ),
        service_card(
            "headphones",
            "Premium Support",
            "White-glove support and consulting for all your music tech needs",
            [
                "24/7 expert support",
                "Personal account manager",
                "Custom integrations",
                "Strategy consulting",
            ],
            "Starting at $499/mo",
            "linear-gradient(135deg, #6366F1, #4F46E5)",
            "rgba(99, 102, 241, 0.3)"
        ),
        columns="3",
        spacing="6",
        width="100%",
        margin="4rem 0",
    )

def cta_section() -> rx.Component:
    """Modern call to action section."""
    return rx.box(
        # Background gradient
        rx.box(
            position="absolute",
            top="0",
            left="0",
            right="0",
            bottom="0",
            background="linear-gradient(135deg, rgba(139, 92, 246, 0.9), rgba(168, 85, 247, 0.8))",
            border_radius="25px",
            z_index="1",
        ),
        
        rx.vstack(
            rx.heading("Ready to Transform Your Music Experience?", size="7", text_align="center", color="white", font_weight="bold"),
            rx.text(
                "Join thousands of music lovers who've already discovered the power of AI-driven music intelligence. Get started today with a free trial.",
                size="4",
                text_align="center",
                color="rgba(255, 255, 255, 0.9)",
                margin_bottom="2rem",
                max_width="600px",
                line_height="1.6",
            ),
            rx.hstack(
                rx.button(
                    rx.hstack(
                        rx.text("Start Free Trial", font_weight="bold"),
                        rx.icon("arrow_right", size=18),
                        spacing="2",
                        align="center",
                    ),
                    size="4",
                    background="rgba(255, 255, 255, 0.2)",
                    color="white",
                    border="2px solid rgba(255, 255, 255, 0.3)",
                    border_radius="12px",
                    padding="1rem 2rem",
                    backdrop_filter="blur(10px)",
                    font_weight="bold",
                    transition="all 0.3s ease",
                    _hover={
                        "background": "rgba(255, 255, 255, 0.25)",
                        "border_color": "rgba(255, 255, 255, 0.5)",
                        "transform": "translateY(-2px)"
                    },
                ),
                rx.button(
                    rx.hstack(
                        rx.icon("phone", size=18),
                        rx.text("Schedule Demo", font_weight="bold"),
                        spacing="2",
                        align="center",
                    ),
                    size="4",
                    background="rgba(255, 255, 255, 0.1)",
                    color="white",
                    border="1px solid rgba(255, 255, 255, 0.2)",
                    border_radius="12px",
                    padding="1rem 2rem",
                    backdrop_filter="blur(10px)",
                    transition="all 0.3s ease",
                    _hover={
                        "background": "rgba(255, 255, 255, 0.15)",
                        "transform": "translateY(-2px)"
                    },
                ),
                spacing="4",
            ),
            spacing="4",
            align="center",
            z_index="2",
            position="relative",
        ),
        padding="4rem",
        margin="4rem 0",
        border_radius="25px",
        text_align="center",
        position="relative",
        overflow="hidden",
        box_shadow="0 20px 40px rgba(139, 92, 246, 0.3)",
    )

def services_page() -> rx.Component:
    """Complete modern services page."""
    return rx.vstack(
        services_hero(),
        services_grid(),
        cta_section(),
        spacing="0",
    )