from jinja2 import Template
from IPython.core.display import HTML
import random
import string
import json
import pkgutil

def generate_template(data, labels, values, **kwargs):
    template = Template(data.decode("utf-8"))
    id_name = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    output = template.render(id_name = id_name,
                             labels = labels.tolist(),
                             values = values.tolist(),
                             kwargs = kwargs)
    return HTML(output)

def bar(labels, values, **kwargs):
    data = pkgutil.get_data(__package__, 'templates/bar.html')
    return generate_template(data, labels, values, **kwargs)

def barh(labels, values, **kwargs):
    data = pkgutil.get_data(__package__, 'templates/barh.html')
    return generate_template(data, labels, values, **kwargs)

def pie(labels, values, **kwargs):
    data = pkgutil.get_data(__package__, 'templates/pie.html')
    return generate_template(data, labels, values, **kwargs)

def donut(labels, values, **kwargs):
    data = pkgutil.get_data(__package__, 'templates/donut.html')
    return generate_template(data, labels, values, **kwargs)
