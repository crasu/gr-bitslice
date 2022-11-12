#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2016 <+YOU OR YOUR COMPANY+>.
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

import numpy
from gnuradio import gr

class slicer(gr.basic_block):
    def __init__(self, omega = 1):
        gr.basic_block.__init__(self,
            name="slicer",
            in_sig=[numpy.uint8],
            out_sig=[numpy.uint8])
        self.omega = omega
        self.debug = False

    def forecast(self, noutput_items, ninputs):
        if self.debug:
            print(f"Forecast ninputs: {ninputs} Output {noutput_items} Omega {self.omega}")
        ninput_items_required = [noutput_items * self.omega] * ninputs
        return ninput_items_required

    def general_work(self, input_items, output_items):
        input = input_items[0][:]
        if self.debug:
            print(f"Input: {input} Omega {self.omega}")

        output_idx=0
        consume_all = 0

        while output_idx < len(output_items[0]) and consume_all <= len(input) - self.omega:
            sample = input[consume_all:consume_all + self.omega]
            if self.debug:
                print(f"Sample: {sample}")

            if(numpy.count_nonzero(sample) > self.omega/2):
                output_items[0][output_idx] = 1
            else:
                output_items[0][output_idx] = 0

            consume = self.find_phase_change(sample)
            if consume == 0: # full consume if only phase change is at sample start
                consume = self.omega

            if self.debug:
                print(f"Consume: {consume} Output: {output_items}")

            consume_all += consume
            if consume >= self.omega // 2:
                output_idx+=1

        self.consume_each(consume_all)
        return output_idx

    def find_phase_change(self, sample):
        o2 = self.omega // 2
        if sample[o2] == 1:
            char_to_find = 0
        else:
            char_to_find = 1

        char_idx = numpy.nonzero(sample == char_to_find)[0] 
        if char_idx.size == 0:
            return self.omega

        return char_idx[(numpy.abs(char_idx - o2)).argmin()]
