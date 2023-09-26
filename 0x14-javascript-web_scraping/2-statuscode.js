#!/usr/bin/node

/*
 * a script that display the status code of a GET request
 */

const req = require('request');

if (process.argv.length >= 3) {
  const url = process.argv[2];
  req.get(url, (err, resp) => {
    if (!err) { console.log(`code: ${resp.statusCode}`); }
  });
}
