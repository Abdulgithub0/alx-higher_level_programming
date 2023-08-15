#!/usr/bin/node

/**
 *  a function that returns the number of occurrences in a list
 */

exports.nbOccurences = function (list, searchElement) {
  let occurence = 0;
  for (let i = 0; i < list.length; i++) {
    occurence += list[i] === searchElement ? 1 : 0;
  }
  return (occurence);
};
