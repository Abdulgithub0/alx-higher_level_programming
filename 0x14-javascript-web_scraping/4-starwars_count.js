#!/usr/bin/node

/*
 * a script that prints the title of a Star Wars movie where the
 * episode number matches a given integer.
 */

const req = require('request');

if (process.argv.length >= 3) {
  const url = process.argv[2];
  req.get(url, (err, resp, body) => {
    if (!err) {
      const obj = JSON.parse(body);
      let cha = 0;
      for (let i = 0; i < obj.results.length; i++) {
        for (let j = 0; j < obj.results[i].characters.length; j++) {
	  if (obj.results[i].characters[j].endsWith('18/')) cha++;
        }
      }
      console.log(cha);
    }
  });
}
