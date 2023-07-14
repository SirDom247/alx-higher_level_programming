#!/usr/bin/node
const argsLength = process.argv.length - 2;
let messsage;
if (argsLength === 0) {
	message = "No argumebt";
} else if (argsLength === 1) {
	message = "Argument found";
} else {
	message = "Arguments found";
}
