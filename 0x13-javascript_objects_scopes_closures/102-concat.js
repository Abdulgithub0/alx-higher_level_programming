#!/usr/bin/node

/*
 * a script that concats 2 files.
 */

const fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', (error, cont1) => {
  if (error) return;
  fs.readFile(process.argv[3], 'utf-8', (err, cont2) => {
    if (err) return;
    fs.writeFile(process.argv[4], cont1 + cont2, (err3) => { if (err3); });
  });
});
