---
title: "Reaction-Diffusion simulation with pyglet and glsl"
date: 2015-03-23
url: "reaction-diffusion-simulation"
---

[This project](https://github.com/neozhaoliang/pywonderland/tree/master/src/grayscott) is motivated by [pmneila's javascript project](http://pmneila.github.io/jsexp/grayscott/). The core part of the code are the two GLSL shaders `reaction.frag` and `render.frag`. The python scripts are merely for setting the UI and compiling the GLSL code.

> Requirements: `pyglet` for the UI and OpenGL environment and `ffmpeg` for saving the animation to video files.


# Examples

1. Unstable

    <video src="/images/grayscott/unstable.mp4" controls>

2. Coral

    <video src="/images/grayscott/coral.mp4" controls>

3. Baceria

    <video src="/images/grayscott/bacteria.mp4" controls>  
     
    
# Usage


You may simply run `python main.py` and then use keyboard and mouse to play with the simulation (for keyboard and mouse control please see the printed doc).

You may also initialize the window by passing more options:

```shell
python main.py -size 800x600 -fps 400 -conf 1 -scale 2
```

Here `-size` is the size of the window, `-fps` is the frames per second of the animation, if not specified then max possible value will be used, `-conf` is the line number of the pattern that the program will load from the file `config.txt` (which contains a few precomputed patterns), `-scale` is the "resolution" factor of the texture.

You may also use an image file to control the growth of the pattern by adding the `-mask` option:

<video src="/images/grayscott/mask.mp4" controls>


# How to save the animation to a video file

Make sure `ffmpeg` is installed on your computer and can be found on system path, windows users need to manually add the path to your ffmpeg.exe to environment variables, then press `ctrl+v` to start saving the video and press `ctrl+v` again to stop the saving.

You can use the option `-videorate` to control the fps of the video (not the animation!) and the option `-samplerate` to control how often a frame is sampled from the animation. If the frames are sampled too frequently the size of the video file will grow very large.


# About the code


`pyglet` is only a thin wrapper of OpenGL so one has to write his own classes to manage things like `vao`, `vbo`, `framebuffer`, etc. There are some modules like `vispy` and `gletools` that does similar job, but that lays the burden of learning one more package.

I wrote two scripts `shader.py` and `framebuffer.py` for compiling the shader programs and rendering to texture. They are not meant to be serious tools, just kept simple and suffice for our work.

The GLSL code borrows heavily from pmneila's work, the most genius part in his code is the use of a `brush` variable (`u_mouse` in our program) as the interface between the shader and the UI.