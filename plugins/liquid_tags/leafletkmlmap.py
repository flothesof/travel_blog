"""
Leaflet KML map
---------------
This implements a Liquid-style map tag for Pelican that allows inserting a leafletjs map from a KML input file using the omnivore library.

Syntax
------
{% leafletkmlmap /path/to/map %}

Examples
--------
{% leafletkmlmap /path/to/map.kml %}

Output
------
<figure><img src="/images/ninja.png" alt="Ninja Attack!"><figcaption>Ninja Attack!</figcaption></figure>
"""
import re
from .mdx_liquid_tags import LiquidTags
import six

SYNTAX = '{% leafletkmlmap /path/to/map %}'

PART1 = """<div id="mapid" style="height: 350px;"></div>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.3.1/dist/leaflet.css"
integrity="sha512-Rksm5RenBEKSKFjgI3a41vrjkw4EVPlJ3+OiI65vTjIdo9brlAacEuKOiQ5OFh7cOI1bkDwLqdLw3Zg0cRJAAQ=="
crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.3.1/dist/leaflet.js"
integrity="sha512-/Nsx9X4HebavoBvEBuyp3I7od5tA0UzAxs+j83KgC8PU0kgB4XiK4Lfe4y4cgBtaRJQEIFCW+oC506aPT2L1zw=="
crossorigin=""></script>
<script src='https://api.mapbox.com/mapbox.js/plugins/leaflet-omnivore/v0.2.0/leaflet-omnivore.min.js'></script>
<script type="">
    var mymap = new L.Map('mapid', {center: new L.LatLng(15., 2.3522),
                                    zoom: 2,
                                    worldCopyJump: true});
    mymap.zoomControl.setPosition('topright');
    layer = L.tileLayer('http://a.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png', {
        attribution: '© Openstreetmap France | Données &copy; <a href="https://www.openstreetmap.org/copyright">les contributeurs OpenStreetMap</a>'});
    mymap.addLayer(layer); 
    var runLayer = omnivore.kml('"""
PART2 = """').on('ready', function() {
        mymap.fitBounds(runLayer.getBounds());
        runLayer.eachLayer(function(layer) {
           layer.bindPopup(layer.feature.properties.name);
        });
    }).addTo(mymap);
</script>"""


# Regular expression to match the entire syntax
pattern = re.compile("""(?P<path>\S.*)""")

@LiquidTags.register('leafletkmlmap')
def leafletkmlmap(preprocessor, tag, markup):
    attrs = None

    # Parse the markup string
    match = pattern.search(markup)
    if match:
        attrs = dict([(key, val.strip())
                      for (key, val) in six.iteritems(match.groupdict()) if val])
    else:
        raise ValueError('[leafletkmlmap] Error processing input. '
                         'Expected syntax: {0}. Input: {1}'.format(SYNTAX, markup))

    # Return the formatted tag
    tag = PART1 + attrs['path'] + PART2
    return tag

#----------------------------------------------------------------------
# This import allows the leafletkmlmap tag to be a Pelican plugin
from .liquid_tags import register

