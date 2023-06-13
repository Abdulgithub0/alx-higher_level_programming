#!/usr/bin/node

/*
 * a script that prints and type cast its first argument into int if possible.
 */
const num = parseInt(process.argv[2]);
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: %d', num);
}
