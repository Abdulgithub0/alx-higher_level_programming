#!/usr/bin/node

/*
 * a a script that searches the second biggest integer in the list of arguments.
 */
const array = process.argv;
let max, max2, element;
secondMax(array);
function secondMax (list) {
  if (list[2] === undefined) {
    console.log('%d', 0);
  } else if (list.length === 3) {
    console.log('%d', 1);
  } else {
    console.log(secondBiggest(array.slice(2)));
  }
}
function secondBiggest (arr) {
  arr.map(parseInt);
  arr.sort((a, b) => a - b);
  return arr[arr.length - 2];
}
