// Author:  Mario S. Könz <mskoenz@gmx.net>
// Date:    24.07.2013 19:45:55 CEST
// File:    core_protocol.hpp

#ifndef __CORE_PROTOCOL_HEADER
#define __CORE_PROTOCOL_HEADER

namespace core {
    long int const speed = 57600;
    
    uint8_t const i2c_adress = 66;
    uint8_t const max_gest = 30;
    
    uint8_t const hist_size = 5;
    
    uint8_t const low = 0;
    uint8_t const high = 1;
    
    uint8_t const raw_value = 's';
    uint8_t const write_gesture = 'w';
    uint8_t const read_gesture = 'r';
    uint8_t const read_n_gestures = 'n';
    uint8_t const write_n_gestures = 'm';
    uint8_t const current_gesture = 'c';
    uint8_t const learn_gesture = 'l';
    
    uint8_t const remove_all_gestures = 'd';
    uint8_t const write_to_eeprom = 'e';
    uint8_t const reset_glove = 'x';
    
    uint8_t const reset_time = 'y';
    uint8_t const read_time = 't';
    
    uint8_t const begin_learning = 'a';
    uint8_t const learning_progress = 'b';
    uint8_t const end_learning = 'f';
    
    uint8_t const get_last_gestures = 'h';
    
}//end namespace cmd

#endif //__CORE_PROTOCOL_HEADER
