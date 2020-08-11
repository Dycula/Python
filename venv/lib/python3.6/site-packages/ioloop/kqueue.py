#!/usr/bin/env python
# encoding: utf-8

import select
from ioloop import READ, WRITE, ERROR

class KQueueLoop(object):

    def __init__(self):

        self.loop = select.kqueue()
        self.active = {}

    def register(self, fd, events):
        if fd in self.active:
            raise IOError('FD: %d in active' % fd)
        self._control(fd, events, select.KQ_EV_ADD)
        self.active[fd] = events

    def unregister(self, fd):
        events = self.active.pop(fd)
        self._control(fd, events, select.KQ_EV_DELETE)

    def modify(self, fd, events):
        self.unregister(fd)
        self.register(fd, events)

    def _control(self, fd, events, flags):
        
        kevents = []
        if events & WRITE:
            kevents.append(select.kevent(fd,
                                         filter=select.KQ_FILTER_WRITE,
                                         flags=flags))
        if events & READ:
            kevents.append(select.kevent(fd,
                                         filter=select.KQ_FILTER_READ,
                                         flags=flags))

        [self.loop.control([x], 0) for x in kevents]

    def poll(self, timeout=1):

        kevents = self.loop.control(None, 1000, timeout)
        events = {}

        for kevent in kevents:
            fd = kevent.ident
            if kevent.filter == select.KQ_FILTER_READ:
                events[fd] = events.get(fd,0) | READ
            elif kevent.filter == select.KQ_FILTER_WRITE and not kevent.flags & select.KQ_EV_EOF:
                events[fd] = events.get(fd,0) | WRITE
            elif kevent.flag & select.KQ_EV_ERROR:
                events[fd] = events.get(fd,0) | ERROR

        return events.items()
