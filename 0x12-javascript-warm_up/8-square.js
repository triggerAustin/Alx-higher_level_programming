#!/usr/bin/node

const args = process.argv;

if(!parseInt(args[2])){
	console.log("Missing size")
}
let x = parseInt(args[2]);
let i, j;

for(i = 0; i < x; i++){
	console.log("X".repeat(x));
}
