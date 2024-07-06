#!/usr/bin/node

const args = process.argv;

if (!argv[2]){
	console.log("No argument");
}

argv.forEach((val, index) => {
	if (index == 2){
		console.log(val);
	}
}
