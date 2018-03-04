/* -*- c++ -*- */

#define BITSLICE_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "bitslice_swig_doc.i"

%{
#include "bitslice/bitslice.h"
%}


%include "bitslice/bitslice.h"
GR_SWIG_BLOCK_MAGIC2(bitslice, bitslice);
