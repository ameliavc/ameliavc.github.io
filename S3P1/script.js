function preload() {
  note1 = loadSound('Audio/Note C.mp3');
  note2 = loadSound('Audio/Note D.mp3');
  note3 = loadSound('Audio/Note E.mp3');
  note4 = loadSound('Audio/Note F.mp3');
  note5 = loadSound('Audio/Note G.mp3');
  note6 = loadSound('Audio/ThatsIt.mp3');}
function setup() {
  noCanvas();
}

cvalue = 0
dvalue = 0
evalue = 0
fvalue = 0
gvalue = 0
avalue = 0



// e = 12
function changeColor() {
if (evalue === 1) {
    e1 = select('#e1');
    e1.style('background-color', 'yellow');
}
  
if (evalue === 2) {
    e2 = select('#e2');
    e2.style('background-color', 'yellow');
}

if (evalue === 3) {
    e3 = select('#e3');
    e3.style('background-color','yellow');
}

if (evalue === 4) {
    e4 = select('#e4');
    e4.style('background-color','yellow');
}

if (evalue === 5) {
    e5 = select('#e5');
    e5.style('background-color','yellow');
}

if (evalue === 6) {
    e6 = select('#e6');
    e6.style('background-color','yellow');
}

if (evalue === 7) {
    e7 = select('#e7');
    e7.style('background','yellow');
}

if (evalue === 8) {
    e8 = select('#e8');
    e8.style('background','yellow');
}

if (evalue === 9) {
    e9 = select('#e9');
    e9.style('background','yellow');
}

if (evalue === 10) {
    e_10 = select('#e_10');
    e_10.style('background','yellow');
}

if (evalue === 11) {
    e_11 = select('#e_11');
    e_11.style('background','yellow');
}

if (evalue === 12) {
    e_12 = select('#e_12');
    e_12.style('background','yellow');
}

// f = 5

if (fvalue === 1) {
    f1 = select('#f1');
    f1.style('background','yellow');
}

if (fvalue === 2) {
    f2 = select('#f2');
    f2.style('background','yellow');
}

if (fvalue === 3) {
    f3 = select('#f3');
    f3.style('background','yellow');
}

if (fvalue === 4) {
    f4 = select('#f4');
    f4.style('background','yellow');
}

if (fvalue === 5) {
    f5 = select('#f5');
    f5.style('background','yellow');
}

// g = 3

if (gvalue === 1) {
    g1 = select('#g1');
    g1.style('background','yellow');
}

if (gvalue === 2) {
    g2 = select('#g2');
    g2.style('background','yellow');
}

if (gvalue === 3) {
    g3 = select('#g3');
    g3.style('background','yellow');
}

// c = 1

if (cvalue === 1) {
    c1 = select('#c1');
    c1.style('background','yellow');
}

// d = 1

if (dvalue === 1) {
    d1 = select('#d1');
    d1.style('background','yellow');
}

// a = 1

if (avalue === 1) {
    a1 = select('#a1');
    a1.style('background','red');
}
}

function keyTyped() {
//   this may also be helpful with keyCode() https://www.toptal.com/developers/keycode
  if (key === 'c') {
      note1.play();
      cvalue += 1;
      changeColor();
    }
  if (key === 'd') {
      note2.play();
      dvalue += 1;
      changeColor();
    }
  if (key === 'e') {
      note3.play();
      evalue += 1;
      changeColor();
  }
  if (key === 'f') {
      note4.play();
      fvalue += 1;
      changeColor();
  }
  if (key === 'g') {
      note5.play();
      gvalue += 1;
      changeColor();
  }
  if (key === 'a') {
      note6.play();
      avalue += 1;
      changeColor();
  }
}

// Opt-in: //
// function typing() {
//   hint = select('#hint');
//   hint.html("try typing");
// }
