from fastapi.templating import Jinja2Templates
from pathlib import Path

# Configuración de templates
email_templates = Jinja2Templates(
    directory=Path(__file__).parent.parent.parent / "templates/emails"
)

def render_email_template(template_name: str, context: dict):
    template = email_templates.get_template(template_name)
    return template.render(context)