#!/usr/bin/node

/**
 * Class Rectangle represent a protolytic object for Rectangle shape
 */

class Rectangle {
  /* adding properties */
  constructor (w, h) {
    if (w >= 1 && h >= 1) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
