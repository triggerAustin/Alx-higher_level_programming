#!/usr/bin/node
/*
 script that gets the contents of a webpage and stores it in a file.
 first argument is the URL to request
 second argument the file path to store the body response
 file must be UTF-8 encoded
 use the module request
 */

const args = process.argv.slice(2);
const request = require('request');
const fs = require('fs');
const url = args[0];
const filename = args[1];

request(url, { json: true }, (error, response, body) => {
  if (!error) {
    fs.writeFile(filename, body, 'utf8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
