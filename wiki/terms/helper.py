from terms.models import Definition


def save_definition(name, definition=None, short_definition=None,
                    source=None, equation=None):
    d = Definition.objects.create(name=name, definition=definition,
                                  short_definition=short_definition,
                                  source=source, equation=equation)
    return d
