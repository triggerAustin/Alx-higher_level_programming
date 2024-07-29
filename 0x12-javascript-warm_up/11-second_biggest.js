#!/usr/bin/node
const args = process.argv;
let arr = [args[1]...];
int i, min = 0;
for(i = 0; i < arr.length; i++){
	if(arr[i] < min){
		min = arr[i];
	}
	i++;
}
console.log(min);
