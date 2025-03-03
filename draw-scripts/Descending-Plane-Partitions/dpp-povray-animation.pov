// Persistence of Vision Ray Tracer Scene Description File
// File: penrose.pov
// Vers: 3.7
// Date: 2018/02/08
// Auth: Zhao Liang mathzhaoliang@gmail.com

#version 3.7;

global_settings {
    assumed_gamma 1.0
}

/*=========================================================*/
/* Tiling                                                  */

#include "tiles.inc"
#include "data.inc"
#include "colors.inc"
#include "textures.inc"
/*=========================================================*/
/* Rubik's cube                                            */

#include "rubik.inc"

#declare Top = texture { pigment { rgb <0.314, 0.188, 0.475> } normal { FaceNormal } finish{ FaceFinish } }
#declare Bot = texture { pigment { rgb <0, 0, .8> } normal { FaceNormal } finish{ FaceFinish } }
#declare Lef = texture { pigment { rgb  <0.678, 0.847, 1> } normal { FaceNormal } finish{ FaceFinish } }
#declare Rig = texture { pigment { rgb <1, 0.569, 0.459> } normal { FaceNormal } finish{ FaceFinish } }
#declare For = texture { pigment { rgb <0.255, 0.648, 0.875> } normal { FaceNormal } finish{ FaceFinish } }
#declare Aft = texture { pigment { rgb <0.483, 0.233, 0.696> } normal { FaceNormal } finish{ FaceFinish } }
#declare mycube =
  object
  {
    union
    {
      object { Cube }
      object { FaceT texture { Top } }
      object { FaceL texture { Lef } }
      object { FaceF texture { For } }
      object { FaceR texture { Rig } }
      object { FaceA texture { Aft } }
      object { FaceB texture { Bot } }
    }
    scale 1 / wCube
    rotate y*270
    translate <1, 1, 1> * 0.5
  }


plane {
    y (-0.001)
    texture {
        pigment { rgb .8 }
        finish {
            specular 0.2
            roughness 0.5
            diffuse 0.8
        }
    }
}
#macro isTime(a, b)
  #local T = false;
  #if(clock >= a & clock <= b)
    #local T = true;
  #end
  T
#end

#macro setTime(a, b)
  #local T = 0.0;
  #if(clock < a)
    #local T = 0;
  #else
    #if(clock >= a & clock < b)
      #local T = (clock - a) / (b - a);
    #else
      #local T = 1.0;
    #end
  #end
  T
#end
/*=========================================================*/
/* Camera and Lights                                       */

#local cameraT = setTime(0, 0.2);
#local camRotT = setTime(0.85, 1.2);
camera {
  location <12 - cameraT*5, 20, 12 - cameraT*5>
  look_at <2, 0, 2>
  angle 35
  right x*image_width/image_height
  translate <-2, 0, -2>
  rotate <0, camRotT*360, 0>
  translate <2, 0, 2>
}


light_source {
    <1, 1, 1>*50
    color rgb <1, 1, 1>
    fade_distance 20
}


light_source {
    <-1, 2, 1>*100
    color rgb <1, 1, 1>*0.6
    fade_distance 20
}



#declare cubes = array[4] {
  array[6]{ 7, 7, 6, 6, 3, 1 },
  array[4]{ 6, 5, 4, 2 },
  array[2]{ 3, 3 },
  array[1]{ 2 },
};


#macro rowOfCubes(num, transVect)
  union {
    #for(k, 0, num-1)
      object {
        mycube
        translate z*k
      }
    #end
    translate transVect
  }
#end

#macro layerOfCubes(arr, transVect1, transVect2)
  #for(row, 0, dimension_size(arr, 1) - 1)
    #local num = arr[row];
    #if(row=0)
      rowOfCubes(num, x*row + transVect1 + transVect2)
    #else
      rowOfCubes(num, x*row + transVect1)
    #end
  #end
#end

