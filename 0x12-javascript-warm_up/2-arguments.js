#!/usr/bin/node
const argsLength = process.argv.length;

if (argsLength === 0) {
  console.log("No argument");
} else if (argsLength === 1) {
  console.log("Argument found");
} else {
  console.log("Arguments found");
}
