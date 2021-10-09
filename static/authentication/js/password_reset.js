var form_fields = document.getElementsByTagName('input')
form_fields[1].placeholder = 'Your Email';


for (var field in form_fields) {
    form_fields[field].className += ' shadow py-2 px-4'
}