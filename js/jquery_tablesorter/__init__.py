from fanstatic import Library, Resource
from js.jquery import jquery

library = Library('jquery tablesorter', 'resources')

tablesorter = Resource(library, 'jquery.tablesorter.js',
    minified='jquery.tablesorter.min.js', depends=[jquery])

blue = Resource(library, 'themes/blue/style.css')

green = Resource(library, 'themes/green/style.css')

