import requests
import json
import pygal
from flask import Flask, render_template

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


plot_TC.title = 'total cases'
plot_new_dead.tile = 'NEW DEATHS'
plot_cured.title = 'CURED'

# basically sort the data in acending order
sorted_data = sorted(data, key=lambda x: int(x['new_active']))

sorted_data_death = sorted(data, key=lambda x: int(x['new_death']))  #for the deaths

sorted_data_cured = sorted(data, key=lambda x: int(x['cured'])) #for cured



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





@app.route('/')
def home_page():
    return render_template('index p1.html', data=data)

@app.route('/dead_graph')
def dead_graph():
    return render_template('dead_graph.html')

    


if __name__ == "__main__":
    app.run(debug=True)
