from flask import Flask, render_template, redirect, request, jsonify
from modelHelper import ModelHelper

# Create an instance of Flask
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

modelHelper = ModelHelper()

# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    # Return template and data
    return render_template("home.html")

@app.route("/ml")
def ml():
    # Return template and data
    return render_template("ml.html")

@app.route("/about_us")
def about_us():
    # Return template and data
    return render_template("about_us.html")

@app.route("/tableau")
def tableau():
    # Return template and data
    return render_template("tableau.html")

@app.route("/tableau2")
def tableau2():
    # Return template and data
    return render_template("tableau2.html")

@app.route("/works_cited")
def works_cited():
    # Return template and data
    return render_template("works_cited.html")

@app.route("/makePrediction", methods=["POST"])
def make_prediction():
    content = request.json["data"]
    print(content)

    # parse
    gender = content["gender"]
    customer_type = content["customer_type"]
    age = float(content["age"])
    travel_type = content["travel_type"]
    travel_class = content["travel_class"]
    distance = float(content["distance"])
    wifi = int(content["wifi"])
    time_convenience = int(content["time_convenience"])
    booking = int(content["booking"])
    gate = int(content["gate"])
    food = int(content["food"])
    boarding = int(content["boarding"])
    comfort = int(content["comfort"])
    entertainment = int(content["entertainment"])
    onboard_service = int(content["onboard_service"])
    legroom = int(content["legroom"])
    baggage = int(content["baggage"])
    checkin_service = int(content["checkin_service"])
    inflight_service = int(content["inflight_service"])
    cleanliness = int(content["cleanliness"])
    delay_d = float(content["delay_d"])
    delay_a = float(content["delay_a"])

    preds = modelHelper.makePrediction(gender, customer_type, age, travel_type, 
                                       travel_class, distance, wifi, time_convenience, 
                                       booking, gate, food, boarding, comfort, 
                                       entertainment, onboard_service, legroom, 
                                       baggage, checkin_service, inflight_service, 
                                       cleanliness, delay_d, delay_a)
    
    return(jsonify({"ok": True, "prediction": str(preds)}))


#############################################################

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

#main
if __name__ == "__main__":
    app.run(debug=True)
