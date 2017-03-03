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
        self.omega = omega
        gr.basic_block.__init__(self,
            name="slicer",
            in_sig=[numpy.uint8],
            out_sig=[numpy.uint8])

    def forecast(self, noutput_items, ninput_items_required):
        #setup size of input_items[i] for work call
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = self.omega

    def general_work(self, input_items, output_items):
        print("general_work")
        #output_items[0][0] = input_items[0][0]
        sample = input_items[0][0:self.omega]
        print(sample)
        if(numpy.count_nonzero(sample) > self.omega/2):
            output_items[0][0] = 1
        else:
            output_items[0][0] = 0
        self.consume_each(self.omega)
        return 1

    def find_phase_change(self, sample):
	if sampe[rate/2] == "1":
	    char_to_find = "0"
	else:
	    char_to_find = "1"
	before_idx = input.rfind(char_to_find, rate/2, 0)
	after_idx = input.find(char_to_find, 0, rate/2)

	if before_idx == -1 and after_idx == -1:
	    return rate

	if before_idx == -1:
	    return after_idx

	if after_idx == -1:
	    return before_idx + rate
	return before_idx + rate if rate/2 - before_idx > after_idx - rate/2 else after_idx 


