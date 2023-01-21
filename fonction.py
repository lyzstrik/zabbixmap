import random, time, sys, os
from math import sqrt

os.system('cls')

def set_sum(sets) :
    result = set()
    for i in sets :
        result.update(i)
    return result

class TimingAnalysis:
    DEFAULT_PRECISION = 2
    def __init__(self,func_name,details,precision=DEFAULT_PRECISION):
        self.timings   = []
        self.func_name = func_name
        self.details   = details
        self.precision = precision
    
    def average(self) :
        return sum(self.timings)/len(self.timings)

    def variance(self) :
        return sum([(a - self.average())**2 for a in self.timings])/len(self.timings)

    def std(self) :
        return sqrt(self.variance())

    def write(self,execution_time,ID) :
        self.timings.append(round(execution_time,self.precision))

        string = "[function {} : {}] ".format(self.func_name,ID)
        string += ", ".join(["{} = {}s".format(
            func.__name__,round(func(self),self.precision)
        ) for func in self.details])

        print(f"{string}\r")

class Flags:
    ALL      = {TimingAnalysis.average,TimingAnalysis.std,TimingAnalysis.variance}
    AVERAGE  = {TimingAnalysis.average}
    VARIANCE = {TimingAnalysis.variance}
    STD      = {TimingAnalysis.std}
    NONE     = set()

def timing_analysis(n,*flags,precision=TimingAnalysis.DEFAULT_PRECISION) :
    def decorator(func) :
        def wrapper(*args,**kwargs) :
            details = set_sum(flags)
            t = TimingAnalysis(func.__name__,details,precision)
            for i in range(1,n+1) :
                start = time.time()
                func(*args,**kwargs)
                end = time.time()
                t.write(end-start,i)
        return wrapper
    return decorator

def time_to_run(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end   = time.time()
        print("It's take {}".format(end-start))
    return wrapper