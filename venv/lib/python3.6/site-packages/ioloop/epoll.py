#!/usr/bin/env python
# encoding: utf-8

import select

class EPollLoop(object):

    def __init__(self):

        self.loop = select.epoll()

        self.register = self.loop.register
        self.unregister = self.loop.unregister
        self.modify = self.loop.modify
        self.poll = self.loop.poll
