$('#categoryBtn').click(function () {
    $('#phoneCategoryBox').toggle(500);
    $('#phoneTagBox').hide(500);
})
$('#tagBtn').click(function () {
    $('#phoneTagBox').toggle(500);
    $('#phoneCategoryBox').hide(500);
})

$('#cancelAnswere').click(function () {
    $('#replyBox').remove();
})


const element = document.querySelectorAll(".textEditorBtn");

element.forEach(element => {
    element.addEventListener('click', () => {
        let command = element.dataset['element'];
        document.execCommand(command, false, null);
    })
})

function myFunction(id) {
    $("." + "replyBox" + id).toggle(400)
}

// for asking the question 
$("#submitButton").click(function (e) {
    console.log("hello");
    e.preventDefault(); // avoid to execute the actual submit of the form.
    var description = $('#addTopicTextarea').val();
    var title = $('#askQuestionInput').val();
    var urlt = $('#addUrlInput').val();

    $.ajax(
        {
            type: "POST",
            url: "{% url 'create-question' %}",
            data: { 'csrfmiddlewaretoken': '{{ csrf_token }}', 'description': description, 'title': title, 'url': urlt }, // serializes the form's elements.
            dataType: 'json',
            success: function () {
                console.log("submitted");
                $('#create-answer')[0].reset();
                $('#submitspan').append(" <span class='label label-important' style='color:green'> Sucess Done </span>");
                // show response from the php script.
            }
        });


});