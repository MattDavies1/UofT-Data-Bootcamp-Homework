from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save reference to 'Measurement' table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Setup Flask
app = Flask(__name__)

# Flask Routes
# /
@app.route('/')
def welcome():
    return(
        f'Available Routes:<br/>'
        f'/api/v1.0/precipitation<br/>'
        f'/api/v1.0/stations<br/>'
        f'/api/v1.0/tobs<br/>'
        f'/api/v1.0/start<br/>'
        f'/api/v1.0/start/end<br/>')

# /api/v1.0/precipitation
@app.route('/api/v1.0/precipitation')
def precipitation():
    session = Session(engine)
    date = dt.datetime(2016, 8, 24)
    results = session.query(Measurement.date, Measurement.prcp)\
        .filter(Measurement.date > date)\
        .order_by(Measurement.date.desc())\
        .all()

    returns = {}

    for i in results:
        returns[i[0]]=[]

    for i in results:
        returns[i[0]].append(i[1])

    session.close()    

    return(jsonify(returns))

# /api/v1.0/stations
@app.route('/api/v1.0/stations')
def stations():
    session = Session(engine)
    result = session.query(Measurement.station.distinct()).all()
    session.close()

    return(jsonify([x[0] for x in result]))

# /api/v1.0/tobs
@app.route('/api/v1.0/tobs')
def tobs():
    session = Session(engine)
    date = dt.datetime(2016, 8, 24)
    result = session.query(Measurement.date, Measurement.tobs)\
        .filter(Measurement.station == 'USC00519281')\
        .filter(Measurement.date > date)\
        .all()
    session.close()

    t_dict = {}

    for i in result:
        t_dict[i[0]] = i[1]

    return(jsonify(t_dict))

# /api/v1.0/<start>
@app.route('/api/v1.0/<start>')

def dynamic1(start):
    try:
        session = Session(engine)

        date_list = start.split('-')
        date = dt.datetime(int(date_list[0]), int(date_list[1]), int(date_list[2]))
        
        result = session.query(func.avg(Measurement.tobs), func.min(Measurement.tobs), func.max(Measurement.tobs))\
            .filter(Measurement.date > date)\
            .all()

        t_stats = {}
        t_stats['Average'] = result[0][0]
        t_stats['Min'] = result[0][1]
        t_stats['Max'] = result[0][2]

        session.close()

        return(jsonify(t_stats))

    except:
        return(f'Input Date as format: YYYY-MM-DD')

# /api/v1.0/<start>/<end>
@app.route('/api/v1.0/<start>/<stop>')
def dynamic2(start, stop):
    try:
        session = Session(engine)

        start_date_list = start.split('-')
        start_date = dt.datetime(int(start_date_list[0]), int(start_date_list[1]), int(start_date_list[2]))
        start_date = start_date - dt.timedelta(days=1)

        stop_date_list = stop.split('-')
        stop_date = dt.datetime(int(stop_date_list[0]), int(stop_date_list[1]), int(stop_date_list[2]))
        
        result = session.query(func.avg(Measurement.tobs), func.min(Measurement.tobs), func.max(Measurement.tobs))\
        .filter(Measurement.date.between(start_date, stop_date))\
        .all()

        t_stats = {}
        t_stats['Average'] = result[0][0]
        t_stats['Min'] = result[0][1]
        t_stats['Max'] = result[0][2]

        session.close()

        return(jsonify(t_stats))

    except:
        return(f'Input Date as format: YYYY-MM-DD')
    
if __name__ == "__main__":
    app.run(debug=True)