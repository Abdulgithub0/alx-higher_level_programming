#!/usr/bin/node

/**
 *  a function that prints the number of arguments already printed and the new argument value. (see example below)
 */

exports.logMe = function (item) {
  if (exports.logMeCounter) {
    console.log(`${exports.logMeCounter}: ${item}`);
    exports.logMeCounter++;
  } else {
    exports.logMeCounter = 0;
    console.log(`${exports.logMeCounter}: ${item}`);
    exports.logMeCounter++;
  }
};
