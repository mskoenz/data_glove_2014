// Author:  Mario S. Könz <mskoenz@gmx.net>
// Date:    24.07.2013 20:29:43 CEST
// File:    keyop_protocol.hpp

#ifndef __KEYOP_PROTOCOL_HEADER
#define __KEYOP_PROTOCOL_HEADER

namespace keyop {
    
    long int const speed = 57600;
    //~ long int const speed = 115200;
    //~ long int const speed = 460800;
    
    uint8_t const read_key = 'k';
    uint8_t const write_key = 'l';
    uint8_t const read_n_keys = 'o';
    uint8_t const write_n_keys = 'p';
    
    uint8_t const max_keys = 30;
    
}//end namespace keyop

#endif //__KEYOP_PROTOCOL_HEADER
