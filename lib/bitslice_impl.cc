/* -*- c++ -*- */
/* 
 * Copyright 2018 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "bitslice_impl.h"

namespace gr {
  namespace bitslice {

    bitslice::sptr
    bitslice::make(int omega)
    {
      return gnuradio::get_initial_sptr
        (new bitslice_impl(omega));
    }

    /*
     * The private constructor
     */
    bitslice_impl::bitslice_impl(int omega)
      : gr::block("bitslice",
              gr::io_signature::make(1, 1, sizeof(unsigned char)),
              gr::io_signature::make(1, 1, sizeof(unsigned char))),
        d_omega(omega)
    {}

    /*
     * Our virtual destructor.
     */
    bitslice_impl::~bitslice_impl()
    {
    }

    void
    bitslice_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
        ninput_items_required[0] = noutput_items * d_omega;
    }

    int
    bitslice_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const unsigned char *in = (const unsigned char *) input_items[0];
      unsigned char *out = (unsigned char *) output_items[0];

      consume_each (noutput_items);

      return noutput_items;
    }

  } /* namespace bitslice */
} /* namespace gr */

