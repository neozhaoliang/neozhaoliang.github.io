#version 3.7;

#include "colors.inc"
#include "transforms.inc"

global_settings {
  assumed_gamma 1.0
}

background { Quartz }

#declare imagename = "tex-noncompact.png";

#declare hyperboloid_transparency = 0.3;
// mirrors for the (7, 3) tiling
#declare m1 = <1, 0, 0>;
#declare m2 = <-cos(pi/3), sin(pi/3), 0>;
#declare aa = -1.1;
#declare bb = (cos(pi/3)*aa - cos(pi/2)) / sin(pi/2);
#declare cc = -sqrt(aa*aa + bb*bb - 1);
#declare m3 = <aa, bb, cc>;
// vertices for the fundamental cone, all are in halfspace z > 0
#declare A = vcross(m1, m2);
#declare B = <0, m3.z/m3.y, 1>;
#declare C = vcross(<m3.x, m3.y, -m3.z>, m2);

#macro FundCone(ht)
  #local p1 = A / A.z * ht;
  #local p2 = B / B.z * ht;
  #local p3 = C / C.z * ht;
  #local n = vnormalize(vcross(p2, p3));
  box {
    <p2.x, p2.y, p2.z>, <-p2.x, -p2.y, -0.001>
    pigment { color Blue transmit 0.4 }
    finish { ambient 0.7 diffuse 0.3 specular 0.2 roughness 0.02 }
  }
#end

#declare projx = function (x,y,z) { x/z }
#declare projy = function (x,y,z) { y/z }

#declare ImageFn = function {
  pigment {
    image_map { png imagename once }
    translate <-.5, -.5, 0>
  }
}

#declare PigmentR = pigment {
  function { ImageFn(projx(x,y,z)/2, projy(x,y,z)/2, 0).red }
  color_map {
    [ 0 color rgbt <0, 0, 0, hyperboloid_transparency>]
    [ 1 color rgbt <3, 0, 0, hyperboloid_transparency> ]
  }
}

#declare PigmentG = pigment {
  function { ImageFn(projx(x,y,z)/2, projy(x,y,z)/2, 0).green }
  color_map {
    [ 0 color rgbt <0, 0, 0, hyperboloid_transparency>]
    [ 1 color rgbt <0, 3, 0, hyperboloid_transparency> ]
  }
}

#declare PigmentB = pigment {
  function { ImageFn(projx(x,y,z)/2, projy(x,y,z)/2 ,0).blue }
  color_map {
    [ 0 color rgbt <0, 0, 0, hyperboloid_transparency>]
    [ 1 color rgbt <0, 0, 3, hyperboloid_transparency> ]
  }
}

#declare hyperboloid = object {
  poly {
    2, <1, 0, 0, 0, 1, 0, 0, -1, 0, 1>
  }
  clipped_by { plane{-z, 0 } }
  clipped_by { plane{ z, 2 } }
  texture {
    pigment {
      average
      pigment_map {
        [ PigmentR ]
        [ PigmentG ]
        [ PigmentB ]
      }
    }
    finish {
      ambient 0.7
      diffuse 0.3
      reflection 0
      specular 0.2
      roughness 0.2
      irid { 0.3 thickness 0.2 turbulence 0.05 }
      conserve_energy
    }
  }
}

#declare lightcone = object {
  poly {
    2, <1, 0, 0, 0, 1, 0, 0, -1, 0, 0>
  }
  clipped_by{ plane{-z, 0} }
  clipped_by{ plane{ z, 1.5} }
  pigment { Pink }
  finish {
    ambient 0.8
    diffuse 0.2
    reflection 0
    roughness 0.25
  }
}

//object{ hyperboloid }
object { lightcone }
plane {
  z, 1
  pigment {
    image_map { png imagename once }
    translate <-0.5, -0.5, 0>
    scale 2
  }
  finish {
    ambient 0.3 diffuse 0.7 reflection 0 roughness 0.25
  }
}


#declare ht = 2;

#declare rad = 0.04;

union {
 FundCone(ht)

sphere {
  B/B.z*ht, rad
  pigment {
    color rgb <1, 1, 0>
  }
  finish {
    diffuse 0.7
    specular 1
    reflection 0.2
    ambient 0.1
  }
}

sphere {
  <0, 0, 0>, rad
  pigment {
    color rgb <0, 0, 1>
  }
  finish {
    diffuse 0.7
    specular 1
    reflection 0.2
    ambient 0.1
  }
}
}

camera {
  location <2, 0, 4>
  look_at <0, 0, 1>
  sky z
  up z
  right x*image_width/image_height
}

light_source {
  <-10, 10, 6>
  color rgb 1
  area_light
  x*4 y*4
  5, 5
  jitter
  orient
  adaptive 2
}

torus {
  0.98, 0.02
  pigment { Red }
  finish {
    ambient 0.7
    diffuse 0.3
    specular 0.2
    roughness 0.02
  } // major radius, minor radius
  clipped_by {plane {-x, 0}}
  rotate <90, 0, 0>
  translate <0, 0, 1>
}