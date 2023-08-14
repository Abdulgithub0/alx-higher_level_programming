#!/usr/bin/node

/*
 * a script that prints 'x' times “C is fun”, where 'x' is first cmd argument pass to the script
 */
const len = +(process.argv[2]);
if (isNaN(len)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < len) {
    console.log('C is fun');
    i++;
  }
}
