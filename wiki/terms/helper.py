from terms.models import Definition

import re


def save_definition(name, definition=None, short_definition=None,
                    source=None, equation=None):
    d = Definition.objects.create(name=name, definition=definition,
                                  short_definition=short_definition,
                                  source=source, equation=equation)
    return d


def find_definition_terms(eq):
    terms = re.findall(r'{\s+=*(.*?)\s*}', eq)
    return terms


def find_complete_definitions():
    queryset = Definition.objects.filter(equation__contains="{")
    defs = {}
    for q in queryset:
        name = q.name
        equation = q.equation
        if not equation:
            equation = name
        else:
            equation = '({})'.format(equation)
        defs[name] = equation
    results = {}
    for q in queryset:
        name = q.name
        equation = defs[name]
        # If this is a base stat
        if not equation:
            defs[name] = name
            continue
        terms = find_definition_terms(equation)
        original_form = equation.replace("{ ", "").replace(" }", "")
        while terms:
            equations = {}
            for term in terms:
                if term in defs:
                    equations[term] = defs[term]
                else:
                    equations[term] = term
            equation = equation.replace("{ ", "{").replace(" }", "}").format(**equations)
            terms = find_definition_terms(equation)
        defs[name] = equation
        if len(equation) == len(original_form) + 2:
            equation = original_form
        results[name] = {"equation": original_form,
                         "expanded": equation,
                         "definition": q.definition}
    return results
