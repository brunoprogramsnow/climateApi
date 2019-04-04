from flask import Flask,jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import inspect

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)
inspector = inspect(engine)
twelve_months = session.query(Measurement.prcp, Measurement.date).filter(Measurement.date >='2016-08-23').filter(Measurement.date <='2017-08-23').all()
station = engine.execute('SELECT station FROM Measurement').fetchall()


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
    list_twelve_months = list(twelve_months)
    return jsonify(list_twelve_months)

@app.route("/api/v1.0/stations")
def stations():
   
    return jsonify([dict(row) for row in station])

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