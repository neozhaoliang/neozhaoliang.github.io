import settings;
settings.outformat = "svg";

real u = 1cm;
pair A = (-u,0);
pair B = (u,0);
pair C = A + W / sqrt(2) * u;
pair D = B + E / sqrt(2) * u;
filldraw(box((-2.5*u,-u),(-1.5*u,u)), lightgray, black);
filldraw(box((1.5*u,-u),(2.5*u,u)), lightgray, black);
draw(C--D);
draw(A--A+dir(135)*u);
draw(A--A+dir(225)*u);
draw(B--B+dir(45)*u);
draw(B--B+dir(-45)*u);
filldraw(circle((0,0),0.1*u),red,black+linewidth(1));
filldraw(circle((u,0),0.1*u),red,black+linewidth(1));
filldraw(circle((-u,0),0.1*u),red,black+linewidth(1));
label("$v$",(0,0),N*1.5);
label("$v'$",A,N*1.5);
label("$v''$",B,N*1.5);

label("$H$",(-2*u, 0), fontsize(12));
label("$K$",(2*u, 0), fontsize(12));
shipout(bbox(xmargin=0.3cm, ymargin=0.2cm, FillDraw(fillpen=white, drawpen=white)));
