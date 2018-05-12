import math,sys

class SoundComparator :
    number = -1
    lastfreq = None
    timeremain = 0
    
    fundamental=[16,17,18,19,20,21,23,24,26,27,29,30,
                 32,34,36,38,41,43,46,49,51,55,58,62,
                65,69,74,78,83,87,92,98,104,110,117,123,
                 131,139,147,156,165,175,185,196,208,220,233,247,
                 262,277,294,311,330,349,370,392,415,440,466,494,
                 523,554,587,622,659,698,740,784,831,880,932,988,
                 1046,1109,1175,1244,1318,1397,1480,1568,1661,1760,1865,1975,
                 2093,2217,2349,2489,2637,2794,2960,3126,3322,3520,3729,3951,
                 4186,4435,4698,4978,5274,5588,5920,6272,6645,7040,7458,7902,
                 8372,8870,9396,9956,10548,117176,11840,12544,13290,14080,14918,15804,
                 16744,17740,18792,19912,21098]
    
    
    def findHeight(frequency):
        search = math.ceil(frequency)
        if search in fundamental:
            height=fundamental.index(search)
        elif search+1 in fundamental:
            height=fundamental.index(search+1)
        elif search-1 in fundamental:
            height=fundamental.index(search-1)
        else:
            height = -1
        return height+1
    
    def compareFreq(frequency,high):
        search = 2
    
    @staticmethod       
    def compare(mymusic):
        SoundComparator.number += 1
        SoundComparator.timeremain -= 1
        if not(SoundComparator.timeremain > 0) :
            freq = (mymusic.getHeight(SoundComparator().number))
            if freq != None :
                SoundComparator.lastfreq = freq.height
                SoundComparator.timeremain = freq.duration
            else :
                SoundComparator.lastfreq = None
                SoundComparator.timeremain = 0
        sys.stdout.write("{0} : {1}\n".format(str(SoundComparator.number),str(SoundComparator.lastfreq)))  # same as print
        sys.stdout.flush()