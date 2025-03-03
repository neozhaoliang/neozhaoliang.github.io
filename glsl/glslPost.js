(function () { function r(e, n, t) { function o(i, f) { if (!n[i]) { if (!e[i]) { var c = "function" == typeof require && require; if (!f && c) return c(i, !0); if (u) return u(i, !0); var a = new Error("Cannot find module '" + i + "'"); throw a.code = "MODULE_NOT_FOUND", a } var p = n[i] = { exports: {} }; e[i][0].call(p.exports, function (r) { var n = e[i][1][r]; return o(n || r) }, p, p.exports, r, e, n, t) } return n[i].exports } for (var u = "function" == typeof require && require, i = 0; i < t.length; i++)o(t[i]); return o } return r })()({
  1: [function (require, module, exports) {
    var glslify = require('glslify');

    var preFunction = glslify(["\nprecision mediump float;\n#define GLSLIFY 1\n#define PI 3.14159265359\n#define PI2 6.28318530718\n\nuniform vec2 u_resolution;\nuniform vec2 u_mouse;\nuniform float u_time;\n\nuniform sampler2D u_tex0;\nuniform sampler2D u_tex1;\nuniform sampler2D u_tex2;\nuniform sampler2D u_tex3;\n#define iResolution u_resolution\n#define iTime u_time\n#define iChannel0 u_tex0\n#define iChannel1 u_tex1\n#define iMouse u_mouse\n\nvec3 draw_grid(vec2 uv)\n{\n  vec2 dd = 0.5 - abs(uv);\n  float d = min(dd.x, dd.y);\n  d = smoothstep(0.05, 0.0, d);\n  return vec3(d, 0, 0);}\n\nvec3 noise(vec2 id)\n{\n  vec3 p3 = fract(vec3(id.xyx) * vec3(0.1031, 0.11369, 0.13787));\n  p3 += dot(p3, p3.yzx + 33.33);\n  return fract((p3.xxy + p3.yzz) * p3.zyx);\n}\nfloat saw(float b, float t)\n{\n  t = fract(t);\n  return smoothstep(0.0, b, t) * smoothstep(1.0, b, t);\n}\n#define hash11(x) fract(x * 17.0 * fract(x * 0.3183099))\n\n"]);

    var glslCanvases = [];
    var glslEditors = [];
    var glslGraphs = [];


    function sliceOutMain(str) {
      var regex = /void mainImage\s*\(.*?\)\s*?{/img;
      var p = 1;
      var end = undefined;
      var match = regex.exec(str);
      if (!match) {
        console.log(str);
        return str;
      }
      for (var i = regex.lastIndex, len = str.length; i < len; i++) {
        if (str[i] == "{") {
          p += 1;
        } else if (str[i] == "}") {
          p -= 1;
        }
        if (p == 0) {
          end = i;
          break;
        }
        if (p < 0) {
          end = len;
          break;
        }
      }
      return str.substring(0, regex.lastIndex - match[0].length) + str.substring(end + 1, str.length);
    }

    function findClosingParen(str, idx) {
      var p = 0;
      for (var i = idx, len = str.length; i < len; i++) {
        if (str[i] == "{") {
          p += 1;
        } else if (str[i] == "}") {
          p -= 1;
        }
        if (p == 0) {
          return i;
        }
        if (p < 0) {
          return len;
        }
      }
    }

    function getMethods(str) {
      var functions = []
      var regex = /^\s*?[a-zA-Z\d]{1,6}\s*?(\S+)\(.*?\)\s*?{/img;
      while ((match = regex.exec(str)) !== null) {
        var msg = 'Found ' + match[1] + '. ';
        var last = findClosingParen(str, regex.lastIndex - 1);
        var first = regex.lastIndex - match[0].length;
        functions.push({ name: match[1], protoLength: match[0].length, first: regex.lastIndex, last: last });
        regex.lastIndex = last;
      }
      return functions;
    }
    function hasPrototypeFor(theString, name) {
      var regex = new RegExp('^\s*?[a-zA-Z0-9]{1,6} +' + name + '\(.*?\)\s*?;', 'img');
      return regex.exec(theString) != null;
    }
    function removeMethod(str, methods, method) {
      var to_return = str;
      var removed_amount = undefined;
      for (var j = 0; j < methods.length; j++) {
        if (methods[j].name == method) {
          if (hasPrototypeFor(str, method)) {
            to_return = str.substring(0, methods[j].first - methods[j].protoLength) + "" + str.substring(methods[j].last + 1, str.length);
            removed_amount = methods[j].last - methods[j].first + methods[j].protoLength;
          } else {
            to_return = str.substring(0, methods[j].first - 1) + ";" + str.substring(methods[j].last + 1, str.length);
            removed_amount = methods[j].last - methods[j].first + 1;
          }
        } else if (removed_amount) {
          methods[j].first -= removed_amount;
          methods[j].last -= removed_amount;
        }
      }

      return to_return;
    }

    function overrideCode(cumulativeCode, newCode) {
      if (!cumulativeCode) { return ""; }
      var newMethods = getMethods(newCode);
      var cumulativeMethods = getMethods(cumulativeCode);

      for (var j = 0; j < newMethods.length; j++) {
        cumulativeCode = removeMethod(cumulativeCode, cumulativeMethods, newMethods[j].name);
      }
      return cumulativeCode;
    }

    function loadGlslElements() {

      var postFunction = "\n\
void main(){\n\
    mainImage(gl_FragColor, gl_FragCoord.xy);\n\
}"
      // Load single Shaders
      var canvas = document.getElementsByClassName("canvas");
      for (var i = 0; i < canvas.length; i++) {
        glslCanvases.push(new GlslCanvas(canvas[i]));
      }

      // parse EDITORS
      var ccList = document.querySelectorAll(".codeAndCanvas");
      var cumulativeCode = "";

      for (var i = 0; i < ccList.length; i++) {
        var width = 250;
        var height = 250;
        var srcFile; var textures = [];
        var theme = "monokai";
        var preF = preFunction;
        var postF = postFunction;
        if (ccList[i].hasAttribute("literate")) {
          preF += "\n" + cumulativeCode;
        }
        if (ccList[i].hasAttribute("pre")) {
          preF += ccList[i].getAttribute("pre");
        }
        if (ccList[i].hasAttribute("pre_keep")) {
          cumulativeCode += ccList[i].getAttribute("pre_keep");
          preF += ccList[i].getAttribute("pre_keep");
        }
        if (ccList[i].hasAttribute("data")) {
          srcFile = ccList[i].getAttribute("data");
        } else {
          srcFile = ccList[i].innerHTML;
          ccList[i].innerHTML = "";
        }
        //        cumulativeCode += overrideCode(srcFile, cumulativeCode);
        //        preF = overrideCode(preF, srcFile);

        cumulativeCode += sliceOutMain(srcFile);
        if (ccList[i].hasAttribute("override")) {
          var k = ccList[i].getAttribute("override").split(",");
          var methods = getMethods(preF);
          for (var j = 0; j < k.length; j++) {
            preF = removeMethod(preF, methods, k);
          }
        }
        if (ccList[i].hasAttribute("data-width")) {
          width = ccList[i].getAttribute("data-width");
        }
        if (ccList[i].hasAttribute("data-theme")) {
          theme = ccList[i].getAttribute("data-theme");
        }
        if (ccList[i].hasAttribute("data-texture")) {
          textures[0] = ccList[i].getAttribute("data-texture");
        }
        if (ccList[i].hasAttribute("data-raw")) {
          preF = "";
          postF = "";
        }

        var editor = new GlslEditor(ccList[i], { canvas_width: width, canvas_height: height, theme: theme, canvas_follow: false, tooltips: false, exportIcon: false, frag_header: preF, frag_footer: postF, textures: textures });
        /*window.setTimeout(function(e,s){
          return function(){
            e.open(s);
            window.scrollTo(0,0);
          }}(editor,srcFile),glslEditors.length*500+500);*/
        editor.open(srcFile);
        glslEditors.push(editor);
        //		setTimeout(function(){ window.scrollTo(0,0);}, 100);
      }

      // parse GRAPHS
      var sfList = document.querySelectorAll(".simpleFunction");
      for (var i = 0; i < sfList.length; i++) {
        if (sfList[i].hasAttribute("data")) {
          var srcFile = sfList[i].getAttribute("data");
          glslGraphs.push(new GlslEditor(sfList[i], { canvas_width: 800, lineNumbers: false, canvas_height: 250, frag_header: preFunction, frag_footer: postFunction, tooltips: true }).open(srcFile));
        }
      }
      document.activeElement.blur();
      //	window.scrollTo(0,0);
      //
    }

    //loadGlslElements();

    window.onload = function () {
      window.scrollTo(0, 0);
      window.setTimeout(function () {
        window.scrollTo(0, 0);
        loadGlslElements();
        window.scrollTo(0, 0);
        setTimeout(function () { window.scrollTo(0, 0); }, 100);
      }, 100);
    }
  }, { "glslify": 2 }], 2: [function (require, module, exports) {
    module.exports = function (strings) {
      if (typeof strings === 'string') strings = [strings]
      var exprs = [].slice.call(arguments, 1)
      var parts = []
      for (var i = 0; i < strings.length - 1; i++) {
        parts.push(strings[i], exprs[i] || '')
      }
      parts.push(strings[i])
      return parts.join('')
    }

  }, {}]
}, {}, [1]);
