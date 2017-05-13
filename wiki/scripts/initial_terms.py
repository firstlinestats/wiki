import os
import re
import sys
import csv
import json
import django

sys.path.append(os.path.join(os.path.dirname(__file__), "wiki"))
sys.path.append("../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wiki.settings")
from django.conf import settings

django.setup()

from terms.models import Definition
from terms.helper import save_definition


def ingest_initial():
    with open('initial_db.csv', 'r') as csvfile:
        headers = []
        defreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in defreader:
            if not headers:
                headers = row
            else:
                info = {}
                for h in xrange(len(headers)):
                    name = headers[h]
                    value = row[h]
                    info[name] = value
                    d = Definition(**info)
                    d.save()


def find_missing():
    existing = {}
    for d in Definition.objects.all():
        existing[d.name] = d

    missing = set()
    for d in Definition.objects.filter(equation__isnull=False):
        eq = d.equation
        for val in re.findall(r'{\s(.*?)\s}', eq):
            if val not in existing:
                missing.add(val)

    for m in missing:
        print m


if __name__ == "__main__":
    ingest_initial()
    # find_missing()
