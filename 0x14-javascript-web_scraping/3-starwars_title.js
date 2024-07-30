#!/usr/bin/node
/*
 script that prints the title of a Star Wars movie where the episode number matches a given integer
 first argument is the movie ID
 You must use the Star wars API with the endpoint https://swapi-api.alx-tools.com/api/films/:id
 you must use the module request
 */
const args = process.argv.slice(2);
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + args[0];

request(url, { json: true }, function (error, response, body) {
  if (!error && response) {
    console.log(body.title);
  }
});
