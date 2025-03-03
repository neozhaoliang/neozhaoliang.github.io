window.requestAnimationFrame = window.requestAnimationFrame ||
    window.mozRequestAnimationFrame ||
    window.webkitRequestAnimationFrame ||
    window.msRequestAnimationFrame;
window.onload = start;

const branch_angle = Math.PI / 3;

var canvas;
var ctx;
var current_text_size = 12;
var render_depth = 8;
var text_depth = 6;

function start() {
    init();
    loop();
}

function init() {
    canvas = document.getElementById("canvas");
    ctx = canvas.getContext("2d", { alpha: false });
    ctx.fillStyle = "#333";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.scale(canvas.height / 2, -canvas.height / 2);
    ctx.translate(canvas.width / canvas.height, -1);
}

function loop() {
    plot_circle([[0, 0], 1], 0.01, "#FF00FF")
    plot_hyperbolic_segment([0.5, 0], [0.5, 0.5], 0.01, "#FFF000");
    window.requestAnimationFrame(loop);
}

function clamp_twopi(x) {
    const twopi = 2 * Math.PI;
    return (x + twopi) % twopi;
}

function cross2d(A, B) {
    return A[0] * B[1] - A[1] * B[0];
}

function squared_dist(A, B) {
    var dx = A[0] - B[0];
    var dy = A[1] - B[1];
    return dx * dx + dy * dy;
}

function squared_norm(A) {
    return A[0] * A[0] + A[1] * A[1];
}

function plot_point(P, radius, color = "#000000") {
    ctx.beginPath();
    ctx.arc(P[0], P[1], radius, 0, 2 * Math.PI, false);
    ctx.fillStyle = color;
    ctx.fill();
}

function plot_line(A, B, lw, color = "#000000") {
    ctx.beginPath();
    ctx.lineWidth = lw;
    ctx.strokeStyle = color;
    ctx.moveTo(A[0], A[1]);
    ctx.lineTo(B[0], B[1]);
    ctx.stroke();
}

function plot_circle(C, lw, color = "#000000") {
    var [center, radius] = C;
    ctx.beginPath();
    ctx.arc(center[0], center[1], radius, 0, 2 * Math.PI, false);
    ctx.lineWidth = lw;
    ctx.strokeStyle = color;
    ctx.stroke();
}

function circle_from_three_points(A, B, C) {
    var dx = B[0] - A[0],
        dy = B[1] - A[1],
        ex = C[0] - A[0],
        ey = C[1] - A[1];
    var
        bl = dx * dx + dy * dy,
        cl = ex * ex + ey * ey,
        d = 0.5 / (dx * ey - ex * dy);
    var
        x = (ey * bl - dy * cl) * d,
        y = (dx * cl - ex * bl) * d,
        r = Math.sqrt(x ** 2 + y ** 2);
    return [[A[0] + x, A[1] + y], r];
}

function hyperbolic_line(A, B) {
    var cx;
    var cy;
    var radius;
    var q = cross2d(A, B);
    var r1 = squared_norm(A) + 1;
    var r2 = squared_norm(B) + 1;

    cx = (r1 * B[1] - r2 * A[1]) / q / 2;
    cy = -(r1 * B[0] - r2 * A[0]) / q / 2;
    radius = Math.sqrt(cx * cx + cy * cy - 1);

    return [[cx, cy], radius];
}

function hyperbolic_segment(A, B) {
    var [[cx, cy], radius] = hyperbolic_line(A, B);
    var x1, y1 = A;
    var x2, y2 = B;
    var
        angle0 = Math.atan2(y1 - cy, x1 - cx),
        angle1 = Math.atan2(y2 - cy, x2 - cx);
    var theta0 = clamp_twopi(angle0 - angle1),
        theta1 = clamp_twopi(angle1 - angle0);
    var min_angle = Math.min(theta0, theta1),
        max_angle = Math.max(theta0, theta1);
    return [[cx, cy], radius, [min_angle, max_angle]];
}

function plot_hyperbolic_segment(A, B, lw, color = "#000000") {
    var [[cx, cy], radius, [min_angle, max_angle]] = hyperbolic_segment(A, B);
    ctx.beginPath();
    ctx.arc(cx, cy, radius, min_angle, max_angle, false);
    ctx.lineWidth = lw;
    ctx.strokeStyle = color;
    ctx.stroke();
}