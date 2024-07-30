#!/usr/bin/node

const fs = require('fs');
const path = require('path');
const filePath = path.resolve(process.argv[2]);

fs.readFile(filePath, 'utf8', (err, data) => {
	if (err) {
		console.log(err);
	}
	else{
		console.log(data);
	}
});
