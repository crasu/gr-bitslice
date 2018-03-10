#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2018 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from bitslice.bitslice_swig import bitslice

class qa_bitslice (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def run_slicer(self, input, output, omega):
        src = blocks.vector_source_b(input, False)
        sl = bitslice(omega)
        sink = blocks.vector_sink_b()
        self.tb.connect(src, sl, sink)
        self.tb.run()
        self.assertEqual(sink.data(), output)

    def test_001_t (self):
        self.run_slicer([0, 1, 0], (0, 1, 0), 1)
        self.run_slicer([0, 0], (0, ), 2)
        self.run_slicer([0, 0, 0, 1, 1, 1], (0, 1), 3)
        self.run_slicer([0, 0, 1, 1, 1], (0, 1), 3)
        self.run_slicer([0, 0, 1, 1, 1, 1], (0, 1), 3)
        self.run_slicer([0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1], (0, 1), 5)
        self.run_slicer([0, 0, 1, 1, 1, 1], (0, 1, 1), 2)
        self.run_slicer([0], (), 2)
        self.run_slicer([0, 0, 1, 1, 1, 1, 1, 1], (1,), 6)
        self.run_slicer([0,0,1,1,1,1,0,0,1,1,1], (0,1,0,1), 3)


if __name__ == '__main__':
    gr_unittest.run(qa_bitslice, "qa_bitslice.xml")
