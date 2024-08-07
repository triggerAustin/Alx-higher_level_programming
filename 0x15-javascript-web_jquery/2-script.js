/*
 update text color to red when 
 another element is clicked
 */
const clickableElement = $('#red_header');
const headerElement = $('header');

clickableElement.addEventListener('click', (ev) =>{
	headerElement.css('color', '#FF0000');
});
