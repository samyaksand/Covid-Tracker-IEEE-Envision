import requests
import json
import pygal
from flask import Flask, render_template
#import pandarequest
import pandas as pd
import plotly.express as px

app = Flask(__name__)

# API - to access web data

url = 'https://www.mohfw.gov.in/data/datanew.json'

# perform GET request
res = requests.get(url)

# convert data into json
data = res.json()

#print(data)

plot_TC = pygal.Bar()
plot_new_dead =  pygal.Bar()
plot_cured = pygal.Bar()
plot_newpositive = pygal.Bar()


plot_TC.title = 'total cases'
plot_new_dead.tile = 'NEW DEATHS'
plot_cured.title = 'CURED'
plot_newpositive.title = 'NEW POSITIVE'




# basically sort the data in acending order
sorted_data = sorted(data, key=lambda x: int(x['new_active']))

sorted_data_death = sorted(data, key=lambda x: int(x['new_death']))  #for the deaths

sorted_data_cured = sorted(data, key=lambda x: int(x['cured'])) #for cured

sorted_data_newpositive = sorted(data, key = lambda x :int(x['new_positive']))#new positive





#this is for the template tile========================================================
for dict in sorted_data[1:11]:
    plot_TC.add(dict['state_name'], int(dict['new_active']))

plot_TC.render_to_file('static/data/active.svg')
#======================================================================================

#for separate web page active cases====================================================
for dict in sorted_data[1:25]:
    plot_TC.add(dict['state_name'], int(dict['new_active']))

plot_TC.render_to_file('static/data/active_long.svg')
#======================================================================================





#this is for the template tile========================================================
for dict in sorted_data_death[1:11]:
    plot_new_dead.add(dict['state_name'], int(dict['new_death']))

plot_new_dead.render_to_file('static/data/active_ded.svg')
#======================================================================================

#for separate web page death cases=====================================================
for dict in sorted_data_death[1:25]:
    plot_new_dead.add(dict['state_name'], int(dict['new_death']))

plot_new_dead.render_to_file('static/data/active_ded_long.svg')
#======================================================================================





#this is for the template tile========================================================
for dict in sorted_data_cured[1:11]:
    plot_cured. add (dict['state_name'], int(dict['cured']))

plot_cured.render_to_file('static/data/active_cured.svg')
#======================================================================================

#for separate web page CURED cases=====================================================
for dict in sorted_data_cured[1:25]:
    plot_cured.add(dict['state_name'], int(dict['cured']))

plot_cured.render_to_file('static/data/active_cured_long.svg')
#======================================================================================






#this is for the template tile========================================================
for dict in sorted_data_newpositive[1:11]:
    plot_newpositive. add (dict['state_name'], int(dict['new_positive']))

plot_newpositive.render_to_file('static/data/positive.svg')
#======================================================================================

#for separate web page CURED cases=====================================================
for dict in sorted_data_newpositive[1:25]:
    plot_newpositive.add(dict['state_name'], int(dict['new_positive']))

plot_newpositive.render_to_file('static/data/positive_long.svg')
#======================================================================================


#maps::================================================================================

data.pop()
df = pd.DataFrame(data)
df['active'] = df['active'].astype(int)

geojson_file = open('india.geojson','r')
geojson_data = json.load(geojson_file)

map = px.choropleth(
    df,
    locations = 'state_name',

    color = 'active',

    geojson = geojson_data,
    featureidkey = 'properties.ST_NM',

    color_continuous_scale = 'curl'
)

map.update_geos(fitbounds = 'locations')

map.write_html('static/data/map.html')

#======================================================================================


@app.route('/')
def home_page():
    return render_template('index.html', data=data)

@app.route('/dead_graph')
def dead_graph():
    return render_template('dead_graph.html')

@app.route('/graph')
def graph():
    return render_template('graph.html')
 
@app.route('/cured')
def cured():
    return render_template('cured.html')

@app.route('/newpositive')
def newpositive():
    return render_template('newpositive.html')



if __name__ == "__main__":
    app.run(debug=True)
