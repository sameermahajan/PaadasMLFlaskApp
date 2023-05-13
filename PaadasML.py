# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, send_file, Response
# Response, send_file, after_this_request
import random
import time
import wave

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with paadas() function.
def paadas():
    # Approach1: working
    number = random.randint(1,10)
    f1 = "../numbers/" + str(number) + ".wav"
    times = random.randint(1,10)
    f2 = "../times/" + str(times) + ".wav"
    infiles = [f1, f2]
    outfile = "play.wav"

    data= []
    for infile in infiles:
        w = wave.open(infile, 'rb')
        data.append( [w.getparams(), w.readframes(w.getnframes())] )
        w.close()
    
    output = wave.open(outfile, 'wb')
    output.setparams(data[0][0])
    for i in range(len(data)):
        output.writeframes(data[i][1])
    output.close()
    f = open("play.wav", "rb")
    return send_file(f, mimetype="audio/wav")

    #Approach 2: not working
    #def generate(files):
    #    for file in files:
    #        yield file.read()

    #files = []
    #number = random.randint(1,10)
    #f1 = open("../numbers/" + str(number) + ".wav", 'rb')
    #files.append(f1)
    #times = random.randint(1,10)
    #f2 = open("../times/" + str(times) + ".wav", 'rb')
    #files.append(f2)
    #return Response(generate(files), mimetype='audio/wav')

    #Approach 3: not working
    # @after_this_request
    # def times(response):
    #    times = random.randint(1,10)
    #    f = open("../times/" + str(times) + ".wav", 'rb')
        #return response
    #    time.sleep(1)
    #    return send_file(f, mimetype="audio/wav")
    # return send_file(f, mimetype="audio/wav")
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()