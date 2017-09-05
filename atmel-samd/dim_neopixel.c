#include "dim_neopixel.h"

int dim_level = 40;
bool neopixel_dim = false;

void dim_neopixel_enable(){
      neopixel_dim = true;
}

void dim_neopixel_disable(){
      neopixel_dim = false;
}

void set_dim_level(int level){
      dim_level = level;
}

int get_dim_level(){
      return dim_level;
}

bool dim_neopixel_is_enabled(){
      return neopixel_dim;
}
