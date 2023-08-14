#!/usr/bin/node

const you = require('node:process').argv;
// if (you.length >= 3) {
const arr = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
for (let i = 0; i < 3; i++) {
  console.log(arr[i]);
}
