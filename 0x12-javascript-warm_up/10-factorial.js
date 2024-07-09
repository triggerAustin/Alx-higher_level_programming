#!/usr/bin/node

const args = process.argv;

if(!(args[1]) || args[1] == 1){
	console.log("NaN");
	return;
}

function factorial(x){
	if (x > 1){
		factorial(x-1);
	}

	return(x * x-1);
}
