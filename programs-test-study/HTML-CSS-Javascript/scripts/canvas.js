// canvas is a API (Application Programming Interface) for browsers, used through Javascript
// floating dots effect background

const canvas = document.getElementById("draw-area");                            // element canvas
const canvas_rendering_context = canvas.getContext("2d");                       // get rendering context object, for graphics rendering

// get the width and height of the canvas element, defined using the "<canvas>" tag attributes
canvas.width = window.innerWidth;
canvas.height = window.innerHeight
let canvasWidth  = canvas.width;
let canvasHeight = canvas.height;

console.log(canvasWidth, canvasHeight);

// creates the mouse object
const mouse = {
  x: null,
  y: null,
  radius: 100 // circumference that the mouse occupies
};

// wait for a mouse movement event
canvas.addEventListener('mousemove', (event) => {
  mouse.x = event.x;
  mouse.y = event.y;
  console.log(event)
});

// when the window is resized, adjust canvas size and reinitialize particles
window.addEventListener('resize', () => {
  canvas.width  = window.innerWidth;
  canvas.height = window.innerHeight;
  canvasWidth   = canvas.width;
  canvasHeight  = canvas.height;
  init();
});

/* class to create the "particle" object through the "constructor" function,
   and functions necessary for its movement */
class Particle {
  // creates the "particle" object with its definitions
  constructor(x, y, size, speedX, speedY) {
    this.x      = x;
    this.y      = y;
    this.size   = size;
    this.speedX = speedX;
    this.speedY = speedY;
  }

  // function that updates the movement and behavior of the object "particle"
  update() {
    // move according to speed
    this.x += this.speedX;
    this.y += this.speedY;

    // bounce off the canvas edges
    if (this.x + this.size > canvasWidth) {
       this.x      = canvasWidth - this.size;
       this.speedX *= -1;
    } else if (this.x - this.size < 0) {
      this.x      = this.size;
      this.speedX *= -1;
    }
    if (this.y + this.size > canvasHeight) {
       this.y      = canvasHeight - this.size;
       this.speedY *= -1;
    } else if (this.y - this.size < 0) {
      this.y      = this.size;
      this.speedY *= -1;
    }

    // get the value of the distance between the particle and the mouse
    const distanceX = this.x - mouse.x;
    const distanceY = this.y - mouse.y;
    const distance  = Math.sqrt(distanceX * distanceX + distanceY * distanceY);

    // if the particle is within the mouse's "radius", push it away
    if (distance < mouse.radius) {
      const angle = Math.atan2(distanceY, distanceX);                 // direction from particle to mouse
      const force = (mouse.radius - distance) / mouse.radius;         // stronger when closer

      const moveX = force * Math.cos(angle) * 10;                     // X component of the push
      const moveY = force * Math.sin(angle) * 10;                     // Y component of the push

      this.x += moveX;
      this.y += moveY;
    }
  }

  // draws the particle as a circle in the canvas
  draw() {
    canvas_rendering_context.beginPath();
    canvas_rendering_context.arc(this.x, this.y, this.size, 0, Math.PI * 3);
    canvas_rendering_context.fillStyle = 'rgba(0, 0, 0, 1)';
    canvas_rendering_context.fill();
  }
}

// initialize the points
function init() {
  particlesArray = [];
  const numberParticles = 100;
  for (let i = 0; i < numberParticles; i++) {
      const size   = Math.random() * 5;                            // particle radius
      const x      = Math.random() * canvasWidth;
      const y      = Math.random() * canvasHeight;
      const speedX = (Math.random() - 0.5) * 5;                    // horizontal speed
      const speedY = (Math.random() - 0.5) * 5;                    // vertical speed

    // create a Particle object with its values
    particlesArray.push(new Particle(x, y, size, speedX, speedY));
  }
}

/* function responsible for the animation loop,
   calling update() and draw() for each particle in the array */
function animate() {
  canvas_rendering_context.clearRect(0, 0, canvasWidth, canvasHeight);  // clear canvas

  if (mouse.x !== null && mouse.y !== null) {
     canvas_rendering_context.beginPath();
     canvas_rendering_context.arc(
       mouse.x, mouse.y, mouse.radius, 0, Math.PI * 2
     );
     canvas_rendering_context.strokeStyle = "rgba(100, 100, 100, 1)";
     canvas_rendering_context.lineWidth = 2;
     canvas_rendering_context.stroke();
  }
  particlesArray.forEach(particle => {
    particle.update();
    particle.draw();
  });

  requestAnimationFrame(animate);                                       // loop
}

init();
animate();

