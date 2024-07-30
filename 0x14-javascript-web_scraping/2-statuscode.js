#!/usr/bin/node
/*
 script that display the status code of a GET request
 first argument is the URL to request (GET)
 status code must be printed like this: code: <status code>
 must use the module request
 */
const args = process.argv.slice(2);
const request = require('request');

request(args[0], function (error, response, body) {
  if (response && !error) {
    console.log('code:', response.statusCode);
  }
});
