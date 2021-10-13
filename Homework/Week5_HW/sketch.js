let serial;
let latestData = "waiting for data";


function setup() {
 createCanvas(windowWidth, windowHeight);
 print("BEGIN!");
 console.log("starting!");

 serial = new p5.SerialPort();

 serial.list();
 serial.open('/dev/tty.usbserial-1410');

 serial.on('connected', serverConnected);

 serial.on('list', gotList);

 serial.on('data', gotData);

 serial.on('error', gotError);

 serial.on('open', gotOpen);

 serial.on('close', gotClose);
}

function serverConnected() {
 print("Connected to Server");
}

function gotList(thelist) {
 print("List of Serial Ports:");

 for (let i = 0; i < thelist.length; i++) {
  print(i + " " + thelist[i]);
 }
}

function gotOpen() {
 print("Serial Port is Open");
}

function gotClose(){
 print("Serial Port is Closed");
 latestData = "Serial Port is Closed";
}

function gotError(theerror) {
 print(theerror);
}

function gotData() {
 let currentString = serial.readLine();
  trim(currentString);
 if (!currentString) return;
 console.log(currentString);
 latestData = currentString;
}

function draw() {
    background(220,0,200);
    fill(0,0,0);
    text(latestData, 10, 10);
    //lastestData=map(lastestData,0,1186,0,250);
    //if (lastestData == 0) {
   
        //ellipse(width / 2,height /2 ,100,100);
    //} else {
       // rectMode(CENTER);
       // rect(width / 2, height / 2,100,100);
       //let m = map(latestData, 0, 1184, 0, 550);
    
       ellipse(500,500,lastestData,lastestData);

       
    }
