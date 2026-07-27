"""Template engine for project generation."""

from pathlib import Path
from typing import Any, Dict

from jinja2 import Environment, FileSystemLoader, Template


class TemplateEngine:
    """Jinja2-based template engine with custom filters."""

    def __init__(self, templates_dir: Path) -> None:
        """Initialize template engine.
        
        Args:
            templates_dir: Directory containing template files
        """
        self.env = Environment(
            loader=FileSystemLoader(str(templates_dir)),
            trim_blocks=True,
            lstrip_blocks=True,
        )
        self._register_filters()

    def _register_filters(self) -> None:
        """Register custom Jinja2 filters."""
        self.env.filters["snake_case"] = self._snake_case
        self.env.filters["pascal_case"] = self._pascal_case
        self.env.filters["kebab_case"] = self._kebab_case

    @staticmethod
    def _snake_case(value: str) -> str:
        """Convert string to snake_case.
        
        Args:
            value: Input string
            
        Returns:
            Snake case string
        """
        import re
        s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", value)
        return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()

    @staticmethod
    def _pascal_case(value: str) -> str:
        """Convert string to PascalCase.
        
        Args:
            value: Input string
            
        Returns:
            PascalCase string
        """
        return "".join(word.capitalize() for word in value.replace("-", "_").split("_"))

    @staticmethod
    def _kebab_case(value: str) -> str:
        """Convert string to kebab-case.
        
        Args:
            value: Input string
            
        Returns:
            Kebab case string
        """
        import re
        s1 = re.sub("(.)([A-Z][a-z]+)", r"\1-\2", value)
        return re.sub("([a-z0-9])([A-Z])", r"\1-\2", s1).lower()

    def render_file(self, template_name: str, context: Dict[str, Any]) -> str:
        """Render a template file.
        
        Args:
            template_name: Name of the template file
            context: Template variables
            
        Returns:
            Rendered content
            
        Raises:
            jinja2.TemplateNotFound: If template not found
        """
        template = self.env.get_template(template_name)
        return template.render(**context)

    def render_string(self, content: str, context: Dict[str, Any]) -> str:
        """Render a template string.
        
        Args:
            content: Template content
            context: Template variables
            
        Returns:
            Rendered content
        """
        template = Template(content)
        return template.render(**context)
