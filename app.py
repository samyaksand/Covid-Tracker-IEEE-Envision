import json, requests
import pandas as pd
import pygal
import plotly.express as px
from flask import Flask, render_template


# API for Table Cases Data----------------------------------------------------------

# API - to access web data
url = 'https://www.mohfw.gov.in/data/datanew.json' 

#perform GET request
res = requests.get(url)

#convert data into json
data = res.json()

# India Map-----------------------------------------------------------------------------------

data.pop()
df = pd.DataFrame(data)
df['active'] = df['active'].astype(int)

geojson_file = open('india.geojson','r')
geojson_data = json.load(geojson_file)


map = px.choropleth(
     
     df, locations = 'state_name',
     color = 'active',

     geojson = geojson_data,
     featureidkey  = 'properties.ST_NM',
     color_continuous_scale = 'Reds'
)

map.update_geos(fitbounds = 'locations', visible = False)
map.write_html('static/data/map.html')

#Initialize Bar Graph--------------------------------------------------------------------
plot1 = pygal.Bar()

plot1.title = 'Top 10 States with Highest Active Cases'

#Sort the data about 'new_active' key (in ascending order)
sorted_data = sorted(data, key = lambda x: int(x['new_active']), reverse = True)

#Take the Top 10 States and add them to the bar graph
for dict in sorted_data[1:11]:
    plot1.add(dict['state_name'], int(dict['new_active']))

#Save the bar graph file in the static folder
plot1.render_to_file('static/data/active.svg')

# --------------------------------------------------------------------------------------

plot2 = pygal.Bar()

plot2.title = 'Top 10 States with Highest Cases'

#Sort the data about 'new_active' key
sorted_data = sorted(data, key = lambda x: int(x['new_positive']), reverse = True)

#Take the Top 10 States and add them to the bar graph
for dict in sorted_data[1:11]:
   plot2.add(dict['state_name'], int(dict['new_positive']))

#Save the bar graph file in the static folder
plot2.render_to_file('static/data/positive.svg')

# ----------------------------------------------------------------------------------
plot3 = pygal.Bar()

plot3.title = 'Top 10 States with Highest Recovered Cases'

sorted_data = sorted(data, key = lambda x: int(x['new_cured']), reverse = True)

#Take the Top 10 States and add them to the bar graph
for dict in sorted_data[1:11]:
    plot3.add(dict['state_name'], int(dict['new_cured']))

#Save the bar graph file in the static folder
plot3.render_to_file('static/data/cured.svg')


# ----------------------------------------------------------------------------------
plot4 = pygal.Bar()

plot4.title = 'Top 10 States with Highest Death Cases'

sorted_data = sorted(data, key = lambda x: int(x['new_death']), reverse = True)

#Take the Top 10 States and add them to the bar graph
for dict in sorted_data[1:11]:
    plot4.add(dict['state_name'], int(dict['new_death']))

#Save the bar graph file in the static folder
plot4.render_to_file('static/data/death.svg')


# ----------------------------------------------------------------------------------

app=Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html', data = data)

if __name__=="__main__":
    app.run(debug=True)
