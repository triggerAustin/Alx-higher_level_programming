/*
 fetches character name from url
 updates element with name
 */
const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json'
const characterDiv = $('#character');

$.ajax({
	url : url,
	method: 'GET',
	success: (response) => {
		characterDiv.text(response.name);
	}
})
