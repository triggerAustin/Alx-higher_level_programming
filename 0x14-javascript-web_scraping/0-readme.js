#!/usr/bin/node
/*
 reads a file
 outputs it's content / errors
 */
const fs = require('fs');
const filePath = process.argv.slice(2)[0]

fs.readFile (filePath, 'utf8', (error, data) => {
	if (error) {
		console.log(error);
	}
	else{
		console.log(data);
	}
});
