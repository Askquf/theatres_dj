window.onload = function(){

    buttons = document.querySelectorAll('[class = "info_button"]')
    buttons.forEach(button => {
        button.onclick = function() {
            window.location.href = 'theatre/' + button.name
        }
    })
};
