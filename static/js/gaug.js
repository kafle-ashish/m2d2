const opts = {
    lines: 0.14, // The number of lines to draw
    angle: 0.10, // The length of each line
    lineWidth: 0.14, // The line thickness
    radius: 0.80,
    pointer: {
      length: 0.43, // The radius of the inner circle
      strokeWidth: 0.35, // The rotation offset
      color: '#000000' // Fill color
    },
    limitMax: 'True', // If true, the pointer will not go past the end of the gauge
    colorStart: '#2DA3DC', // Colors
    colorStop: '#C0C0DB', // just experiment with them
    strokeColor: '#EEEEEE', // to see which ones work best for you
    generateGradient: true
  };
  let target = document.getElementById('canvas-preview'); // your canvas element
  let gauge = new Donut(target).setOptions(opts); // create sexy gauge!
  let target1 = document.getElementById('canvas-preview1'); // your canvas element
  let gauge1 = new Donut(target1).setOptions(opts); // create sexy gauge!
  gauge.maxValue = 100; // set max gauge value
  gauge.animationSpeed = 32; // set animation speed (32 is default value)
  gauge1.maxValue = 100; // set max gauge value
  gauge1.animationSpeed = 32; // set animation speed (32 is default value)