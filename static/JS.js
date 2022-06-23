
var text ="     Want to start your journey with us?"
var chars = text.split('');
var container = document.getElementById("writerH3");
var i = 0;


setInterval(function () {    /* Typewriter function */
    if(document.getElementById("writerH3") != null) { 
        if (i < chars.length) {
            writerH3.innerHTML += chars[i++];
        }
    }
     
}, 80);





function ReplaceImage() { /* replacing images by clicking function*/
    var myImage = document.getElementById('changedImage');
    var mySrc = myImage.getAttribute('src');
    if(mySrc === "../static/teacher1.jpg") {
        myImage.setAttribute('src',"../static/teacher2.jpg");
     } else if(mySrc === "../static/teacher2.jpg") {
        myImage.setAttribute('src',"../static/teacher3.jpg");
     }
     else {
        myImage.setAttribute('src',"../static/teacher1.jpg");
     }
}
window.onload = setActive;



function setActive() { /* marking current page function*/
    aObj = document.getElementById('navbar').getElementsByTagName('a');
    for(i=0;i<aObj.length;i++) {
      if(document.location.href.indexOf(aObj[i].href)>=0) {
        aObj[i].className='active';
      }
    }
  }



