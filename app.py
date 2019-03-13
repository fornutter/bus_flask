from flask import Flask, render_template, request
from bus_search import bus_search

app = Flask(__name__)


@app.route("/bus/<direction>")
def bus(direction):

    bus = bus_search()

    result = bus.direct_bus(direction)

    return render_template("index.html", result=result, direction=direction)


if __name__ == "__main__":
    app.run(host= "0.0.0.0",debug=True)
