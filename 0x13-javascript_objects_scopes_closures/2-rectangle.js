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
}
module.exports = Rectangle;
