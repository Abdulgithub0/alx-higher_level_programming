#!/usr/bin/node

/*
 * a script that prints a square
 */
const len = +(process.argv[2]);
if (isNaN(len)) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < len) {
    for (let j = 0; j < len; j++) {
      process.stdout.write('X');
    }
    console.log();
    i++;
  }
}
