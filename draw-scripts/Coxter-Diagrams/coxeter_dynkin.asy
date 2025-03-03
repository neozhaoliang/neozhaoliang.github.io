settings.outformat = "svg";
usepackage("mathpazo");
string outname = "cp2";

real u = 3cm;
real radius = 0.15cm;

pair v0 = E * u + E * sqrt(3) * u / 2 + N * 0.5 * u;
pair v1 = (E + N) * u;
pair v3 = (0, 0);
pair v4 = E * u ;
pair v2 = N * u ;
//pair v0 = (-v2.x, v2.y);
//pair v1 = (-v3.x, v3.y);

pen p2 = black + linewidth(0.03cm);
draw(v2 -- v3 -- v4 -- v2 -- v1 -- v4 -- v0 -- v1 , p2);
//draw(v0 -- v1 -- v4 -- cycle, p2);
//draw(v0 -- v1, p2);

pen p3 = yellow + 0.2green;
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
//label("", mid(v2, v3), p=p0);
label("5", mid(v0, v4), p=p0);
label("$\infty$", mid(v0, v1), p=p0);
label("$\infty$", mid(v4, v1), p=p0);

shipout(
    outname,
    bbox(
        xmargin=0.1cm, ymargin=0.1cm,
        FillDraw(fillpen=white, drawpen=white)
    )
);
