// Author:  Mario S. Könz <mskoenz@gmx.net>
// Date:    04.07.2013 15:53:36 EDT
// File:    hardware_constants.hpp

#ifndef __HARDWARE_CONSTANTS_HEADER
#define __HARDWARE_CONSTANTS_HEADER

//------------------- pos in array -------------------
//thumb
uint8_t const Dx = 0;
//trigger finger
uint8_t const Tx = 1;
uint8_t const Ty = 2;
//middle finger
uint8_t const Mx = 3;
uint8_t const My = 4;
//ring finger
uint8_t const Rx = 5;
uint8_t const Ry = 6;
//little finger
uint8_t const Lx = 7;
uint8_t const Ly = 8;
/*
* start with m[] = {0, 1, 2, 3, 4, 5, 6, 7, 8};
* 
* move thumb -> note what changes ...
* 
* get map
* 0, 1, 2, 3, 4, 5, 6, 7, 8
* 0, 8, 4, 3, 6, 2, 7, 1, 5
* 
* reverse map
* 0, 7, 5, 3, 2, 8, 4, 6, 1 --> this is the map!
* 0, 1, 2, 3, 4, 5, 6, 7, 8
*/


//------------------- measurement order -------------------

namespace version_2 {
    uint8_t const BLUE_LED = 9;
    uint8_t const GREEN_LED = 5;
    uint8_t const RED_LED = 11;
    uint8_t const BUTTON = 2;

    //mux-pins
    uint8_t const MUX0_PIN = 13;
    uint8_t const MUX1_PIN = 3;
    uint8_t const MUX2_PIN = 4;
    uint8_t const MUX_MASTER_PIN = A0;

    //because I have 9 sensors, a 8:1 MUX isn't enough. !! I start counting at 0 !!
    uint8_t const SENSOR8_PIN = A1;

    uint8_t const SOFTWARE_SERIAL_RX = 9;
    uint8_t const SOFTWARE_SERIAL_TX = 10;
    
    //in order to get values between 0-255
    int const cutoff = 670; 
    uint8_t const m[9] = {My, Tx, Rx, Ry, Lx, Ly, Ty, Dx, Mx};
    
}//end namespace version_2

inline namespace version_3 {
    uint8_t const BLUE_LED = 4;
    uint8_t const GREEN_LED = 3;
    uint8_t const RED_LED = 2;
    uint8_t const BUTTON = 1;

    //mux-pins
    uint8_t const MUX0_PIN = 5;
    uint8_t const MUX1_PIN = 8;
    uint8_t const MUX2_PIN = 6;
    uint8_t const MUX_MASTER_PIN = A2;

    //because I have 9 sensors, a 8:1 MUX isn't enough. !! I start counting at 0 !!
    uint8_t const SENSOR8_PIN = A1;

    uint8_t const SOFTWARE_SERIAL_RX = A1;
    uint8_t const SOFTWARE_SERIAL_TX = A2;
    
    //in order to get values between 0-255
    int const cutoff = 1024-680; 
    uint8_t const magnet_length = 20;
    uint8_t const additional_margin = 5;
    
    uint8_t const m[9] = {5, 7, 8, 3, 4, 1, 2, 0, 6};
    //~ uint8_t const m[9] = {0, 7, 5, 3, 2, 8, 4, 6, 1};
}//end namespace version_3

#endif //__HARDWARE_CONSTANTS_HEADER
