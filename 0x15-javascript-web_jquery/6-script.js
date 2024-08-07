/*
 updates the text of the <header>
 to New Header!!! when the user clicks on DIV#update_header
 */
const headerElement = $('header');
const updateHeader = $('#update_header');

updateHeader.addEventListener('click', (ev) => {
	headerElement.text('New Header!!!');
})
