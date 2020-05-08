from flask import Flask
from flask import render_template
from pandas_datareader import data

import datetime
app=Flask("_name_")
start=datetime.datetime(2014,9,1)
end=datetime.datetime(2014,9,10)
df=data.DataReader(name="GOOG",data_source="yahoo",start=start,end=end)
    
@app.route('/')
def hello_World():
    return render_template("college.html")

@app.route('/college/')
def college():
    return render_template("about.html")

@app.route('/data/')
def stock_data():
    return render_template("data.html",df=df)
@app.route('/plot/')
def plot():
   
    from bokeh.plotting import figure,show,output_file
    from bokeh.embed import components
    from bokeh.resources import CDN
    
    x=df["High"]
    y=df["Low"]
    f=figure()
    f.line(x,y)
    script1,div1= components(f)
    cdn_js=CDN.js_files[0]
    return render_template("plot.html",
    script1=script1,div1=div1,cdn_js=cdn_js)

if __name__=='__main__':
    app.run(debug=True)
