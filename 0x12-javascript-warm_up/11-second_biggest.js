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
    max = +(list[2]);
    max2 = 0;
    for (let i = 3; i < list.length; i++) {
      element = +(list[i]);
      if (max < element) {
        max2 = max;
        max = element;
      } else if (element !== max && element > max2) {
        max2 = element;
      }
    }
    console.log(max2);
  }
}
