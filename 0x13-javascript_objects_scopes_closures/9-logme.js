#!/usr/bin/node

/**
 *  a function that prints the number of arguments already printed and the new argument value. (see example below)
 */
exports.logMeCounter = 0;
exports.logMe = function (item) {
  console.log(`${exports.logMeCounter}: ${item}`);
  exports.logMeCounter++;
};
