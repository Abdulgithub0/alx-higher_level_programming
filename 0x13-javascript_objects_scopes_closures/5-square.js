#!/usr/bin/node

/**
 * Class square Inherit from class Rectangle and mimic a square shape physical object.
 */
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }
}
module.exports = Square;
