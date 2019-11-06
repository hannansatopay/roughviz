from jinja2 import Template
from IPython.core.display import HTML
import random
import string
import json
import pkgutil

def barplot(labels, values, **kwargs):

    data = pkgutil.get_data(__package__, 'templates/barplot.html')
    template = Template(data.decode("utf-8"))

    id_name = ''.join(random.choice(string.ascii_lowercase) for i in range(10))

    output = template.render(id_name=id_name,
                             labels=labels.tolist(),
                             values=values.tolist(),
                             kwargs = kwargs)

    return HTML(output)
