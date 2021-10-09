

var myFunc = function () {
    // $('#title1').toggle(700);
    // $('#title2').toggle(700);
    // $('#title3').toggle(700);
    // $('#title4').toggle(700);
    // $('#title5').toggle(700);
    // $('#title6').toggle(700);
    
}
window.onload = function () {
    setTimeout(myFunc, 300);
}


$('#link1').hover(function () {
    $('#title1').toggle(700);
});
$('#link2').hover(function () {
    $('#title2').toggle(700);
});
$('#link3').hover(function () {
    $('#title3').toggle(700);
});
$('#link4').hover(function () {
    $('#title4').toggle(700);
});
$('#link5').hover(function () {
    $('#title5').toggle(700);
});
$('#link6').hover(function () {
    $('#title6').toggle(1000);
});


