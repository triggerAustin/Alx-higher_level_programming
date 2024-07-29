#!/usr/bin/node
const args = process.argv;
if(!args[2] || !args[3]){
	console.log("NaN");
	return;
}
function add(a, b){
	console.log(a + b);
}
add(+args[2], +args[3]);
