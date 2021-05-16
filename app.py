import requests, json
from flask import Flask, render_template
import pygal

app=Flask(__name__)

#----------------------------------------------------------
# API - to access web data
url = 'https://www.mohfw.gov.in/data/datanew.json' 

#perform GET request
res = requests.get(url)

#convert data into json
data = res.json()

#-----------------------------------------------------------------------------------

#Initialize Bar Graph
plot1 = pygal.Bar()

plot1.title = 'Top 10 States with Highest Active Cases'

#Sort the data about 'new_active' key
sorted_data = sorted(data, key = lambda x: int(x['new_active']), reverse = True)

#Take the Top 10 States and add them to the bar graph
for dict in sorted_data[1:11]:
    plot1.add(dict['state_name'], int(dict['new_active']))

#Save the bar graph file in the static folder
plot1.render_to_file('static/data/active.svg')

# --------------------------------------------------------------------------------------

plot2 = pygal.Bar()

plot2.title = 'Top 10 States with Highest Positive Cases'

#Sort the data about 'new_active' key
sorted_data = sorted(data, key = lambda x: int(x['new_positive']), reverse = True)

#Take the Top 10 States and add them to the bar graph
for dict in sorted_data[1:11]:
   plot2.add(dict['state_name'], int(dict['new_positive']))

#Save the bar graph file in the static folder
plot2.render_to_file('static/data/positive.svg')

# ----------------------------------------------------------------------------------

@app.route('/')
def home_page():
    return render_template('index.html', data = data)

if __name__=="__main__":
    app.run(debug=True)
