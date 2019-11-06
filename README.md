
roughviz is a python visualization library for creating sketchy/hand-drawn styled charts.

### Available Charts
<ul>
  <li>Bar (<code>roughviz.bar</code>) </li>
  <li>Horizontal Bar (<code>roughviz.barh</code>) </li>
  <li>Pie (<code>roughviz.pie</code>) </li>
  <li>Donut (<code>roughviz.donut</code>) </li>
</ul>

### Installation
```
pip install roughviz
```

<h2 id="API">API</h2>

### <code id="Bar">roughviz.bar</code>
Required
- `labels`: Labels with which to construct chart.
- `values`: Values with which to construct chart.
```
roughviz.bar(df["ABC"], df["XYZ"])
```

Optional
- `axisFontSize` [string]: Font-size for axes' labels. Default: `'1rem'`.
- `axisRoughness` [number]: Roughness for x & y axes. Default: `0.5`.
- `axisStrokeWidth` [number]: Stroke-width for x & y axes. Default: `0.5`.
- `bowing` [number]: Chart bowing. Default: `0`.
- `color` [string]: Color for each bar. Default: `'skyblue'`.
- `fillStyle` [string]: Bar fill-style.
- `fillWeight` [number]: Weight of inner paths' color. Default: `0.5`.
- `font`: Font-family to use. You can use `0` or `gaegu` to use `Gaegu`, or `1` or `indie flower` to use `Indie Flower`. Or feed it something else. Default: `Gaegu`.
- `highlight` [string]: Color for each bar on hover. Default: `'coral'`.
- `innerStrokeWidth` [number]: Stroke-width for paths inside bars. Default: `1`.
- `labelFontSize` [string]: Font-size for axes' labels. Default: `'1rem'`.
- `padding` [number]: Padding between bars. Default: `0.1`.
- `roughness` [number]: Roughness level of chart. Default: `1`.
- `simplification` [number]: Chart simplification. Default `0.2`.
- `stroke` [string]: Color of bars' stroke. Default: `black`.
- `strokeWidth` [number]: Size of bars' stroke. Default: `1`.
- `title` [string]: Chart title. Optional.
- `titleFontSize` [string]: Font-size for chart title. Default: `'1rem'`.
- `tooltipFontSize` [string]: Font-size for tooltip. Default: `'0.95rem'`.
- `xLabel` [string]: Label for x-axis.
- `yLabel` [string]: Label for y-axis.
- `width` [number]: Width of the chart (in pixels).
- `height` [number]: Height of the chart (in pixels).

### <code id="BarH">roughviz.barh</code>
Required
- `labels`: Labels with which to construct chart.
- `values`: Values with which to construct chart.
```
roughviz.barh(df["ABC"], df["XYZ"])
```

Optional
- `axisFontSize` [string]: Font-size for axes' labels. Default: `'1rem'`.
- `axisRoughness` [number]: Roughness for x & y axes. Default: `0.5`.
- `axisStrokeWidth` [number]: Stroke-width for x & y axes. Default: `0.5`.
- `bowing` [number]: Chart bowing. Default: `0`.
- `color` [string]: Color for each bar. Default: `'skyblue'`.
- `fillStyle` [string]: Bar fill-style.
- `fillWeight` [number]: Weight of inner paths' color. Default: `0.5`.
- `font`: Font-family to use. You can use `0` or `gaegu` to use `Gaegu`, or `1` or `indie flower` to use `Indie Flower`. Or feed it something else. Default: `Gaegu`.
- `highlight` [string]: Color for each bar on hover. Default: `'coral'`.
- `innerStrokeWidth` [number]: Stroke-width for paths inside bars. Default: `1`.
- `labelFontSize` [string]: Font-size for axes' labels. Default: `'1rem'`.
- `padding` [number]: Padding between bars. Default: `0.1`.
- `roughness` [number]: Roughness level of chart. Default: `1`.
- `simplification` [number]: Chart simplification. Default `0.2`.
- `stroke` [string]: Color of bars' stroke. Default: `black`.
- `strokeWidth` [number]: Size of bars' stroke. Default: `1`.
- `title` [string]: Chart title. Optional.
- `titleFontSize` [string]: Font-size for chart title. Default: `'1rem'`.
- `tooltipFontSize` [string]: Font-size for tooltip. Default: `'0.95rem'`.
- `xLabel` [string]: Label for x-axis.
- `yLabel` [string]: Label for y-axis.
- `width` [number]: Width of the chart (in pixels).
- `height` [number]: Height of the chart (in pixels).

### <code id="Donut">roughviz.donut</code>
Required
- `labels`: Labels with which to construct chart.
- `values`: Values with which to construct chart.
```
roughviz.donut(df["ABC"], df["XYZ"])
```

Optional
- `bowing` [number]: Chart bowing. Default: `0`.
- `fillStyle` [string]: Chart fill-style.
- `fillWeight` [number]: Weight of inner paths' color. Default: `0.85`.
- `font`: Font-family to use. You can use `0` or `gaegu` to use `Gaegu`, or `1` or `indie flower` to use `Indie Flower`. Or feed it something else. Default: `Gaegu`.
- `highlight` [string]: Color for each arc on hover. Default: `'coral'`.
- `innerStrokeWidth` [number]: Stroke-width for paths inside arcs. Default: `0.75`.
- `roughness` [number]: Roughness level of chart. Default: `1`.
- `simplification` [number]: Chart simplification. Default `0.2`.
- `strokeWidth` [number]: Size of bars' stroke. Default: `1`.
- `title` [string]: Chart title. Optional.
- `titleFontSize` [string]: Font-size for chart title. Default: `'1rem'`.
- `tooltipFontSize` [string]: Font-size for tooltip. Default: `'0.95rem'`.

### <code id="Pie">roughviz.pie</code>
Required
- `labels`: Labels with which to construct chart.
- `values`: Values with which to construct chart.
```
roughviz.pie(df["ABC"], df["XYZ"])
```

Optional
- `bowing` [number]: Chart bowing. Default: `0`.
- `fillStyle` [string]: Chart fill-style.
- `fillWeight` [number]: Weight of inner paths' color. Default: `0.85`.
- `font`: Font-family to use. You can use `0` or `gaegu` to use `Gaegu`, or `1` or `indie flower` to use `Indie Flower`. Or feed it something else. Default: `Gaegu`.
- `highlight` [string]: Color for each arc on hover. Default: `'coral'`.
- `innerStrokeWidth` [number]: Stroke-width for paths inside arcs. Default: `0.75`.
- `roughness` [number]: Roughness level of chart. Default: `1`.
- `simplification` [number]: Chart simplification. Default `0.2`.
- `strokeWidth` [number]: Size of bars' stroke. Default: `1`.
- `title` [string]: Chart title. Optional.
- `titleFontSize` [string]: Font-size for chart title. Default: `'1rem'`.
- `tooltipFontSize` [string]: Font-size for tooltip. Default: `'0.95rem'`.

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
