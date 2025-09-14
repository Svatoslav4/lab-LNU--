import math
import random as rnd
import tkinter as tki
import matplotlib.pyplot as plt


#Expropriated from pynative
def frange(start, stop=None, step=None):
    start = float(start)
    if stop == None:
        stop = start + 0.0
        start = 0.0
    if step == None:
        step = 1.0
    # print("start = ", start, "stop = ", stop, "step = ", step)
    count = 0
    while True:
        temp = float(start + count * step)
        if step > 0 and temp >= stop:
            break
        elif step < 0 and temp <= stop:
            break
        yield temp
        count += 1


TestingSignal=[10,11,17]

class Signal():
    SignalReal=[[],[]]
    def SignalGenerator(self,Xboundary0,Xboundary1,Yboundary0,Yboundary1,variant):
        if variant == 0:
            #Random generated in certain scale and certain number
            for i in frange(Xboundary0,Xboundary1,abs(Xboundary0-Xboundary1)/1000):
                self.SignalReal[0].append(i)
                self.SignalReal[1].append(rnd.uniform(Yboundary0,Yboundary1))
        elif variant == 1:
            #Sinusoid function from Xb`y0 to Xb`y1; Yb`y0 as phase shift; Yb`y1 as scale
            for i in frange(Xboundary0,Xboundary1,abs(Xboundary0-Xboundary1)/1000):
                self.SignalReal[0].append(i)
                self.SignalReal[1].append(math.sin(i+Yboundary0)*Yboundary1)
        elif variant == 2:
            #Cosinusoid function from Xb`y0 to Xb`y1; Yb`y0 as phase shift; Yb`y1 as scale
            for i in frange(Xboundary0,Xboundary1,abs(Xboundary0-Xboundary1)/1000):
                self.SignalReal[0].append(i)
                self.SignalReal[1].append(math.cos(i+Yboundary0)*Yboundary1)
        # else variant == 3:
        #     print("test")



    def Scaling(self,InSignal,Scale):
        Scaled=InSignal.copy()
        Scaled[1]=[i*Scale for i in Scaled[1]]
        return Scaled
    def TimeReversal(self,InSignal):
        Reversed=InSignal.copy()
        Reversed[0]=Reversed[0][::-1]
        return Reversed
    def TimeShift(self,InSignal,Shift):
        Shifted=InSignal.copy()
        Shifted[0]=[i+Shift for i in Shifted[0]]
        #InSignal[0]=Shifted
        return Shifted
    def Widen(self,InSignal,WidthFactor):
        Widened=InSignal.copy()
        Widened[0]=[i*WidthFactor for i in Widened[0]]
        #InSignal[0]=Widened
        return Widened
    def Combination(self,InSignal1,InSignal2):
        Combined=[]
        for i in range(max(InSignal1[0].__len__(),InSignal2[0].__len__())):
            if InSignal1[0][i]==InSignal2[0][i]:
                Combined.append(InSignal1[1][i]+InSignal2[1][i])
        return Combined

    def Multiplication(self,InSignal1,InSignal2):
        Multiplied=[]
        for i in range(max(InSignal1[0].__len__(),InSignal2[0].__len__())):
            if InSignal1[0][i]==InSignal2[0][i]:
                Multiplied.append(InSignal1[1][i]+InSignal2[1][i])
        return Multiplied


Generated=Signal()

Generated.SignalGenerator(0,10,0,1,2)

plt.plot(Generated.SignalReal[0],Generated.SignalReal[1])
plt.show()
GG=Generated.TimeShift(Generated.SignalReal,3)


plt.plot(GG[0],GG[1],'g')
plt.show()

YY=Generated.TimeReversal(Generated.SignalReal)

plt.plot(YY[0],YY[1],'y')
plt.show()

plt.plot(Generated.SignalReal[0],Generated.SignalReal[1])
plt.plot(GG[0],GG[1],'g')
plt.plot(YY[0],YY[1],'y')
plt.show()

