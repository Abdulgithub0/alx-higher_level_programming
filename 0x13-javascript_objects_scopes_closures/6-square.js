#!/usr/bin/node

/**
 * Class square Inherit from class Rectangle and mimic a square shape physical object.
 */
const Square = require('./5-square');
class Square extends Square {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  // print out the rectangle shape using char 'C' or 'X' if parameter is undefined.
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.size; i++) {
        console.log(c.repeat(this.size));
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
