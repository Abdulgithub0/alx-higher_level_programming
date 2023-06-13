#!/usr/bin/node

/*
 * a script that prints a message depending of the number of arguments passed
 */
const argLen = require('node:process').argv.length; 
if (argLen === 2)
{
	console.log('Argument found');
}
else if (argLen > 2)
{
	console.log('Arguments found');
}
else
{
	console.log('No argument');
}
