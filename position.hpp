// Author:  Mario S. Könz <mskoenz@gmx.net>
// Date:    04.07.2013 18:29:44 EDT
// File:    position.hpp

#ifndef __POSITION_HEADER
#define __POSITION_HEADER

#include <ustd.hpp>
#include <diag.hpp>
#include <tool.hpp>
#include <numerics.hpp>

#include "sensor.hpp"

class position_class {
public:
    typedef ustd::array<uint8_t, 9> array_type;
    //------------------- ctor -------------------
    position_class(): count_(0), dist_(0) {
        //just to get rid of initial irregularities
        for(uint8_t i = 0; i < 40; ++i) {
            sen_.update(pos_[i&1]); //saves code on -O3
        }
    }
    //------------------- ops -------------------
    void update(uint8_t const & n = 1) {
        ++count_;
        sen_.update(pos_[count_ & 1]);
        dist_ += d1<uint32_t>(pos_[0], pos_[1]);
        change_ << dist_;
    }
    //------------------- print and serialize -------------------
    template<typename S>
    void print(S & os) const {
        os << change() << "\t" << pos_[count_ & 1];
    }
    template<typename Archive>
    void serialize(Archive & ar) {
        //~ ASSERT(false)
        ar & pos_[count_ & 1];
    }
    array_type const & pos() const {
        return pos_[count_ & 1];
    }
    uint8_t const & operator[](array_type::size_type const & idx) {
        return pos_[count_ & 1][idx];
    }
    uint64_t change() const {
        return change_;
    }
private:
    array_type pos_[2];
    sensor_class sen_;
    uint64_t count_;
    uint64_t dist_;
    ustd::highpass_filter<uint64_t, 990> change_;
    //~ uint16_t speed_;
};


#endif //__POSITION_HEADER
