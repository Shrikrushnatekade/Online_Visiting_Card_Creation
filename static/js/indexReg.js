const form = document.getElementById('form');
const username = document.getElementById('username');
const email = document.getElementById('email');
const phone = document.getElementById('phone');
const password = document.getElementById('password');
const cpassword = document.getElementById('cpassword');

form.addEventListener('submit', (event) => {
    event.preventDefault();
    validate();
})

const isEmail = (emailVal) => {
    var atSymbol = emailVal.indexOf("@");
    if (atSymbol < 1)
        return false;

    var dot = emailVal.lastIndexOf('.');
    if (dot <= atSymbol + 3)
        return false;
    return true;
}

const validate = () => {
    const form = form.value.trim();
    const usernameVal = username.value.trim();
    const emailVal = email.value.trim();
    const phoneVal = phone.value.trim();
    const passwordVal = password.value.trim();
    const Val = cpassword.value.trim();


    // validatetion username
    if (usernameVal === "") {
        setErrormsg(username, "UserName cannot be blank");
    }
    else {
        setSuccessMsg(username);
    }

    // validation email
    if (emailVal === "") {
        setErrormsg(email, "Email cannot be blank");
    }
    else if (!isEmail(emailVal)) {
        setErrormsg(emailVal, "Not a valid email");
    }
    else {
        setSuccessMsg(email);
    }
    if (username === "") {
        setErrormsg(username, "UserName cannot be blank");
    }
    else {
        setSuccessMsg(username);
    }
    if (username === "") {
        setErrormsg(username, "UserName cannot be blank");
    }
    else {
        setSuccessMsg(username);
    }
    if (username === "") {
        setErrormsg(username, "UserName cannot be blank");
    }
    else {
        setSuccessMsg(username);
    }
}





function callfun() {
    alert("Your account has been Verified, You can Login")
}
 