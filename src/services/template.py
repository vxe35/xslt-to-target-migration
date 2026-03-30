from jinja2 import Environment, FileSystemLoader

class TemplateService:
    def __init__(self, template_dir="templates"):
        self.env = Environment(loader=FileSystemLoader(template_dir))

    def render_template(self, template_name, context):
        template = self.env.get_template(template_name)
        return template.render(context)