from django.shortcuts import render
from django.http import HttpResponse
import json,socket,pickle

# Create your views here.
def index(request):
    data = json.dumps(connect("cpubo"))
    response = HttpResponse(data,content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

def testhtml(request):
    return render(request,"test.html")

def connect(mass):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 8001))

    sock.send(mass.encode())
    date = sock.recv(100000)
    date = pickle.loads(date)
    return date

def neicuninfo(request):
    data = json.dumps(connect("neicuninfo"))
    response = HttpResponse(data, content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

def anshen(request):
    sock  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(('0.0.0.0',1000))
    sock.send("guang".encode())
    data = sock.recv(1000000)
    data = pickle.loads(data)
    return HttpResponse(data)
