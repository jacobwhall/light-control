#!/usr/bin/python3

from flask import Flask, render_template, request

from lifxlan import LifxLAN
print("Discovering lights...")
lifx = LifxLAN(2)

web = Flask(__name__)

@web.route("/", methods=["POST" , "GET"])
def home():
	#
#    if (request.method == "POST"):
#        tmp = int(request.form["state"])
#        if (tmp == -1):
#            rad.Play(-1)
#            print("Previous")
#        elif (tmp == 0):
#            rad.pause()
#            print("Pause")
#        elif (tmp == 1):
#            rad.Play(1)
#            print("Next")
    return render_template("home.html")

@web.route("/colorchange")
def color():
    if "color" in request.args:
        color =  int(request.args["color"])
        print(color)
    else:
        print("NO COLOR")
    return home()

@web.route("/turnonlights")
def turnon():
	lifx.set_power_all_lights("on", rapid=True)
	return home()

@web.route("/turnofflights")
def turnoff():
	lifx.set_power_all_lights("off", rapid=True)
	return home()

# run the application
if __name__ == "__main__":
    web.run(host="0.0.0.0", port="80", debug=False)
