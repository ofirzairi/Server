
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

  // $("frontend").submit();

  function userID() {
    const formInput = document.getElementById("frontend").user_id.value;
    console.log(formInput)
    fetch(`https://reqres.in/api/users/${formInput}`)
        .then((response) => response.json())
        .then((object) => {
            const data = object?.data;
            document.getElementById("Response_BE").innerHTML = `<div></div>`;
            document.getElementById("Response_FE").innerHTML =
                `
                    <br>
                    <h3>${data?.first_name} ${data?.lastname}</h3>
                    <h3>${data?.email}</h3>
                    <img src="${data?.avatar}" alt="Profile Picture"/>
                `
        })
        .catch((err) => console.log(err));
}


