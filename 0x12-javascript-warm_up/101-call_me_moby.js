#!/usr/bin/node

/**
 * a function that executes x times a function.
 */

function callMeMoby (x, fun) {
  let i = 0;
  while (i < x) {
    fun();
    i++;
  }
}
module.exports = { callMeMoby };
