#!/usr/bin/node
// A scrit that prints the value of the first argument passed

const argument = process.argv[2];

if (argument) {
  console.log(argument);
} else {
  console.log('No argument');
}

