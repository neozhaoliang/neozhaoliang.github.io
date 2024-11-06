#version 3.7;

#include "colors.inc"

global_settings {
  assumed_gamma 1.0
}

background { Quartz }

#declare imagename = "tex-237-poincare.png";

#declare hyperboloid_transparency = 0.3;

#declare pqr = <2, 3, 7>;

// mirrors for the (7, 3) tiling
#declare m1 = <1, 0, 0>;
#declare m2 = <-cos(pi/pqr.x), sin(pi/pqr.x), 0>;
#declare X = -cos(pi/pqr.y);
#declare Y = (-cos(pi/pqr.z) - X * m2.x) / m2.y;
#declare m3 = <X, Y, -sqrt(X*X + Y*Y - 1)>;

// vertices for the fundamental cone, all are in halfspace z > 0
#declare A = vcross(m1, m2);
#declare B = vcross(m2, m3);
#declare C = vcross(m3, m1);

#macro FundCone(ht)
  #local p1 = A / A.z * ht;
  #local p2 = B / B.z * ht;
  #local p3 = C / C.z * ht;
  mesh2 {
    vertex_vectors {
      4,
      0, p1, p2, p3
    }
    face_indices {
      4,
      <0, 1, 2>,
      <0, 1, 3>,
      <0, 2, 3>,
      <1, 2, 3>
    }
    pigment { color Red }
    finish { ambient 0.3 diffuse 0.8 specular 0.2 roughness 0.2 }
  }
#end

#declare projx = function (x,y,z) { x/(1+z) }
#declare projy = function (x,y,z) { y/(1+z) }

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
  clipped_by{ plane{ z, 2} }
  pigment { Pink  transmit 0.5 }
  finish {
    ambient 0.8
    diffuse 0.2
    reflection 0
    roughness 0.25
    irid { 0.3 thickness 0.2 turbulence 0.05 }
    conserve_energy
  }
}
object{ hyperboloid }
object { lightcone }
plane {
  z, 1
  pigment {
    image_map { png imagename once }
    translate <-0.5, -0.5, 0>
    scale 4
  }
  finish {
    ambient 0.3 diffuse 0.7 reflection 0 roughness 0.25
  }
}

#declare ht = 2.5;
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
  location <3, 3, 4>
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
