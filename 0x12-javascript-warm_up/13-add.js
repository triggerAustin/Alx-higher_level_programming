#!/usr/bin/node

const args = process.argv;

let x = args[1];
let y = args[2];

export function add(a, b){
	return(a + b);
}

add(x, y);
