#!/usr/bin/node

/**
 *  script that imports an array and computes a new array by multiply each element by it index.
 */
const list = require('./100-data').list;
const newList = list.map((e, i) => e * i);
console.log(list);
console.log(newList);
