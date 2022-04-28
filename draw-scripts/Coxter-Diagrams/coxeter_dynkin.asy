settings.outformat = "eps";
usepackage("mathpazo");
string outname = "244-424-424-2-1111";

real u = 3cm;
real radius = 0.15cm;

pair v2 = E * u;
pair v3 = N * u;
pair v4 = W * u;
pair v1 = S * u;
pair v0 = (0, 0);

pen p2 = black + linewidth(0.03cm);
draw(v2 -- v3 -- v4 -- v1 -- v2, p2);
draw(v2 -- v0 -- v4, p2);

pen p3 = red + 0.2green;
filldraw(circle(v0, radius), p3);
filldraw(circle(v1, radius), p3);
filldraw(circle(v2, radius), p3);
filldraw(circle(v3, radius), p3);
filldraw(circle(v4, radius), p3);

pair mid(pair p1, pair p2) {
     return (p1 + p2) / 2.;
}

pen p0 = fontsize(0.8cm) + black;
real a = 0.7u;
label("4", mid(v2, v3), p=p0);
label("4", mid(v3, v4), p=p0);
label("4", mid(v4, v1), p=p0);
label("4", mid(v1, v2), p=p0);
label("4", mid(v2, v0), p=p0);
label("4", mid(v4, v0), p=p0);


shipout(
    outname,
    bbox(
        xmargin=0.1cm, ymargin=0.1cm,
        FillDraw(fillpen=white, drawpen=white)
    )
);
