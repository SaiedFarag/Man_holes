import matplotlib.pyplot as plt
import osmnx as ox
import geopandas as gpd
import folium
from folium.plugins import HeatMap
import webbrowser
from pyproj import crs
import networkx as nx
import osmnx.settings
from shapely.geometry import Point, LineString, Polygon

ox.settings.timeout = 1800

outPath = r'K:\G\Python\New folder\man_hole.shp'

place_name = "Kamppi, Helsinki, Finland"
matareyaData = 'West El Matareya'
vienna = 'Vienna'
usa = 'California'
# gdf = ox.geocode_to_gdf(usa)
# gdf.to_file(outPath)


# network = ox.graph_from_place(place_name)

# fig, ax = ox.plot_graph(network)
# plt.show()

# nodes, edges = ox.graph_to_gdfs(network)
# print(nodes.head())
# print(edges.head())

# area = ox.geocode_to_gdf(place_name)
# print(area)

tag_dict = {'tourism' : 'hotel'}
tagRest = {'amenity' : 'restaurant'}
tagATM = {'amenity' : 'atm'}
tagsPark = {'leisure': 'park', 'landuse': 'grass'}
man_hole = {'man_made' : 'manhole', 'manhole' : 'drain'}

# buildings = ox.geometries_from_place(place_name, tag_dict)
# restaurants = ox.geometries_from_place(place_name, tagRest)
# parks = ox.geometries_from_place(vienna, tagsPark)
# ATM = ox.geometries_from_place(vienna, tagATM)

buildingsM = ox.geometries_from_place(usa, man_hole)
# buildingsM = ox.geometries_from_place(polygon, tag_dict)
# buildingsM.plot()
# plt.show()

# print(len(ATM))
# print(type(ATM))

buildingsM.to_file(outPath)
# graph

# m = folium.Map(zoom_start=12, control_scale=True)
# #
# parks_gjson = folium.features.GeoJson(parks, name='Parks').add_to(m)
#
# ATM['x'] = ATM['geometry'].x
# ATM['y'] = ATM['geometry'].y
#
# atmLocations = list(zip(ATM['y'], ATM['x']))
#
# print('=' * 150)
# print(atmLocations)
# #
# HeatMap(atmLocations, name='Heat Map').add_to(m)
# #
# folium.LayerControl().add_to(m)
# m.save (r'K:\G\Python\New folder\ATM.html')
# webbrowser.open(r'K:\G\Python\New folder\ATM.html')
#
# shpTest = ox.graph_to_gdfs(ATM)
# shp = shpTest.to_file(outPath)

# cols = ['name', 'opening_hours', 'addr:city', 'addr:country', 'addr:housenumber', 'addr:postcode', 'addr:street']

# print(restaurants[cols].head(10))
# print(len(restaurants))
# print(restaurants.columns.values)

# fromPath = r'K:\G\Python\TEST.geojson'
#
# gdf = gpd.read_file(fromPath, driver='GeoJSON')
# polygon = gdf['geometry'].values[0]
# print(type(polygon))
# gJson = folium.features.GeoJson(gdf)
# print(gJson)

# graph = ox.graph_from_polygon(polygon)
# print(graph)
#
# fig, ax = ox.plot_graph(graph)