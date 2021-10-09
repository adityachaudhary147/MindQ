
var form_fields = document.getElementsByTagName('input')
form_fields[1].placeholder = 'Username';
form_fields[2].placeholder = 'First name';
form_fields[3].placeholder = 'Last name';
form_fields[4].placeholder = 'Your Email';
form_fields[5].placeholder = 'Password';
form_fields[6].placeholder = 'Re-type Password';

for (var field in form_fields) {
    form_fields[field].className += ' shadow mt-3'
}

const form = document.getElementById("userForm");

form.addEventListener("submit", function (e) {
    e.preventDefault();

    const format = /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{7,15}$/;
    const a = document.getElementById("id_password1").value;
    const b = document.getElementById("id_password2").value;
    const userFirstName = document.getElementById("id_first_name").value;
    const userLastName = document.getElementById("id_last_name").value;
    const userName = document.getElementById("id_username").value;


    if (a.match(format)) {
        let uFNToLower = userFirstName.toLowerCase();
        let uLNToLower = userLastName.toLowerCase();
        let uNToLower = userName.toLowerCase();
        let aToLower = a.toLowerCase();
        if (aToLower.includes(uFNToLower) || aToLower.includes(uLNToLower) || uNToLower.includes(aToLower)) {
            if (document.contains(document.getElementById("errorMsg2"))) {
                document.getElementById("errorMsg2").remove();
            }
            let pwd1 = document.getElementById("id_password1");
            pwd1.insertAdjacentHTML('afterend',
                `<small class="text-danger my-0 py-0" id="errorMsg2">Your password must not similar with the other personal information</small>`
            )
        }
        else {
            if (a === b) {
                form.submit();
            }
            else {
                if (document.contains(document.getElementById("errorMsg"))) {
                    document.getElementById("errorMsg").remove();
                }
                let pwd2 = document.getElementById("id_password2");
                pwd2.insertAdjacentHTML('afterend',
                    `<small class="text-danger my-0 py-0" id="errorMsg">Password didn't match</small>`
                )
            }
        }


    }
    else {
        if (document.contains(document.getElementById("errorMsg"))) {
            document.getElementById("errorMsg").remove();
        }
        let pwd1 = document.getElementById("id_password1");
        pwd1.insertAdjacentHTML('afterend',
            `<small class="text-danger my-0 py-0" id="errorMsg">Your password must contain atleast one digit or one special character</small>`
        )
    }

})
