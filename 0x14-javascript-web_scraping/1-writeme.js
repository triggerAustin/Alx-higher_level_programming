#!/usr/bin/node
/*
 script that writes a string to a file.
 first argument is the file path
 second argument is the string to write
 content of the file must be written in utf-8
 print the error object if error occurs
 */

const args = process.argv.slice(2);
const fs = require('fs');

fs.writeFile(args[0], args[1], 'utf8', (error) => {
  if (error) {
    console.log(error);
  }
});
