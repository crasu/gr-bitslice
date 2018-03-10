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

    int find_phase_change(const unsigned char *in, int relevant_count)
    {
        int o2 = relevant_count / 2;
        unsigned char char_to_find = 1;

        if (in[o2] == 1) {
            char_to_find = 0;
        }

        const void *forward_ptr = memchr(in + o2, char_to_find, relevant_count - o2);
        const void *backward_ptr = memrchr(in, char_to_find, o2);

        if(forward_ptr == NULL && backward_ptr == NULL) {
            return relevant_count;
        }

        int forward_dist = std::numeric_limits<int>::max();
        if(forward_ptr != NULL) {
            forward_dist = ((const unsigned char*) forward_ptr - in) - o2;
        }

        int backward_dist = std::numeric_limits<int>::max();
        if(backward_ptr != NULL) {
            backward_dist = o2 - ((const unsigned char*) backward_ptr - in);
        }

        std::cout << "forward_dist " << forward_dist << std::endl;
        std::cout << "backward_dist " << backward_dist << std::endl;

        if (forward_dist < backward_dist) {
            return forward_dist + o2;
        } else {
            return o2 - backward_dist;
        }

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
        int item_count = ninput_items[0];
        int relevant_count = std::min(item_count, d_omega);

        int zero_count = std::count(in, in + relevant_count, 0);
        ninput_items[0] = 1;

        std::cout << "in: ";
        for(int i=0; i < item_count; i++)
            std::cout << (unsigned int)in[i];
        std::cout << std::endl;
        std::cout << "Item Count: " << item_count << std::endl;
        std::cout << "Relevant Count: " << relevant_count << std::endl;
        std::cout << "Zero Count: " << zero_count << std::endl;

        if(zero_count > d_omega / 2) {
            out[0] = 0;
        } else {
            out[0] = 1;
        }

        int consume = find_phase_change(in, relevant_count);
        std::cout << "Consume: " << consume << std::endl;

        if(consume == 0) {
            consume = d_omega;
        }

        consume_each(consume);

        if(consume <= d_omega/2) {
            return 0;
        } else {
            return 1;
        }
    }

  } /* namespace bitslice */
} /* namespace gr */

