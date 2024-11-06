import simplenode;

settings.tex="xelatex";
usepackage("mathpazo");
settings.outformat = "pdf";

real u = 2cm;
Arrow = Arrow(4);
pen text = black;
pen starttext = black;

pen temp = linewidth(0.8) + fontsize(9pt);

pen nodepen = white;

draw_t Initial = none;
draw_t State = compose(shadow, filldrawer(nodepen, darkgreen+0.6));
draw_t Accepting = compose(shadow, filler(nodepen),
                           drawer(darkgreen+1.8), drawer(white+0.6));
draw_t Starting = compose(shadow, filler(red),
                           drawer(darkgreen+1.8), drawer(white+0.6));

node q0 = Circle("$H_0$", (0, 0), text, Accepting),
     q1 = Circle("$H_1$", q0.pos + u*E, text, Accepting),
     q2 = Circle("$H_2$", q1.pos + u*E, text, Accepting),
     q3 = Circle("$H_3$", q2.pos + u*E, text, Accepting),
     q4 = Circle("$H_4$", q3.pos + u*E, text, Accepting),
     q5 = Circle("$H_5$", q4.pos + u*E, text, Accepting);

draw(q0, q1, q2, q3, q4, q5);

real arr_size = 3pt;
currentpen = temp + red;
draw(Label("$s_0$", RightSide), q0 .. loop(up) @ shorten, Arrow);
draw(Label("$s_0$", RightSide), q1 .. loop(up) @ shorten, Arrow);
draw(Label("$s_0$", RightSide), q4 .. loop(up) @ shorten, Arrow);
draw(Label("$s_0$", RightSide), q5 .. loop(up) @ shorten, Arrow);
draw(Label("$s_0$", LeftSide), q2 -- q3 @ shorten, Arrows(arr_size));

currentpen = temp + deepgreen;
draw(Label("$s_1$", LeftSide), q1 -- q2 @ shorten, Arrows(arr_size));
draw(Label("$s_1$", LeftSide), q3 -- q4 @ shorten, Arrows(arr_size));
draw(Label("$s_1$", RightSide), q0 .. loop(S) @ shorten, Arrow);
draw(Label("$s_1$", RightSide), q5 .. loop(S) @ shorten, Arrow);

currentpen = temp + blue;
draw(Label("$s_2$", LeftSide), q0 -- q1 @ shorten, Arrows(arr_size));
draw(Label("$s_2$", LeftSide), q4 -- q5 @ shorten, Arrows(arr_size));
draw(Label("$s_2$", RightSide), q2 .. loop(N) @ shorten, Arrow);
draw(Label("$s_2$", RightSide), q3 .. loop(N) @ shorten, Arrow);

real x = 2u;
real delta = 0.1u;
pair A = (x - delta, u - delta);
pair B = (x + 0.5*u + delta, u + delta);
fill(box(A, B), opacity(0.9)+gray*1.5);

draw("4", (x + 0.25*u, u), S, fontsize(8pt) + black);

currentpen = linewidth(0.5) + black;
real r = 0.03*u;
draw((x, u) -- (x+u, u));
filldraw(circle((x, u), r), red);
filldraw(circle((x+0.5*u, u), r), deepgreen);
filldraw(circle((x+u, u), r), blue);

shipout(bbox(xmargin=0.3cm, ymargin=0.2cm, FillDraw(fillpen=white, drawpen=white)));
