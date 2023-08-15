#!/usr/bin/node
const Square = require('.././sraw.js');

const s1 = new Square(4);
s1.print();
s1.double();
s1.print();
console.log(Object.getPrototypeOf(s1));
