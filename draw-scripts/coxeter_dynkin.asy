settings.tex = "xelatex";
settings.outformat = "eps";
usepackage("courier");
string outname = "cubic-4311";

real u = .6cm;
real radius = 0.1cm;

pair A = (-2u, 0);
pair B = (0, 0);
pair C = sqrt(2)*u * (E + N);
pair D = sqrt(2)*u * (E + S);

draw(A -- B);
draw(B -- C);
draw(B -- D);

filldraw(circle(A, radius), yellow);
filldraw(circle(B, radius), yellow);
filldraw(circle(C, radius), yellow);
filldraw(circle(D, radius), yellow);

label("${\bf 4}$", (A + B) / 2 + 0.3u*N, p=fontsize(9pt));
//label("${\bf 4}$", (D + C) / 2 + 0.3u*N, p=fontsize(9pt));

shipout(
    outname,
    bbox(
        xmargin=0.2cm, ymargin=0.1cm,
        FillDraw(fillpen=white, drawpen=white)
    )
);
