// Author:  Mario S. Könz <mskoenz@gmx.net>
// Date:    04.07.2013 15:57:16 EDT
// File:    sensor.hpp

#ifndef __SENSOR_HEADER
#define __SENSOR_HEADER

#include <ustd.hpp>
#include <tool.hpp>

#include "hardware_constants.hpp"

class sensor_class {
public:
    sensor_class() {
    }
    template<typename U> //U fulfills vector concept
    void update(U & u) {
        sen_[0].update();
        
        mux0_ = 1;
        sen_[1].update();
        
        mux1_ = 1;
        sen_[2].update();
        
        mux0_ = 0;
        sen_[3].update();
        
        mux2_ = 1;
        sen_[4].update();
        
        mux0_ = 1;
        sen_[5].update();
        
        mux1_ = 0;
        sen_[6].update();
        
        mux0_ = 0;
        sen_[7].update();
        
        mux2_ = 0;
        
        last_sen_.update();
        
        for(uint8_t i = 0; i < 9; ++i) {
            if(m[i] == 8)
                u[i] = last_sen_ - cutoff;
            else
                u[i] = sen_[m[i]] - cutoff;
                
        }
    }
private:
    tool::out_pin_class<MUX0_PIN> mux0_;
    tool::out_pin_class<MUX1_PIN> mux1_;
    tool::out_pin_class<MUX2_PIN> mux2_;
    ustd::array<tool::analog_class<MUX_MASTER_PIN, 8>, 8> sen_;
    tool::analog_class<SENSOR8_PIN, 8> last_sen_;
};


#endif //__SENSOR_HEADER
