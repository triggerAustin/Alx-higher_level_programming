#!/usr/bin/node

const args = process.argv;

if(!args[1] || !args[2]){
	console.log("NaN");
	return;
}

function add(a, b){
	console.log(a + b);
}

add(args[1], args[2]);
