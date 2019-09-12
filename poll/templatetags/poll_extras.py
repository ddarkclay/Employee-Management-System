from django import template
from poll.models import Question

register = template.Library()

# custom filter
def upper(value, n):
    """Convert string in Upper Case"""
    return value.upper()[0:n]

register.filter('upper',upper)                      # first method to register method

# custom template tag like for, if ,block, etc.
@register.simple_tag                                # second method to register method
def recent_polls(n=5, **kwargs):
    """Return Recent n Polls"""
    name = kwargs.get("name", "Argument not password")
    print(name)
    questions = Question.objects.all().order_by('-created_by')
    print(questions)
    return questions[0:n]