#!/usr/bin/node

/*
 * a script that prints a message depending on the number of arguments passed
 */
const argLen = process.argv.length;
if (argLen === 3) {
  console.log('Argument found');
} else if (argLen > 3) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
