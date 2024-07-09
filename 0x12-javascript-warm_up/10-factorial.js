#!/usr/bin/node

const args = process.argv;

if(!(args[2]) || args[2] == 1){
	console.log("NaN");
	return;
}

function factorial(x){
	if (isNaN(x) || x <= 0){
		return 1;
	}
	else if(x === 1){
		return 1;
	}
	else{

		return x * factorial(x-1);
	}
}
console.log(factorial(+args[2]));
