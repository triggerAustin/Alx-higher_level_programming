/*
 set class name to header
 on click of diff element
 */
const clickableElement = $('#red_header');
const headerElement = $('header');

clickableElement.addEventListener('click', (ev) => {
	headerElement.addClass('red');
});
