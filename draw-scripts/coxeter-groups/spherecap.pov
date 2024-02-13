#version 3.7;

#include "colors.inc"


global_settings {
    assumed_gamma 2.2
    max_trace_level 8
}

background { color White }


#declare s = 1.5*y;

#declare nor = vnormalize(s);
#declare dist = vlength(s);
#declare invd = 1 / dist;

torus {
    sqrt(1-invd*invd), 0.025
    pigment {
        color Red
    }
    finish {
        ambient 0.5
        diffuse 0.5
        reflection 0.1
        specular 0.4
        roughness 0.02
        }
    translate <0, invd, 0>
}
sphere {
    <0, 0, 0> 1
    pigment {
        color rgb 0.6
        transmit 0.8
    }
    finish {
        ambient 0.4
        diffuse 0.6
        reflection 0
        specular 0.2
        roughness 0.003
        irid { 0.3 thickness 0.2 turbulence 0.05 }
        conserve_energy
        }
    }

light_source {
    <4, 10, 0>
    color <1.0, 1.0,  1.0>
}

light_source {
    <100, -10, -100>
    color rgb 0.8
}


sphere {
    s, 0.04
    pigment {
        color Blue
    }
    finish {
        ambient 0.5
        diffuse 0.5
        reflection 0.1
        specular 0.4
        roughness 0.02
    }
}

box {
    #local k = 1.2;
    <-k, -0.001, -k>, <k, 0.001, k>
    pigment {
        color Green
        transmit 0.7
    }
    finish {
        diffuse .5 ambient .5 reflection .2 phong 0.5
    }
    translate invd * y
}


 cone {
    s, 0.0
    invd*y, sqrt(1-invd*invd)
    pigment {
        color Pink
        transmit 0.5
    }
    finish {
        ambient 0.5
        diffuse 0.5
        reflection 0
        specular 0.4
        roughness 0.003
    }
  }

camera {
    location <0, 2, -4>*0.8
    right     x*image_width/image_height
    look_at  <0, 0.2,  0> // <x, y, z>
    up y
    sky z
}
