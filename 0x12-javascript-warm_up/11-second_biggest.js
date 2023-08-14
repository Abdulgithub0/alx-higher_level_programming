#!/usr/bin/node

/*
 * a a script that searches the second biggest integer in the list of arguments.
 */
const array = process.argv;
secondMax(array);
function secondMax (list) {
  if (array.length === 2) {
    console.log('%d', 0);
  } else if (array.length === 3) {
    console.log('%d', 0);
  } else {
    console.log(secondBiggest(array.slice(2)));
  }
}
function secondBiggest (arr) {
  arr.map(parseInt);
  arr.sort((a, b) => a - b);
  return arr[arr.length - 2];
}
