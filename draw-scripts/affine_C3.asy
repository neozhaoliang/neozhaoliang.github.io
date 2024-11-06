/******************************************************************************
 *                                  LICENSE                                   *
 ******************************************************************************
 *  This file is part of Mathematics-and-Physics.                             *
 *                                                                            *
 *  Mathematics-and-Physics is free software: you can redistribute it and/or  *
 *  modify it under the terms of the GNU General Public License as published  *
 *  by the Free Software Foundation, either version 3 of the License, or      *
 *  (at your option) any later version.                                       *
 *                                                                            *
 *  Mathematics-and-Physics is distributed in the hope that it will be useful *
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of            *
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             *
 *  GNU General Public License for more details.                              *
 *                                                                            *
 *  You should have received a copy of the GNU General Public License         *
 *  along with Mathematics-and-Physics.  If not, see                          *
 *  <https://www.gnu.org/licenses/>.                                          *
 ******************************************************************************/

import three;
import settings;
import tube;
settings.outformat = "svg";
settings.render = 8;
size(256);

currentprojection = perspective(
    camera = (2.0, -6.0, 1.5),
    up = (0.0, 0.0, 1.0),
    target = (0.0, 0.0, 0.0),
    zoom = 1.0
);

currentlight = light(diffuse = new pen[] {cyan, orange},
specular = new pen[] {black, white},
position = new triple[] {-Y+Z, X+Y+Z});

pen wgray = gray(0.3)+opacity(0.5);

triple A0 = (0, 0, 0);
triple A1 = (1, 0, 0);
triple A2 = (1, 1, 0);
triple A3 = (0, 1, 0);

triple B0 = (0, 0, 1);
triple B1 = (1, 0, 1);
triple B2 = (1, 1, 1);
triple B3 = (0, 1, 1);

triple C0 = (0, 0, 0);
triple C1 = (0.5, 0, 0);
triple C2 = (0.5, 0.5, 0);
triple C3 = (0.5, 0.5, 0.5);
real r = 0.01;
real r2 = r / 3.;

material blob = material(
    diffusepen = gray(0.3) + opacity(0.3),
    emissivepen = gray(0.2),
    specularpen = gray(0.2)
);

material blobB = material(
    diffusepen = gray(0.2) + opacity(0.7),
    emissivepen = gray(0.2),
    specularpen = gray(0.2)
);

material pipe = material(
    diffusepen = gray(0.1),
    emissivepen = gray(0.1),
    specularpen = gray(0.1)
);

material pipeA = material(
    diffusepen = blue,
    emissivepen = gray(0.1),
    specularpen = gray(0.1)
);

material pipeB = material(
    diffusepen = red,
    emissivepen = gray(0.1),
    specularpen = gray(0.1)
);

material pipeC = material(
    diffusepen = yellow,
    emissivepen = gray(0.1),
    specularpen = gray(0.1)
);

material ball = material(
    diffusepen = cyan,
    emissivepen = gray(0.1),
    specularpen = gray(0.1)
);

surface sphere = scale(2.2*r, 2.0*r, 2.0*r)*unitsphere;

picture pic1, pic2;
draw(pic1, surface(A0 -- A1 -- A2 -- A3 -- cycle, planar=true), surfacepen=blob, render(merge=true));
draw(pic1, surface(B0 -- B1 -- B2 -- B3 -- cycle, planar=true), surfacepen=blob, render(merge=true));
draw(pic1, surface(A0 -- A3 -- B3 -- B0 -- cycle, planar=true), surfacepen=blob, render(merge=true));
draw(pic1, surface(A1 -- A2 -- B2 -- B1 -- cycle, planar=true), surfacepen=blob, render(merge=true));
draw(pic1, surface(A0 -- A1 -- B1 -- B0 -- cycle, planar=true), surfacepen=blob, render(merge=true));
draw(pic1, surface(A2 -- A3 -- B3 -- B2 -- cycle, planar=true), surfacepen=blob, render(merge=true));
draw(pic1, surface(C0 -- C1 -- C2 -- cycle, planar=true), surfacepen=blobB, render(merge=true));
draw(pic1, surface(C1 -- C2 -- C3 -- cycle, planar=true), surfacepen=blobB, render(merge=true));
draw(pic1, surface(C0 -- C1 -- C3 -- cycle, planar=true), surfacepen=blobB, render(merge=true));
draw(pic1, surface(C0 -- C2 -- C3 -- cycle, planar=true), surfacepen=blobB, render(merge=true));

draw(pic1, tube(A0 -- A1 -- A2 -- A3 -- cycle, scale(r2)*unitcircle), surfacepen=pipe);
draw(pic1, tube(B0 -- B1 -- B2 -- B3 -- cycle, scale(r2)*unitcircle), surfacepen=pipe);
draw(pic1, tube(A0 -- B0, scale(r2)*unitcircle), surfacepen=pipe);
draw(pic1, tube(A1 -- B1, scale(r2)*unitcircle), surfacepen=pipe);
draw(pic1, tube(A2 -- B2, scale(r2)*unitcircle), surfacepen=pipe);
draw(pic1, tube(A3 -- B3, scale(r2)*unitcircle), surfacepen=pipe);


draw(pic1, tube(C0 -- C1, scale(r)*unitcircle), surfacepen=pipeA);
draw(pic1, tube(C2 -- C3, scale(r)*unitcircle), surfacepen=pipeA);

draw(pic1, tube(C0 -- C2, scale(r)*unitcircle), surfacepen=pipeB);
draw(pic1, tube(C2 -- C1, scale(r)*unitcircle), surfacepen=pipeB);
draw(pic1, tube(C3 -- C1, scale(r)*unitcircle), surfacepen=pipeB);

draw(pic1, tube(C0 -- C3, scale(r)*unitcircle), surfacepen=pipeC);

draw(pic1, shift(C0)*sphere, surfacepen=ball);
draw(pic1, shift(C1)*sphere, surfacepen=ball);
draw(pic1, shift(C2)*sphere, surfacepen=ball);
draw(pic1, shift(C3)*sphere, surfacepen=ball);

label(pic1, "$0$", C0 + (0, 0, -0.02), align=S);
label(pic1, "$1$", C1 + (0, 0, -0.02), align=S);
label(pic1, "$2$", C2 + (0.02, 0, 0), align=E);
label(pic1, "$3$", C3 + (0.01, 0, 0.01), align=NE);

add(pic1);