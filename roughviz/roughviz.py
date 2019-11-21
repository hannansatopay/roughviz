from jinja2 import Template
from IPython.core.display import HTML
import random
import string
import json
import pkgutil

def bar(labels, values, **kwargs):
    data = pkgutil.get_data(__package__, 'templates/bar.html')
    template = Template(data.decode("utf-8"))
    id_name = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    output = template.render(id_name = id_name,
                             labels = labels.tolist(),
                             values = values.tolist(),
                             kwargs = kwargs)
    return HTML(output)

def barh(labels, values, **kwargs):
    data = pkgutil.get_data(__package__, 'templates/barh.html')
    template = Template(data.decode("utf-8"))
    id_name = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    output = template.render(id_name = id_name,
                             labels = labels.tolist(),
                             values = values.tolist(),
                             kwargs = kwargs)
    return HTML(output)

def pie(labels, values, **kwargs):
    data = pkgutil.get_data(__package__, 'templates/pie.html')
    template = Template(data.decode("utf-8"))
    id_name = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    output = template.render(id_name = id_name,
                             labels = labels.tolist(),
                             values = values.tolist(),
                             kwargs = kwargs)
    return HTML(output)

def donut(labels, values, **kwargs):
    data = pkgutil.get_data(__package__, 'templates/donut.html')
    template = Template(data.decode("utf-8"))
    id_name = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    output = template.render(id_name = id_name,
                             labels = labels.tolist(),
                             values = values.tolist(),
                             kwargs = kwargs)
    return HTML(output)
