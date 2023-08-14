#!/usr/bin/node

/*
 * a script that computes and prints a factorial
 */
const arg = +(process.argv[2]);
console.log(factorial(arg));
function factorial (num) {
  if (isNaN(num)) {
    return (1);
  } else {
    if (num === 1 || num === 0) {
      return (1);
    }
    return (num * factorial(num - 1));
  }
}
