import folium
import pandas

html = """<h4>Volcano information:</h4>
Height: %s m
"""

data = pandas.read_csv("Volcanoes.txt")

lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])

def returnColor(elevation):
    if elevation<=1000:
        return 'green'
    elif 1000 <= elevation <= 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58,-99.09],zoom_start=6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup("Volcano")

for lt, ln, ele in zip(lat,lon,elev):
    iframe = folium.IFrame(html=html % str(ele), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius = 6, popup=str(ele)+" m",fill_color=returnColor(ele), color='grey',
    fill_opacity=0.7))
    #fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = returnColor(ele))))
#fg.add_child(folium.GeoJson(data=(open('world.json','r',encoding='utf-8-sig').read())))

fgp = folium.FeatureGroup("Population")

fgp.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig').read(), style_function=lambda x: {'fillColor':'green' 
            if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("first.html")