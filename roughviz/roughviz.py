from jinja2 import Template
from IPython.core.display import HTML
import random
import string
import json
import pkgutil
import pandas as pd

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

def stackedbar(labels, values, **kwargs):
    data = pkgutil.get_data(__package__, 'templates/stackedbar.html')
    template = Template(data.decode("utf-8"))
    id_name = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    data = []
    for index, row in pd.concat([labels,values],axis=1).iterrows():
        data.append(row.to_dict())
    output = template.render(id_name = id_name,
                             labels = labels.name,
                             values = data,
                             kwargs = kwargs)
    return HTML(output)
