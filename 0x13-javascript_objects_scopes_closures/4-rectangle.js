#!/usr/bin/node

/**
 * Class Rectangle represent a protolytic object for Rectangle shape
 */

class Rectangle {
  /* adding properties */
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      /* created an empty rectangle object */
    } else {
      this.width = w;
      this.height = h;
    }
  }

  // perform stdout functionality to the Rectangle object.
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  // perform rotation on the Rectangle object.
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // double the value of width and height property of the Rectangle object.
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
