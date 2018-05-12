from classes.textparser import TextParser
from classes.soundcomparator import SoundComparator

from twisted.internet import task
from twisted.internet import reactor

from multiprocessing import Process

import threading

import pygame.mixer

import time,sys

timeout = 1 # Sixty seconds

def doWork(mymusic):
    SoundComparator().compare(mymusic)
    pass

def playMusic():
    pygame.mixer.init()
    pygame.mixer.music.load("audio/Stop.ogg")   # chargement de la musique
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        i = 1    

def dumpclean(obj):
    if type(obj) == dict:
        for k, v in obj.items():
            if hasattr(v, '__iter__'):
                print(k)
                dumpclean(v)
            else:
                print ('%s : %s' % (k, v.text))
    elif type(obj) == list:
        for v in obj:
            if hasattr(v, '__iter__'):
                dumpclean(v)
            else:
                print(v)
    else:
        print(obj)
        



if __name__ == '__main__':
    fileLy = TextParser("Text/Aqua.txt")
    mymusic = fileLy.getMusic()
    #dumpclean(mymusic.lyrics)
    print(mymusic.name)
    l = task.LoopingCall(doWork,mymusic)
    l.start(timeout) # call every sixty seconds
    print(mymusic.getHeight(1010).height)
    #reactor.run()    
    
    p = Process(target=playMusic, args=())
    p2 = Process(target=reactor.run, args=())
    p2.start()    
    p.start()
    p.join()
    p2.terminate()

#thr = threading.Thread(target=reactor.run, args=(), kwargs={})
#thr.start() # Will run "foo"

