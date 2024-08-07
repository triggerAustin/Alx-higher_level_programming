/*
 adds a <li> element to a list 
 when the user clicks on the tag DIV#add_item:
 */
const myList = $('ul.my_list');
const addItem = $('#add_item');

addItem.addEventListener('click', (ev) => {
	myList.append('<li>Item</li>');
})
