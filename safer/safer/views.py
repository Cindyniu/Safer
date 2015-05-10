#!/usr/bin/env python
# coding=utf-8

from django.shortcuts import render_to_response
from django.http import HttpResponse

def camera_capture(request):
    return render_to_response('camera_capture.html', locals())  

def hello(request):
    return HttpResponse("hello world")
