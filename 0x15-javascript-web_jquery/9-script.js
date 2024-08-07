/*
fetches from https://hellosalut.stefanbohacek.dev/?lang=fr 
displays the value of hello from that fetch in the HTML tag DIV#hello
*/
const divHello = $('#hello');
const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr '

$.ajax({
    url: url,
    method: 'GET',
    success: (response) => {
        divHello.text(response.hello)
    }
})