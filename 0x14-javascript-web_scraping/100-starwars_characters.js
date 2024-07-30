#!/usr/bin/node
/*
  script that prints all characters of a Star Wars movie:
  first argument is the Movie ID
  Display one character name by line
  use the Star wars API
  use the module request
 */
const movieId = process.argv.slice(2)[0];
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, { json: true }, (error, response, body) => {
  if (!error) {
    body.characters.forEach(chr => {
      request.get(chr, { json: true }, (error, res, body1) => {
        if (error) {
          console.log(error);
        }
        console.log(body1.name);
      });
    });
  }
});
