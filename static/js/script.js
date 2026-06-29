console.log("AI Resume Analyzer Loaded");

function validateLogin(){

let email=document.querySelector("input[type=email]").value;

let pass=document.querySelector("input[type=password]").value;

if(email==""||pass==""){

alert("Please fill all fields");

return false;

}

return true;

}

function uploadSuccess(){

alert("Resume Uploaded Successfully");

}