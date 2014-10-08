// Author:  Mario S. Könz <mskoenz@gmx.net>
// Date:    24.07.2013 18:58:59 CEST
// File:    key_operator.cpp

#define COLOR_ON
#define DEBUG_ON
#define ADVANCED_INTERRUPTS

#include <Arduino.h>
#include <ustd.hpp>
#include <diag.hpp>
#include <tool.hpp>

#include <com/eeprom.hpp>
#include <com/uart.hpp>
#include <com/i2c.hpp>

//~ #include <device/bluesmirf_hid.hpp>
#include <device/MMA8452.hpp>

#include "position.hpp"
#include "bridge.hpp"
#include "depreller.hpp"
#include "keyop_protocol.hpp"

char in;

typedef ustd::array<uint8_t, 9> array_type;

class program {
public:
    //~ program(): keyboard_(SOFTWARE_SERIAL_RX, SOFTWARE_SERIAL_TX) {
    program() {
        
        setup();
    }
    void setup() {
        ustd::cout.init(keyop::speed);
        com::eeprom.clear();
        
        //~ com::eeprom & data_;
        
        //~ for(uint8_t i = 0; i < keyop::max_keys; ++i) {
            //~ data_[i].calc_mask();
        //~ }
        
        com::i2c_begin();
        //~ acc_meter_.init();
        //~ keyboard_.connect();
        
        delay(150);
    }
    void update() {
        tool::clock.update();
        //~ acc_meter_.update();
        //~ double max = 0;
        //~ uint8_t max_ind = 0;
        //~ for(uint8_t i = 0; i < 3; ++i) {
            //~ g[i] << acc_meter_[i];
            
            //~ if(g[i] > max) {
                //~ max = g[i];
                //~ max_ind = 2*i + 1;
            //~ } else if(-g[i] > max) {
                //~ max = -g[i];
                //~ max_ind = 2*i + 2;
            //~ }
        //~ }
        
        uint8_t curr_gest;
        com::i2cout(core::i2c_adress) << core::current_gesture << ustd::endl;
        delayMicroseconds(100);
        com::i2cin(core::i2c_adress) >> curr_gest;
        
        //~ depreller_.update((max_ind << 5) + (31 & curr_gest));
        //~ for(uint8_t i = 0; i < data_.size(); ++i) {
            //~ btn_[i].update((depreller_.state() & (data_[i].mask)) == data_[i].trigger
                       //~ and (depreller_.old_state() & (data_[i].pre_mask)) == data_[i].pre_trigger);
        //~ }
        //~ DEBUG_VAR(curr_gest)
        //~ diag::speed_report();
    }
    void loop() {
        update();
        
        auto & pipe = com::uart;
        //~ auto & pipe = ustd::cout;
        
        if(com::uart) {
            com::uart >> in;
            if(in == core::raw_value) {
                com::i2cout(core::i2c_adress) << core::raw_value << ustd::endl;
                delayMicroseconds(200);
                com::i2cin(core::i2c_adress) >> pos_;
                pipe << pos_;
            } else if(in == core::read_gesture) { 
                com::uart >> in;
                com::i2cout(core::i2c_adress) << core::read_gesture << in << ustd::endl;
                delayMicroseconds(300);
                com::i2cin(core::i2c_adress) >> gest_;
                pipe << gest_;
            } else if(in == core::write_gesture) {
                com::uart >> in;
                com::uart >> gest_;
                com::i2cout(core::i2c_adress) << core::write_gesture << in << gest_ << ustd::endl; 
            } else if(in == core::read_n_gestures) {
                com::i2cout(core::i2c_adress) << core::read_n_gestures << ustd::endl;
                com::i2cin(core::i2c_adress) >> in;
                pipe << in;
            } else if(in == core::write_n_gestures) {
                com::uart >> in;
                com::i2cout(core::i2c_adress) << core::write_n_gestures << in << ustd::endl;
            } else if(in == core::write_to_eeprom) {
                //~ for(uint8_t i = 0; i < keyop::max_keys; ++i) { //bc of the checksum :-/
                    //~ data_[i].mask = 0;
                    //~ data_[i].pre_mask = 0;
                //~ }
                //~ 
                //~ com::eeprom << data_;
                //~ 
                //~ for(uint8_t i = 0; i < keyop::max_keys; ++i) //bc of the checksum :-/
                    //~ data_[i].calc_mask();
                    
                com::i2cout(core::i2c_adress) << core::write_to_eeprom << ustd::endl;
            } else if(in == core::remove_all_gestures) {
                com::i2cout(core::i2c_adress) << core::remove_all_gestures << ustd::endl;
            } else if(in == core::current_gesture) {
                com::i2cout(core::i2c_adress) << core::current_gesture << ustd::endl;
                com::i2cin(core::i2c_adress) >> in;
                pipe << in;
            
            //~ } else if(in == keyop::read_key) {
                //~ com::uart >> in;
                //~ com::uart << data_[in];
            //~ } else if(in == keyop::write_key) {
                //~ com::uart >> in;
                //~ com::uart >> data_[in];
                //~ data_[in].calc_mask();
            //~ } else if(in == keyop::read_n_keys) {
                //~ in = data_.size();
                //~ com::uart << in;
            //~ } else if(in == keyop::write_n_keys) {
                //~ com::uart >> in;
                //~ data_.set_size(in);
            }
        }
        
        //~ for(uint8_t i = 0; i < data_.size(); ++i) {
            //~ if(btn_[i] == state::falling)
                //~ keyboard_.press(data_[i].key, data_[i].mod);
            //~ else if(btn_[i] == state::rising)
                //~ keyboard_.release(data_[i].key, data_[i].mod);
        //~ }
        //~ diag::speed_report();
    }
    
    void receive(int n){}
    void request(){}
private:
    array_type pos_;
    gesture_class gest_;
    tool::depreller_class depreller_;
    
    ustd::array<tool::button_class<tool::fake>, keyop::max_keys> btn_;
    ustd::static_vector<key_data_struct, keyop::max_keys> data_;
    
    //~ device::MMA8452_class acc_meter_;
    ustd::lowpass_filter<double, 40> g[3];
    //~ device::bluesmirf_hid_class keyboard_;
};

#include <main.hpp>
 
