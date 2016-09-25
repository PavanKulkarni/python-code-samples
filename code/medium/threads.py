import threading

class Downloader(threading.Thread):

    def __init__(self, counter=0, thread=None):
        threading.Thread.__init__(self)
        self.counter=counter
        self.thread = thread

    def run(self):
        t = 0
        while t < self.counter:
           print '%s--->%s' %(self.thread, t)
           t+=1
        print '%s---Done' % self.thread
        



if __name__=='__main__':
    t = Downloader(5, 'T1')
    t1 = Downloader(7, 'T2')
    t.start()
    t1.start()


    
