
$(document).ready(function(){
    $("#writeAbtn").click(function(){
        $("#replyBox").toggle(300)
    })
})

const element = document.querySelectorAll(".textEditorBtn");

element.forEach(element => {
    element.addEventListener('click', () => {
        let command = element.dataset['element'];
        document.execCommand(command, false, null);
    })
})
