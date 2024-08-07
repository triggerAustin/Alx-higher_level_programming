/*
toggles the class of the <header>
when the user clicks on the tag DIV#toggle_header
 */
const headerElement = $('header');
const clickableElement = $('#toggle_header');

clickableElement.addEventListener('click', (ev) => {
	if (!headerElement.hasClass('red')){
		headerElement.removeClass('red');
		headerElement.addClass('green');
	}
	else if (headerElement.hasClass('green')){
		headerElement.removeClass('green');
		headerElement.addClass('red');
	}
});
