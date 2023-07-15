#!/usr/bin/node
// A script that concatenates the values of two arguments passed to it.

const myArgs = process.argv.slice(2);
if (!myArgs[0]) {
	console.log('undefined is undefined');
}
else {
	console.log(myArgs[0], 'is', myArgs[1]);
}
