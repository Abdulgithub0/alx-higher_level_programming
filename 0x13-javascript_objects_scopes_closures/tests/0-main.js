#!/usr/bin/node
const Rectangle = require('.././0-rectangle');

const r1 = new Rectangle();
console.log(r1);
console.log(r1.constructor);
console.log(r1.prototype);
console.log(Object.getPrototypeOf(new Rectangle()));
console.log(Object.getPrototypeOf(r1));
