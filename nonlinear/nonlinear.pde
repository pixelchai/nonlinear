int SIZE_MULT = 80;
int WIDTH = 10;
int HEIGHT = WIDTH;

int LOWER = WIDTH * -1;
int UPPER = WIDTH * 1;
float DELTA = 0.05;

color COL_BACKGROUND = color(0, 0, 0);
color COL_FOREGROUND = color(255, 255, 255);

void setup(){
  frameRate(20);
  surface.setSize(WIDTH * SIZE_MULT, HEIGHT * SIZE_MULT);
}

PVector matmul(float a, float b, float c, float d, float x, float y){
  return new PVector(a*x + b*y, c*x + d*y);
}

PVector f(float x, float y){
  float theta = millis()*0.0005;
  
  // define matrix
  float a,b,c,d;
  a = cos(theta) + cos(x); b = -sin(theta) + cos(y);
  c = sin(theta) + cos(x); d = cos(theta) + cos(y);
  
  return matmul(a,b,c,d,x,y);
}

void plot(float x, float y, color col, float size){
  fill(col);
  rect((x - size/2)*SIZE_MULT, (y + size/2)*SIZE_MULT, size*SIZE_MULT, size*SIZE_MULT);
}

void plot(float x, float y, color col){
  plot(x, y, col, 0.05);
}

void plot(PVector point, color col){
  plot(point.x, point.y, col);
}

void draw_grid(){
  // draw grid
  for(float t = LOWER; t < UPPER; t += 1){
    if (t == 0) continue;
    
    for(float s = LOWER; s < UPPER; s += DELTA){
      plot(f(s, t), 100);
      plot(f(t, s), 100);
    }
  }
  
  // draw axes
  for(float t = LOWER; t < UPPER; t += DELTA){
    plot(f(0, t), 255);
    plot(f(t, 0), 255);
  }
}


void draw(){
  scale(1, -1);
  translate(width/2, -height/2);
  background(0);
  
  draw_grid();
  //plot(0, 0, 255, 1);
}
