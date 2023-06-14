#!/usr/bin/node

/*
 * a script that prints 'x' times “C is fun”, where 'x' is first cmd argument pass to the script
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
