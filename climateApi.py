from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return (
        f"Here are the available routes in this api:<br/><br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    return(f"working")

@app.route("/api/v1.0/stations")
def stations():
    return(f"working")

@app.route("/api/v1.0/tobs")
def tobs():
    return(f"working")

@app.route("/api/v1.0/<start>")
def start():
    return(f"working")

@app.route("/api/v1.0/<start>/<end>")
def startEnd():
    return(f"working")


if __name__ == "__main__":
    app.run(debug=True)