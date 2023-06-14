#!/usr/bin/node

/**
 * a function that increments and calls a function.
 */

function addMeMaybe (x, fun) {
  x++;
  fun(x);
}
module.exports = { addMeMaybe };
