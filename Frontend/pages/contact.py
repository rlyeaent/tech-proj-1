"""Modern contact page component with dark theme."""

import reflex as rx

class ContactState(rx.State):
    """State for contact form."""
    name: str = ""
    email: str = ""
    subject: str = ""
    message: str = ""
    submitted: bool = False

    def submit_form(self):
        """Handle form submission."""
        if self.name and self.email and self.message:
            self.submitted = True
        return rx.toast.success("Message sent successfully!")

    def reset_form(self):
        """Reset the form."""
        self.name = ""
        self.email = ""
        self.subject = ""
        self.message = ""
        self.submitted = False

def contact_hero() -> rx.Component:
    """Modern contact page hero section."""
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
                "CONTACT US",
                size="3",
                color="purple.400",
                font_weight="bold",
                letter_spacing="0.2em",
                text_align="center",
                margin_bottom="1rem",
            ),
            rx.heading(
                "Let's Start a Conversation", 
                size="8", 
                text_align="center", 
                color="white",
                font_weight="bold",
                margin_bottom="1rem",
            ),
            rx.text(
                "Have questions about our services? Want to explore a partnership? We'd love to hear from you and discuss how Resonance can transform your music experience.",
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

def contact_info_card(icon: str, title: str, info1: str, gradient: str, shadow_color: str, info2: str = None) -> rx.Component:
    """Modern contact info card."""
    return rx.box(
        rx.vstack(
            rx.box(
                rx.icon(icon, size=32, color="white"),
                width="70px",
                height="70px",
                border_radius="18px",
                background=gradient,
                display="flex",
                align_items="center",
                justify_content="center",
                margin_bottom="1.5rem",
                box_shadow=f"0 8px 25px {shadow_color}",
            ),
            rx.heading(title, size="5", color="white", margin_bottom="1rem", font_weight="bold"),
            rx.vstack(
                rx.text(info1, color="gray.300", size="3", text_align="center"),
                rx.text(info2, color="gray.300", size="3", text_align="center") if info2 else rx.fragment(),
                spacing="1",
                align="center",
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
    )

def contact_info_section() -> rx.Component:
    """Modern contact information section."""
    return rx.vstack(
        rx.text(
            "GET IN TOUCH",
            size="3",
            color="purple.400",
            font_weight="bold",
            letter_spacing="0.2em",
            text_align="center",
            margin_bottom="1rem",
        ),
        rx.heading("How to Reach Us", size="7", text_align="center", color="white", margin_bottom="4rem", font_weight="bold"),
        
        rx.grid(
            contact_info_card(
                "mail",
                "Email Us",
                "hello@resonance.com",
                "We'll respond within 24 hours",
                "linear-gradient(135deg, #8B5CF6, #A855F7)",
                "rgba(139, 92, 246, 0.3)"
            ),
            contact_info_card(
                "phone",
                "Call Us",
                "+1 (555) 123-4567",
                "Mon-Fri, 9AM-6PM PST",
                "linear-gradient(135deg, #A855F7, #EC4899)",
                "rgba(168, 85, 247, 0.3)"
            ),
            contact_info_card(
                "map_pin",
                "Visit Us",
                "123 Innovation Drive",
                "San Francisco, CA 94105",
                "linear-gradient(135deg, #10B981, #059669)",
                "rgba(16, 185, 129, 0.3)"
            ),
            columns="3",
            spacing="6",
            width="100%",
        ),
        spacing="4",
        margin_bottom="6rem",
    )

def contact_form() -> rx.Component:
    """Modern contact form section."""
    return rx.box(
        rx.cond(
            ContactState.submitted,
            # Success state
            rx.vstack(
                rx.box(
                    rx.icon("check_circle", size=64, color="white"),
                    width="100px",
                    height="100px",
                    border_radius="50%",
                    background="linear-gradient(135deg, #10B981, #059669)",
                    display="flex",
                    align_items="center",
                    justify_content="center",
                    margin_bottom="2rem",
                    box_shadow="0 15px 35px rgba(16, 185, 129, 0.4)",
                ),
                rx.heading("Message Sent!", size="6", color="white", font_weight="bold", margin_bottom="1rem"),
                rx.text("Thank you for reaching out! We'll get back to you within 24 hours.", color="gray.300", size="4", text_align="center", margin_bottom="2rem"),
                rx.button(
                    "Send Another Message",
                    on_click=ContactState.reset_form,
                    size="3",
                    background="linear-gradient(135deg, #8B5CF6, #A855F7)",
                    color="white",
                    border="none",
                    border_radius="12px",
                    padding="0.75rem 2rem",
                    font_weight="bold",
                    box_shadow="0 8px 25px rgba(139, 92, 246, 0.3)",
                    transition="all 0.3s ease",
                    _hover={
                        "transform": "translateY(-2px)",
                        "box_shadow": "0 12px 35px rgba(139, 92, 246, 0.4)"
                    },
                ),
                spacing="3",
                align="center",
                text_align="center",
                padding="4rem 2rem",
            ),
            
            # Contact form
            rx.vstack(
                rx.heading("Send us a Message", size="6", color="white", margin_bottom="2rem", font_weight="bold", text_align="center"),
                
                rx.vstack(
                    # Name input
                    rx.vstack(
                        rx.text("Your Name", color="gray.300", size="3", font_weight="medium", margin_bottom="0.5rem"),
                        rx.input(
                            placeholder="Enter your full name",
                            value=ContactState.name,
                            on_change=ContactState.set_name,
                            size="3",
                            width="100%",
                            background="rgba(255, 255, 255, 0.05)",
                            border="1px solid rgba(255, 255, 255, 0.1)",
                            border_radius="10px",
                            color="white",
                            padding="1rem",
                            _focus={
                                "border_color": "rgba(139, 92, 246, 0.5)",
                                "box_shadow": "0 0 0 3px rgba(139, 92, 246, 0.1)"
                            },
                        ),
                        spacing="2",
                        align="start",
                        width="100%",
                    ),
                    
                    # Email input
                    rx.vstack(
                        rx.text("Email Address", color="gray.300", size="3", font_weight="medium", margin_bottom="0.5rem"),
                        rx.input(
                            placeholder="your.email@example.com",
                            value=ContactState.email,
                            on_change=ContactState.set_email,
                            type="email",
                            size="3",
                            width="100%",
                            background="rgba(255, 255, 255, 0.05)",
                            border="1px solid rgba(255, 255, 255, 0.1)",
                            border_radius="10px",
                            color="white",
                            padding="1rem",
                            _focus={
                                "border_color": "rgba(139, 92, 246, 0.5)",
                                "box_shadow": "0 0 0 3px rgba(139, 92, 246, 0.1)"
                            },
                        ),
                        spacing="2",
                        align="start",
                        width="100%",
                    ),
                    
                    # Subject input
                    rx.vstack(
                        rx.text("Subject", color="gray.300", size="3", font_weight="medium", margin_bottom="0.5rem"),
                        rx.input(
                            placeholder="What's this about?",
                            value=ContactState.subject,
                            on_change=ContactState.set_subject,
                            size="3",
                            width="100%",
                            background="rgba(255, 255, 255, 0.05)",
                            border="1px solid rgba(255, 255, 255, 0.1)",
                            border_radius="10px",
                            color="white",
                            padding="1rem",
                            _focus={
                                "border_color": "rgba(139, 92, 246, 0.5)",
                                "box_shadow": "0 0 0 3px rgba(139, 92, 246, 0.1)"
                            },
                        ),
                        spacing="2",
                        align="start",
                        width="100%",
                    ),
                    
                    # Message textarea
                    rx.vstack(
                        rx.text("Message", color="gray.300", size="3", font_weight="medium", margin_bottom="0.5rem"),
                        rx.text_area(
                            placeholder="Tell us more about your project, questions, or how we can help...",
                            value=ContactState.message,
                            on_change=ContactState.set_message,
                            rows="6",
                            width="100%",
                            resize="vertical",
                            background="rgba(255, 255, 255, 0.05)",
                            border="1px solid rgba(255, 255, 255, 0.1)",
                            border_radius="10px",
                            color="white",
                            padding="1rem",
                            _focus={
                                "border_color": "rgba(139, 92, 246, 0.5)",
                                "box_shadow": "0 0 0 3px rgba(139, 92, 246, 0.1)"
                            },
                        ),
                        spacing="2",
                        align="start",
                        width="100%",
                    ),
                    
                    # Submit button
                    rx.button(
                        rx.hstack(
                            rx.text("Send Message", font_weight="bold"),
                            rx.icon("send", size=18),
                            spacing="2",
                            align="center",
                        ),
                        on_click=ContactState.submit_form,
                        size="4",
                        background="linear-gradient(135deg, #8B5CF6, #A855F7)",
                        color="white",
                        border="none",
                        border_radius="12px",
                        width="100%",
                        padding="1rem",
                        font_weight="bold",
                        box_shadow="0 8px 25px rgba(139, 92, 246, 0.3)",
                        transition="all 0.3s ease",
                        disabled=~((ContactState.name != "") & (ContactState.email != "") & (ContactState.message != "")),
                        _hover={
                            "transform": "translateY(-2px)",
                            "box_shadow": "0 12px 35px rgba(139, 92, 246, 0.4)"
                        },
                        _disabled={
                            "background": "rgba(107, 114, 128, 0.5)",
                            "cursor": "not-allowed",
                            "transform": "none",
                            "box_shadow": "none"
                        },
                    ),
                    
                    spacing="6",
                    width="100%",
                ),
                
                spacing="4",
                align="center",
                width="100%",
            ),
        ),
        padding="3rem",
        background="rgba(255, 255, 255, 0.05)",
        border="1px solid rgba(255, 255, 255, 0.1)",
        border_radius="25px",
        backdrop_filter="blur(20px)",
        max_width="600px",
        margin="0 auto",
    )

def contact_content() -> rx.Component:
    """Main contact content section."""
    return rx.vstack(
        contact_info_section(),
        contact_form(),
        spacing="6",
        width="100%",
    )

def contact_page() -> rx.Component:
    """Complete modern contact page."""
    return rx.vstack(
        contact_hero(),
        contact_content(),
        spacing="0",
    )