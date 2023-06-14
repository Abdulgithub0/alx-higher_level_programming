#!/usr/bin/node

/*
 * a script that prints the addition of 2 integers
 */
const arg1 = +(process.argv[2]);
const arg2 = parseInt(process.argv[3]);
add(arg1, arg2);
function add (a, b) {
  if (isNaN(a) && isNaN(b)) {
    console.log('NaN');
  } else {
    console.log('%d', a + b);
  }
}
