var email = document.getElementById("id_username");
    email.removeAttribute("required");
    email.classList.add("w-full");
    email.classList.add("px-4");
    email.classList.add("py-3");
    email.classList.add("rounded-lg");
    email.classList.add("bg-gray-200");
    email.classList.add("mt-2");
    email.classList.add("border");
    email.classList.add("focus:border-gray-500");
    email.classList.add("focus:bg-white");
    email.classList.add("focus:outline-none");
    email.placeholder = "Enter Email Adress";


var password = document.getElementById("id_password");
    password.removeAttribute("required");
    password.classList.add("w-full");
    password.classList.add("px-4");
    password.classList.add("py-3");
    password.classList.add("rounded-lg");
    password.classList.add("bg-gray-200");
    password.classList.add("mt-2");
    password.classList.add("border");
    password.classList.add("focus:border-gray-500");
    password.classList.add("focus:bg-white");
    password.classList.add("focus:outline-none");
    password.placeholder = "Enter Password";