#!/usr/bin/node

/*
 * a script that prints the title of a Star Wars movie where the
 * episode number matches a given integer.
 */

const req = require('request');

if (process.argv.length >= 3) {
  const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
  req.get(url, (err, resp, body) => {
    const obj = JSON.parse(body);
    if (!err) { console.log(obj.title); }
  });
}
