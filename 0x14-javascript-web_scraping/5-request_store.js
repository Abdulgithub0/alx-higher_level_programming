#!/usr/bin/node

/*
 * a script that prints the title of a Star Wars movie where the
 * episode number matches a given integer.
 */

const req = require('request');
const fs = require('fs');

if (process.argv.length >= 4) {
  const url = process.argv[2];
  const filename = process.argv[3];
  req.get(url, (err, resp, body) => {
    fs.writeFile(filename, body, 'utf-8', (error) => { });
  });
}