#declare thick = 0.08;
#declare pathTex = texture{ pigment { color <0.9, 0, 0> } finish { roughness 0.005 reflection 0.2 diffuse 0.5 specular 1 }};
#macro path(pts)
 #local len = dimension_size(pts, 1);
 #if(len> 2)
  union {
    #for(ind, 0, len - 2)
      #local P = pts[ind];
      #local Q = pts[ind + 1];
      sphere_sweep {
        linear_spline
        11,
        #for(k, 0, 10)
          P + k * (Q - P) / 10, thick
        #end
      }
    #end
    texture { pathTex }
    translate <0, 0.5, 0>
  }
  #else
      #local P = pts[0];
      #local Q = pts[1];
      sphere_sweep {
        linear_spline
        11,
        #for(k, 0, 10)
          P + k * (Q - P) / 10, thick
        #end
        texture { pathTex }
        translate <0, 0.5, 0>
      }
  #end
#end

#macro path2(pts, tv)
  #local len = dimension_size(pts, 1);
  #if(len > 2)
  union {
    #for(ind, 0, len - 2)
      sphere_sweep {
        linear_spline
        11,
        #local P = pts[ind];
        #local Q = pts[ind + 1];
        #for(k, 0, 10)
          P + k * (Q - P) / 10, thick
        #end
      }
    #end
    texture { pathTex }
    translate <0, 0.5, 0> + tv
  }
  #else
      sphere_sweep {
        linear_spline
        11,
        #local P = pts[0];
        #local Q = pts[1];
        #for(k, 0, 10)
          P + k * (Q - P) / 10, thick
        #end
        texture { pathTex }
        translate <0, 0.5, 0> + tv
       }
  #end
#end

#local slideT = setTime(0.25, 0.45);
#local removeT = setTime(0.55, 0.8);

#local pathT = isTime(0.45, 0.55);
#local moveT = isTime(0.55, 1.2);
#if(pathT)
  //-----------------
  path(array[9]{
    <6, 0, 0>,
    <6, 0, 1>,
    <5, 0, 1>,
    <5, 0, 3>,
    <4, 0, 3>,
    <4, 0, 6>,
    <2, 0, 6>,
    <2, 0, 7>,
    <0, 0, 7>
  })
  //-----------------
  path(array[10]{
    <5, 1, 0>
    <4, 1, 0>,
    <4, 1, 2>,
    <3, 1, 2>,
    <3, 1, 4>,
    <2, 1, 4>,
    <2, 1, 5>,
    <1, 1, 5>,
    <1, 1, 6>,
    <0, 1, 6>
  })
  //-----------------
  path(array[3]{
    <2, 2, 0>,
    <2, 2, 3>,
    <0, 2, 3>
  })
  //--------
  path(array[3]{
    <1, 3, 0>,
    <1, 3, 2>,
    <0, 3, 2>
  })
#end

#if(moveT)
  path(array[9]{
    <6, 0, 0>,
    <6, 0, 1>,
    <5, 0, 1>,
    <5, 0, 3>,
    <4, 0, 3>,
    <4, 0, 6>,
    <2, 0, 6>,
    <2, 0, 7>,
    <1, 0, 7>
  })
  //-----------------
  path(array[9]{
    <5, 1, 0>
    <4, 1, 0>,
    <4, 1, 2>,
    <3, 1, 2>,
    <3, 1, 4>,
    <2, 1, 4>,
    <2, 1, 5>,
    <1, 1, 5>,
    <1, 1, 6>
  })
  //-----------------
  path(array[3]{
    <2, 2, 0>,
    <2, 2, 3>,
    <1, 2, 3>
  })
  //-----------------
  path(array[2]{
    <1, 3, 0>,
    <1, 3, 2>
  })
  
  path2(array[2]{
    <1, 0, 7>,
    <0, 0, 7>
  }, removeT*20*(-x))
  
  path2(array[2]{
    <1, 1, 6>,
    <0, 1, 6>
  }, removeT*20*(-x))
  
  path2(array[2]{
    <1, 2, 3>,
    <0, 2, 3>
  }, removeT*20*(-x))
  
  path2(array[2]{
    <1, 3, 2>,
    <0, 3, 2>
  }, removeT*20*(-x))
#end

#for(row, 0, dimension_size(cubes, 1) - 1)
  #local arr = cubes[row];
  layerOfCubes(
    arr,
    row*<1,1,1> + row*<-1, 0, -1>*slideT,
    removeT*20*(-x)
  )
#end
