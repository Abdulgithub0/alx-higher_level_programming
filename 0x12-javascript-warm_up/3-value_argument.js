#!/usr/bin/node

/*
 * a script that prints its first argument pass to it.
 */
if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
