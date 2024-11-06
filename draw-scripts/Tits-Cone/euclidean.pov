#version 3.7;

global_settings {
  assumed_gamma 1.0
}

#include "colors.inc"

background { White }

#macro FundCone(ht)
  #local p1 = <0, 0, ht>;
  #local p2 = <1, 1/sqrt(3), ht>;
  #local p3 = <1, -1/sqrt(3), ht>;
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

camera {
  location <0, -4, 2.8> * 3
  look_at <0, 0, 1>
  sky z
  up z
  right x*image_width/image_height
}

light_source {
  <3, -1, 20>
  color rgb 1.33
  area_light
  x*8 y*8
  5, 5
  jitter
  orient
  adaptive 2
}

#macro Raster(RScale, RLine)
  pigment {
    gradient x scale RScale
    color_map {
      [0.000   color rgb  <1,1,1>*0.1]
      [0+RLine color rgb  <1,1,1>*0.3]
      [0+RLine color rgbt <1,1,1,1>]
      [1-RLine color rgbt <1,1,1,1>]
      [1-RLine color rgb  <1,1,1>*0.3]
      [1.000   color rgb  <1,1,1>*0.5]
    }
  }
#end

#macro Grid(RasterScale, RasterHalfLine, Background_color)
  plane {
    <0, 0, 1>, 4
    texture{ pigment { Background_color filter 0.5 } }
    texture{ Raster(RasterScale, RasterHalfLine) }
    texture{ Raster(RasterScale, RasterHalfLine) rotate<0, 0, 60> }
    texture{ Raster(RasterScale, RasterHalfLine) rotate<0, 0, 120> }
  }
#end

#declare uppersheet = object {
  Grid(1, 0.025, White*1.3)
  bounded_by {
    box { <-5, -5, -5>, <5, 5, 5> }
  }
  clipped_by { bounded_by }
};

union {
  object { uppersheet }
  FundCone(6)
}

box {
  <-5, -5, -0.0001>, <5, 5, 0.0001>
  texture {
    pigment { color Quartz }
    finish { ambient 0.5 diffuse 0.5 }
  }
}

sphere {
  <0, 0, 0>, 0.15
  pigment { color rgb <0.5, 1, 0> }
  finish { diffuse 0.5 ambient 0.3 specular 0.2 roughness 0.025 }
}
