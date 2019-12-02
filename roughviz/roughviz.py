from jinja2 import Template
from IPython.core.display import display, HTML
import random
import string
import json
import pkgutil
import pandas as pd


def generate_template(data, labels, values, plot_svg, **kwargs):
    template = Template(data.decode("utf-8"))
    id_name = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    output = template.render(id_name = id_name,
                             labels = labels,
                             values = values,
                             kwargs = kwargs)
    if(plot_svg):
        svg_id = "svg"+id_name
        script = """
        <style>
        div.output_area img, div.output_area svg{
        height: 100%!important;
        }
        </style>
        <script>
            var e = document.getElementById('"""+id_name+"""');
            var divCheckingInterval = setInterval(function(){
            if(e.getElementsByTagName('svg').length){
                clearInterval(divCheckingInterval);
                e.getElementsByTagName('svg')[0].setAttribute("id", '"""+svg_id+"""');
                var svgElement = document.getElementById('"""+svg_id+"""');
                var svgString = new XMLSerializer().serializeToString(svgElement);
                var decoded = unescape(encodeURIComponent(svgString));
                var base64 = btoa(decoded);
                var imgSource = `data:image/svg+xml;base64,${base64}`;
                e.innerHTML = "<img id='svgplot'>";
                document.getElementById('svgplot').src = imgSource;       
            }}, 1);
        </script>
        """
        display(HTML(output))
        display(HTML(script))
    else:
        display(HTML(output))

def bar(labels, values, plot_svg = False, **kwargs):
    data = pkgutil.get_data(__package__, 'templates/bar.html')
    generate_template(data, labels.tolist(), values.tolist(), plot_svg, **kwargs)

def barh(labels, values, plot_svg = False, **kwargs):
    data = pkgutil.get_data(__package__, 'templates/barh.html')
    generate_template(data, labels.tolist(), values.tolist(), plot_svg, **kwargs)

def pie(labels, values, plot_svg = False, **kwargs):
    data = pkgutil.get_data(__package__, 'templates/pie.html')
    generate_template(data, labels.tolist(), values.tolist(), plot_svg, **kwargs)

def donut(labels, values, plot_svg = False, **kwargs):
    data = pkgutil.get_data(__package__, 'templates/donut.html')
    generate_template(data, labels.tolist(), values.tolist(), plot_svg, **kwargs)

def stackedbar(labels, values, plot_svg = False, **kwargs):
    data = pkgutil.get_data(__package__, 'templates/stackedbar.html')
    content = []
    for index, row in pd.concat([labels,values],axis=1).iterrows():
        content.append(row.to_dict())
    generate_template(data, labels.name, content, plot_svg, **kwargs)
