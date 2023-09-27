#!/usr/bin/node

/*
 * a script that prints the title of a Star Wars movie where the
 * episode number matches a given integer.
 */

const req = require('request');

if (process.argv.length >= 3) {
  const url = process.argv[2].replace('/films', '/people/18');
  req.get(url, (err, resp, body) => {
    const obj = JSON.parse(body);
    if (!err) { console.log(obj.films.length); }
  });
}
