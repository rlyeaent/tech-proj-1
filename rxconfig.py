import reflex as rx

config = rx.Config(
    app_name="tech_proj_1",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)