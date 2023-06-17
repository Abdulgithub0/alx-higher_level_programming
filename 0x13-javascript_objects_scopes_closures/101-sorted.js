#!/usr/bin/node

/**
 * a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
 */
const dict = require('./101-data').dict;
const newDict = {};
let temp = '';
for (const key in dict) {
  temp = String(dict[key]);
  if (newDict[temp] == null) {
    newDict[temp] = [];
  }
  newDict[temp].push(parseInt(key));
}
console.log(newDict);
