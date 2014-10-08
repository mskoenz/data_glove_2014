// Author:  Mario S. Könz <mskoenz@gmx.net>
// Date:    28.06.2013 20:47:31 EDT
// File:    bridge.hpp

#ifndef __BRIDGE_HEADER
#define __BRIDGE_HEADER

#include <ustd_generic.hpp>
#include <tool/ring_buffer.hpp>
#include "core_protocol.hpp"

class gesture_class {
    typedef ustd::array<uint8_t, 9> array_type;
    typedef array_type::size_type size_type;
//=================== public ===================
public:
//------------------- ctors -------------------
    gesture_class(): id_(0xFF) {
        for(size_type i = 0; i < cube_[core::low].size(); ++i) {
            cube_[core::low] = 255;
            cube_[core::high] = 0;
        }
    }
    template<typename U> //U is a model of the vector concept
    bool contains(U const & val) {
        for(size_type i = 0; i < cube_[core::high].size(); ++i) {
            if(val[i] > cube_[core::high][i] or val[i] < cube_[core::low][i])
                return false;
        }
        return true;
    }
    array_type & high() {
        return cube_[core::high];
    }
    array_type & low() {
        return cube_[core::low];
    }
    uint8_t & id() {
        return id_;
    }
    //------------------- print and serialize -------------------
    template<typename S>
    void print(S & os) const {
        os << cube_[core::low] << F("-") << cube_[core::high];
    }
    template<typename Archive>
    void serialize(Archive & ar) {
        ar & cube_;
        ar & id_;
    }
//=================== private ===================
private:
    array_type cube_[2];
    uint8_t id_;
};

struct key_data_struct {
    uint8_t key;
    uint8_t mod;
    uint8_t trigger;
    uint8_t mask;
    
    uint8_t pre_key;
    uint8_t pre_mod;
    uint8_t pre_trigger;
    uint8_t pre_mask;
    
    key_data_struct(): key(0), mod(0), trigger(0), mask(0), pre_key(0), pre_mod(0), pre_trigger(0), pre_mask(0) {
    }
    
    //------------------- print and serialize -------------------
    template<typename S>
    void print(S & os) const {
        os << key << " " << mod << " " << trigger << " " << mask;
    }
    template<typename Archive>
    void serialize(Archive & ar) {
        ar & key;
        ar & mod;
        ar & trigger;
        
        ar & pre_key;
        ar & pre_mod;
        ar & pre_trigger;
    }
    
    void calc_mask() {
        mask = 0xFF;
        if((trigger & 0xE0) == 0) //0 == all axis are ok / ignore axis
            mask &= 0x1F;
        if((trigger & 0x1F) == 0)
            mask &= 0xE0;
        
        pre_mask = 0xFF;
        if((pre_trigger & 0xE0) == 0) //0 == all axis are ok / ignore axis
            pre_mask &= 0x1F;
        if((pre_trigger & 0x1F) == 0)
            pre_mask &= 0xE0;
    }
};


#endif //__BRIDGE_HEADER
