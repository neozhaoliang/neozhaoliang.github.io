#version 3.7;

global_settings {
  assumed_gamma 1.0
}

#include "colors.inc"
#include "math.inc"

background { White }

#declare edgeRad = 0.002;
#declare num_segments = 20;
#declare edgeCol = Yellow;
#declare facefilter = 0.5;
#declare faceCol = White*0.6;
#declare faceColDimmed = faceCol * 0.3;

#declare edgeFinish = finish {
  ambient 0.2 diffuse 0.5 reflection 0.1 specular 0.6 roughness 0.01
}

#declare faceFinish = finish {
  ambient 0.5 diffuse 0.5 specular 0.6 roughness 0.005
}

#macro faceTexture(ind, faceType)
  #if(faceType)
    #local col = faceCol;
  #else
    #local col = faceColDimmed;
  #end

  texture {
    pigment { col filter facefilter }
    finish { faceFinish }
  }
#end

// return the normal vector of a 3d plane passes through the
// projected points of two 4d vectors p1 and p2
#macro get_clipping_plane(p1, p2)
  #local p12 = vnormalize(p1+p2);
  VPerp_To_Plane(p1-p12, p2-p12)
#end

// compute the signed distance of a vector to a plane,
// all vectors here are in 3d.
#macro distance_point_plane(p, p0, pnormal)
  vdot(p-p0, pnormal) / vlength(pnormal)
#end

// check if a vectors p is in the halfspace defined
// by the plane passes through p0 and has orientation pNormal.
#macro on_same_side(p, p0, pnormal)
  #local result = false;
  #local innprod = vdot(pnormal, p-p0);
  #if (innprod > 0)
    #local result = true;
  #end
  result
#end

#macro get_arc(p, q, arc_size)
  sphere_sweep {
    cubic_spline
    num_segments + 3
    p, arc_size
    #for (ind, 0, num_segments)
      #local point = p + (q - p) * ind / num_segments;
      #local point = vnormalize(point);
      point, arc_size
    #end
    q, arc_size
  }
#end

#macro Edge(k, i1, i2)
  #local p = vertices[i1];
  #local q = vertices[i2];
  object {
    get_arc(p, q, edgeRad)
    texture {
      pigment { edgeCol }
      finish { edgeFinish }
    }
  }
#end

#macro Face(k, faceType, pts)
  union {
    #local num = dimension_size(pts, 1);
    #local rib = 0;
    #local ind = 0;
    #while (ind < num)
      #local rib = rib + pts[ind];
      #local ind = ind+1;
    #end
    #local rib = vnormalize(rib);

    #local ind = 0;
    #local planes = array[num];
    #local dists = array[num];
    #local sides = array[num];
    #while (ind < num)
      #local ind2 = ind + 1;
      #if (ind2 = num)
        #local ind2 = 0;
      #end
      #local planes[ind] = get_clipping_plane(pts[ind], pts[ind2]);
      #local dists[ind] = distance_point_plane(0, pts[ind], planes[ind]);
      #local sides[ind] = on_same_side(rib, pts[ind], planes[ind]);
      #if (sides[ind] != true)
        #local planes[ind] = -planes[ind];
      #end
      #local ind = ind+1;
    #end

    #if(num = 3)
      #local p1 = pts[0];
      #local p2 = pts[1];
      #local cen = pts[2];
      merge {
        get_arc(p1, cen, edgeRad)
        get_arc(p2, cen, edgeRad)
        no_shadow
        texture { pigment { edgeCol } finish { edgeFinish }}
      }
    #else
      #local p1 = pts[0];
      #local p2 = pts[2];
      #local cen = pts[3];
      merge {
        get_arc(p1, cen, edgeRad)
        get_arc(p2, cen, edgeRad)
        no_shadow
        texture { pigment { edgeCol } finish { edgeFinish }}
      }
    #end

    sphere {
      0, 1
      faceTexture(k, faceType)
      #local ind = 0;
      #while (ind < num)
        clipped_by { plane { -planes[ind], dists[ind] } }
        #local ind = ind+1;
      #end
    }
  }
#end

#macro FundCone(pts)
  #local ht = 1.1;
  #local p1 = pts[0] * ht;
  #local p2 = pts[1] * ht;
  #local p3 = pts[2] * ht;
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
  location <0, 0, 2.4>
  look_at <0, 0, 0>
  up y
  right x*image_width/image_height
}

light_source {
  <3, 10, 3>
  color rgb 1
}

union {
  #include "polyhedra-data.inc"
  rotate <-20, 15, 0>
}
