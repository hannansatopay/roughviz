# roughviz

![roughviz](https://user-images.githubusercontent.com/7835634/69475723-6bce0080-0df6-11ea-8f36-82128cc108ac.jpg)

roughviz is a python visualization library for creating sketchy/hand-drawn styled charts.

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://github.com/hannansatopay)

### Available Charts
<ul>
  <li>Bar (<code>roughviz.bar</code>) </li>
  <li>Horizontal Bar (<code>roughviz.barh</code>) </li>
  <li>Pie (<code>roughviz.pie</code>) </li>
  <li>Donut (<code>roughviz.donut</code>) </li>
  <li>Stacked Bar (<code>roughviz.stackedbar</code>) </li>
</ul>

### Installation
[![PyPI](https://img.shields.io/pypi/v/roughviz?color=dark%20green&style=for-the-badge)](https://pypi.org/project/roughviz/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/roughviz?color=dark%20green&style=for-the-badge)](https://pypi.org/project/roughviz/)
```
pip install roughviz
```

### Usage
```
import roughviz
import pandas as pd 
d = {'col1': [1, 2, 3, 4, 5], 'col2': [3, 4, 10, 2, 0.9]}
df = pd.DataFrame(data=d)
roughviz.bar(df["col1"], df["col2"])
```
Note: The library works seamlessly with Jupyter Notebook

### API
The API Documentation is available on: [Wiki](https://github.com/hannansatopay/roughviz/wiki/API)

### Future Plans
- [ ] Exception Handling
- [ ] Add Chart: Histogram
- [ ] Add Chart: Scatter
- [ ] Add Chart: Bubble Chart
- [ ] Add Chart: Line
- [ ] Advance CSS control capabilities

### Based on
<a href="https://github.com/jwilber/roughViz"><img src="https://raw.githubusercontent.com/jwilber/random_data/master/roughViz_Title.png"  width="350" alt="roughViz.js"><a>

### License
MIT License

Copyright (c) 2019 Hannan Satopay

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
