var form_fields = document.getElementsByTagName('input')
form_fields[1].placeholder = 'Enter new password';
form_fields[2].placeholder = 'Re-enter new password';


for (var field in form_fields) {
    form_fields[field].className += ' shadow py-2 px-4'
}
