#!/usr/bin/node
const args = process.argv;
if(!Number.isInteger(parseFloat(args[2]))){
	console.log("Not a number");
	return;
}
console.log(parseInt(args[2]));
