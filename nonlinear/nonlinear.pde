import com.hamoid.*;
VideoExport videoExport;

int SIZE_MULT = 160;
int WIDTH = 5;
int HEIGHT = WIDTH;

float LOWER = WIDTH * -1;
float UPPER = WIDTH * 1;
float DELTA = 0.05;

void setup(){
  frameRate(60);
  surface.setSize(WIDTH * SIZE_MULT, HEIGHT * SIZE_MULT);
  noFill();
  
  videoExport = new VideoExport(this);
  videoExport.startMovie();
}

PVector matmul(float a, float b, float c, float d, float x, float y){
  return new PVector(a*x + b*y, c*x + d*y);
}

PVector f(float x, float y){
  float theta = millis()*0.0005;
  
  // define matrix
  float a,b,c,d;
  a = tan(theta*0.1); b = -sin(theta) + sin(x);
  c = sin(theta) + sin(x); d = cos(theta) + sin(x);
  
  return conv(matmul(a,b,c,d,x,y));
}

PVector conv(PVector point){
  return new PVector(point.x * SIZE_MULT, point.y * SIZE_MULT);
}

void draw_grid(){
  // draw grid
  stroke(100);
  noFill();
  for(float t = LOWER; t < UPPER; t += 1){
    if (t == 0) continue;
    
    beginShape();
    for(float s = LOWER; s < UPPER; s += DELTA){
      PVector point = f(s, t);
      vertex(point.x, point.y);
    }
    endShape();
    
    beginShape();
    for(float s = LOWER; s < UPPER; s += DELTA){
      PVector point = f(t, s);
      vertex(point.x, point.y);
    }
    endShape();
  }
  
  stroke(255);
  
  // draw y axis
  beginShape();
  for(float t = LOWER; t < UPPER; t += DELTA){
    PVector point = f(0, t);
    vertex(point.x, point.y);
  }
  endShape();
  
  // draw x axis
  beginShape();
  for(float t = LOWER; t < UPPER; t += DELTA){
    PVector point = f(t, 0);
    vertex(point.x, point.y);
  }
  endShape();
}


void draw(){
  scale(1, -1);
  translate(width/2, -height/2);
  background(0);
  
  draw_grid();
  videoExport.saveFrame();
}

void keyPressed() {
  if (key == 'q') {
    videoExport.endMovie();
    exit();
  }
}
