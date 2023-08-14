#!/usr/bin/node

const you = require('node:process').argv;
const num = you[2];
// console.log(factorial(num));
function factorial (num) {
  if (num === 1 || isNaN(num) || num === 0) {
    return 1;
  }
  return (num * (factorial(num - 1)));
}
secondBiggest(you.slice(2, you.length));
function secondBiggest (arr) {
  // arr.map(parseInt);
  arr.sort((a, b) => a - b);
  console.log(arr[arr.length - 2]);
}
