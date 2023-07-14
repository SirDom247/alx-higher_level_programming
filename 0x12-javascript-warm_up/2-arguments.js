#!/usr/bin/node
const argsLength = process.argv.length - 2;

if (argsLength === null) {
  console.log("No argument");
} else if (argsLength === 1) {
  console.log("Argument found");
} else {
  console.log("Arguments found");
}

