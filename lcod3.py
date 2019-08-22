from mrjob.job import MRJob
from mrjob.step import MRStep
class DeathCause(MRJob):
        def steps(self):
                return[
                        MRStep(mapper=self.mymapper,reducer=self.myreducer)
                        ]
        def mymapper(self,_,line):
                field={}
                field=line.split(',')
                yield(field[2],1)
        def myreducer(self,key,value):
                yield key,sum(value)
if __name__=='__main__':
        DeathCause.run()
