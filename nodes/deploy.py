#!/usr/bin/env python

import nodes.root


class Deploy(nodes.root.Node):

    def __init__(self, yml):
        super(Deploy, self).__init__(yml)
