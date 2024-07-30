#!/usr/bin/node
/*
prints the number of movies where the character “Wedge Antilles” is present.
first argument is the API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/
Wedge Antilles is character ID 18
script must use this ID for filtering the result of the API
use the module request
*/

const args = process.argv.slice(2);
const request = require('request');
const url = args[0];
const character_id = 18;
const characters = []

request(url, {json : true},  function(error, response, body){
	if (error){
		console.log(error);
	}

	let count = 0;
	let i;

	for (i = 0; i < body.results.length; i++){
		characters.push(body.results[i].characters);
	}

	characters.forEach(chr => {
		chr.forEach(ch => {
			if(String(ch).endsWith(`${character_id}/`)){
				count++;
			}
		});
	});
console.log(count);
});
