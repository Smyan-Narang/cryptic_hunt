var app = document.getElementById('app');
var mainApp = document.getElementById('mainapp');
var typewriterNew = new Typewriter(mainApp, {
    loop: false,
    delay: 75,
    autoStart: true,
    cursor: '█',
    strings: ['']
  });
typewriterNew
    .typeString('KRYPTOS - SHISTECH 2022')
var typewriter = new Typewriter(app, {
  loop: false,
  delay: 100,
  autoStart: true,
  cursor: '█',
  strings: [''],
});
typewriter
  .pauseFor(1800)
  .typeString('SHISTECH KRYPTOS')
  .deleteAll(1)
  .pauseFor(50)
  .deleteAll(1)
  .typeString('The cryptic hunt shall begin on 1st October 12:00 AM.')
  .pauseFor(300)
  .deleteAll(1)
  .typeString("KRYPTOS is SHISTECH's cryptic hunt")


  var input = document.getElementById('input')

  var customNodeCreator = function(character) {
    // Add character to input placeholder
    input.placeholder = input.placeholder + character;
  
    // Return null to skip internal adding of dom node
    return null;
  }
  
  var onRemoveNode = function({ character }) {
    if(input.placeholder) {
      // Remove last character from input placeholder
      input.placeholder = input.placeholder.slice(0, -1)
    }
  }
  
  var typewriter13 = new Typewriter(null, {
    loop: false,
    delay: 75,
    onCreateTextNode: customNodeCreator,
    onRemoveNode: onRemoveNode,
  });
  
  typewriter13
    .typeString('Username')
    .pauseFor(300)
    .start();