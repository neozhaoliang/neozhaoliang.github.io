settings.tex = "xelatex";
settings.outformat = "pdf";
usepackage("mathpazo");
string outname = "diagram-4-3";

real u = 2cm;
real radius = 0.1cm;
pair A = (-2, 0);
pair B = A + 2u*E;
pair C = (A + B) / 2;

draw(A -- B);

filldraw(circle(A, radius*2), white);
filldraw(circle(A, radius), yellow);
filldraw(circle(B, radius), yellow);
filldraw(circle(C, radius), yellow);

label("$4$", (A + C) / 2 + 0.12u*N, p=fontsize(9pt));

shipout(
    outname,
    bbox(
        xmargin=0.2cm, ymargin=0.1cm,
        FillDraw(fillpen=white, drawpen=white)
    )
);
