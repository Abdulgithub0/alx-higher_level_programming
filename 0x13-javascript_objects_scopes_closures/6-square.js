#!/usr/bin/node

/**
 * Class square Inherit from class Rectangle and mimic a square shape physical object.
 */
const square = require('./5-square');
class Square extends square {
  constructor (size) {
    super(size, size);
  }

  // print out the rectangle shape using char 'C' or 'X' if parameter is undefined.
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.width));
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
