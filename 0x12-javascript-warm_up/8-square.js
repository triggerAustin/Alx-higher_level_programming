#!/usr/bin/node

const args = process.argv;

if(!parseInt(args[2])){
	console.log("Missing size")
}
int x = parseInt(args[2]);
int i, j;

for(i = 0; i < x; i++){
	for(j = 0; j < x; j++){
		console.log("X");
	}
}
