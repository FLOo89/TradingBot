# -*- coding: utf-8 -*-

import numpy as np

def Strategy():
    
    def __init__(self, maxtab,mintab):
        self.maxtab = []
        self.mintab = []
        
    # Peaks detection function
    def peakdet(self,v, delta, x = None):
        if x is None:
            x = np.arange(len(v))
        v = np.asarray(v)
        mn, mx = np.Inf, -np.Inf
        mnpos, mxpos = np.NaN, np.NaN
        lookformax = True
        for i in np.arange(len(v)):
            this = v[i]
            if this > mx:
                mx = this
                mxpos = x[i]
            if this < mn:
                mn = this
                mnpos = x[i]
    
            if lookformax:
                if this < mx-delta:
                    self.maxtab.append((mxpos, mx))
                    mn = this
                    mnpos = x[i]
                    lookformax = False
            else:
                if this > mn+delta:
                    self.mintab.append((mnpos, mn))
                    mx = this
                    mxpos = x[i]
                    lookformax = True
    
        return np.array(self.maxtab), np.array(self.mintab)
    
    # Frame labelization functions
    def setSell(idx, peaksmax, peaksmin):
        for i in peaksmax:
            if i[0] == idx:
                return 1.0
        for i in peaksmin:
            if i[0] == idx:
                return 0.0
        return 0.0
    
    def setWait(idx, peaksmax, peaksmin):
        for i in peaksmax:
            if i[0] == idx:
                return 0.0
        for i in peaksmin:
            if i[0] == idx:
                return 0.0
        return 1.0
    
    def setBuy(idx, peaksmax, peaksmin):
        for i in peaksmax:
            if i[0] == idx:
                return 0.0
        for i in peaksmin:
            if i[0] == idx:
                return 1.0
        return 0.0
    
    def frame_labelization(frame_base, maxp, minp, data):
        frame_base["wait"] = [setWait(d, maxp, minp) for d in range(len(data[0]["data"]))]
        frame_base["sell"] = [setSell(d, maxp, minp) for d in range(len(data[0]["data"]))]
        frame_base["buy"] = [setBuy(d, maxp, minp) for d in range(len(data[0]["data"]))]
        return frame_base
