#!/usr/bin/node

const args = process.argv;

if (!args[2]){
	console.log("No argument");
}

args.forEach((val, index) => {
	if (index == 2){
		console.log(val);
	}
});
