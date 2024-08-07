/*
 fetches and lists the title for all movies by using this URL:
 https://swapi-api.alx-tools.com/api/films/?format=json
 */

const movieList = $('#list_movies');
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json'

$.ajax({
	url: url,
	method: 'GET',
	success: (response) => {
		let results = response.results;

		results.forEach(element => {
			if (element.title){
				movieList.append(`<li>${element.title}<li/>`);
			}
		});
	}
});
