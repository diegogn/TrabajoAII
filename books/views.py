from django.shortcuts import render_to_response
import urllib2

def inicio(request):
    return render_to_response('Inicio.html')

def getGames():
    
    try:
        f = urllib2.urlopen('http://feeds.feedburner.com/planetadelibros-novedades')
        print f.read()
    except urllib2.HTTPError, e:
        print e.fp.read()
    
getGames()