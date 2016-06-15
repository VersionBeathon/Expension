# _*_ coding:utf-8 _*_
import os

print('Process %s start ...' % os.getpid())
pid = os.fork()

source = 10

if pid is 0:
    print("This is child process and my pid is %d, my process is %d" % (os.getpid(), os.getppid()))
    source -= 6
    print("Child process source value is " + str(source))
else:
    print("This is Father process, And its child pid is %d" % pid)
    source -= 1
    print("Father process source value is " + str(source))
print("Source value is " + str(source))