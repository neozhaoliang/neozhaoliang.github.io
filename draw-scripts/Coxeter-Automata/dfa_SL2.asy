import simplenode;

settings.tex="xelatex";
usepackage("mathpazo");
settings.outformat = "eps";

real u = 4cm;
Arrow = Arrow(5);
pen text = white;
pen starttext = black;
pen temp = linewidth(1.2) + fontsize(9pt);

pen nodepen = deepgreen;

draw_t Initial = none;
draw_t State = compose(shadow, filldrawer(nodepen, darkgreen+0.6));
draw_t Accepting = compose(shadow, filler(nodepen),
                           drawer(darkgreen+1.8), drawer(white+0.6));
draw_t Starting = compose(shadow, filler(red),
                           drawer(darkgreen+1.8), drawer(white+0.6));

real u2 = u / sqrt(3);
pair D = dir(225);
pair D2 = dir(-45);

node
     q0 = Circle("$q_{0}$", (0, 0), text, Starting),
     q1 = Circle("$q_{1}$", q0.pos + u2*W, text, Accepting),  
     q2 = Circle("$q_{2}$", q0.pos + u2*S, text, Accepting),
     q8 = Circle("$q_{3}$", q0.pos + u2*E, text, Accepting),
     q3 = Circle("$q_{8}$", q2.pos + u2*dir(240), text, Accepting),
     q4 = Circle("$q_{4}$", q1.pos + u2*S, text, Accepting),
     q7 = Circle("$q_{7}$", q8.pos + u2*S, text, Accepting),
     q6 = Circle("$q_{6}$", q2.pos + u2*dir(-60), text, Accepting),
     q9 = Circle("$q_{9}$", q7.pos + u2*dir(-60), text, Accepting),
     q5 = Circle("$q_{5}$", q4.pos + u2*dir(240), text, Accepting);

currentpen = temp;
node start = Circle("$\mathrm{Start}$", q0.pos + u/2.5*N, starttext, Initial);
draw(start, q6, q8, q7, q1, q2, q0, q3, q4, q5, q9);

draw(start -- q0 @ shorten(-2, 4), Arrow);

shorten = shorten(4, 4);
currentpen = temp + red*0.8;
draw(Label("$A$", LeftSide), q0 -- q8 @ shorten, Arrow);
draw(Label("$A$", LeftSide), q7 -- q9 @ shorten, Arrow);
draw("$A$", q2 -- q3 @ shorten, Arrow);
draw(Label("$A$", LeftSide), q4 -- q3 @ shorten, Arrow);
draw(Label("$A$", LeftSide), q9 .. bend(30) .. q3 @ shorten, Arrow);
draw(shift(u/5*dir(60))*Label("$A$", LeftSide), q3 .. bend(-20) .. q8 @ shorten, Arrow);
draw("$A$", q8 .. loop(N, 2.4)  @ shorten, Arrow);


currentpen = temp + olive;
draw(Label("$B$", RightSide), q0 -- q1 @ shorten, Arrow);
draw(Label("$B$", LeftSide), q2 -- q6 @ shorten, Arrow);
draw("$B$", q7 -- q6 @ shorten, Arrow);
draw("$B$", q4 -- q5 @ shorten, Arrow);
draw(Label("$B$", RightSide), q5 .. bend(-30) .. q6 @ shorten, Arrow);
draw(shift(u/5*dir(120))*Label("$B$", RightSide), q6 .. bend(20) .. q1 @ shorten, Arrow);
draw("$B$", q1 .. loop(N, 2.4)  @ shorten, Arrow);

currentpen = temp + rgb(30, 144, 255);
draw("$C$", q0 -- q2 @ shorten, Arrow);
draw("$C$", q1 -- q4 @ shorten, Arrow);
draw(Label("$C$", LeftSide), q8 -- q7 @ shorten, Arrow);

currentpen = temp;
shipout(bbox(xmargin=0.3cm, ymargin=0.2cm, FillDraw(fillpen=white, drawpen=white)));
