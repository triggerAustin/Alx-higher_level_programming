#!/usr/bin/node
const args = process.argv;
let i = 0;
let j;
if (!Number.isInteger(parseInt(args[2]))){
	console.log("Missing number of occurrences");
	return;
}
j = args[2];
while (i < j){
	console.log("C is fun");
	i++;
}
