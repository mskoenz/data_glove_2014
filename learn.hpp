// Author:  Mario S. Könz <mskoenz@gmx.net>
// Date:    20.07.2013 11:08:02 EDT
// File:    learn.hpp

#ifndef __LEARN_HEADER
#define __LEARN_HEADER

#include <ustd.hpp>
#include <tool.hpp>

#include "hardware_constants.hpp"

class learn_algo_class {
public:
    //------------------- ctor -------------------
    learn_algo_class(): cur_iter(0), id(0), pos(0), max_iter_(0) {
    }
    
    //------------------- ops -------------------
    operator bool() const {
        return max_iter_ != 0;
    }
    void set_iter(uint8_t const & iter) {
        max_iter_ = iter;
    }
    uint8_t cur_iter;
    uint8_t const & max_iter() const {
        return max_iter_;
    }
    uint8_t id;
    uint8_t pos;
private:
    uint8_t max_iter_;
};

#endif //__LEARN_HEADER
