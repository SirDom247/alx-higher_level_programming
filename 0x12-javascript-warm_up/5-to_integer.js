#!/usr/bin/node
// A script to output  My number: <first argument converted in integer> if the first argument can be converted to an integer: If the argument can’t be converted to an integer, print “Not a number”

const argument = process.argv[2];

const parsedNumber = parseInt(argument);

if (!isNaN(parsedNumber)) {
  console.log(`My number: ${parsedNumber}`);
} else {
  console.log("Not a number";
