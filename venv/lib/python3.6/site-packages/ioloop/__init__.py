#!/usr/bin/env python
# encoding: utf-8

import threading
import select

_EPOLLIN = 0x001
_EPOLLOUT = 0x004
_EPOLLERR = 0x008
_EPOLLHUP = 0x010

# Our events map exactly to the epoll events
NONE = 0
READ = _EPOLLIN
WRITE = _EPOLLOUT
ERROR = _EPOLLERR | _EPOLLHUP


class IOLoop(object):

    
    _instance_lock = threading.Lock()
    _current = threading.local()

    @staticmethod
    def instance():
        """Returns a global `IOLoop` instance.

        Most applications have a single, global `IOLoop` running on the
        main thread.  Use this method to get this instance from
        another thread.  To get the current thread's `IOLoop`, use `current()`.
        """
        if not hasattr(IOLoop, "_instance"):
            with IOLoop._instance_lock:
                if not hasattr(IOLoop, "_instance"):
                    # New instance after double check
                    IOLoop._instance = IOLoop()
        return IOLoop._instance   

    
    def __init__(self, impletement=None):
       
        if impletement:
            self._impl = impletement
        elif hasattr(select, 'kqueue'):
            from ioloop.kqueue import KQueueLoop
            self._impl = KQueueLoop
        elif hasattr(select, 'epoll'):
            from ioloop.epoll import EPollLoop
            self._impl = EPollLoop
        else:
            raise NotImplemented('No model')

        self._loop = self._impl()

        self._running = False
        self._fd_to_handlers = {}
    
    def add_handler(self, fd, events, handler):
        
        self._fd_to_handlers[fd] = handler
        self._loop.register(fd, events)

    def remove_handler(self, fd):

        self._fd_to_handlers.pop(fd)
        self._loop.unregister(fd)

    def modify_handler(self, fd, events, handler):
        self.remove_handler(fd)
        self.add_handler(fd, events, handler)

    @staticmethod
    def current():

        current = getattr(IOLoop._current, 'instance', None)
        if current is None:
            return IOLoop.instance()
        return current
    

    def start(self):

        if self._running:
            raise RuntimeError('IOLoop is already running')

        while True:
            for fd, events in self._loop.poll():
                self._fd_to_handlers[fd](fd, events)

