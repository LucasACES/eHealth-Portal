from django import template

register = template.Library()

@register.filter
def startswith(text, prefix):
    """Verifica se a string começa com o prefixo dado."""
    if isinstance(text, str):
        return text.startswith(prefix)
    return False

@register.filter
def endswith(text, suffix):
    """Verifica se a string termina com o sufixo dado."""
    if isinstance(text, str):
        return text.endswith(suffix)
    return False
