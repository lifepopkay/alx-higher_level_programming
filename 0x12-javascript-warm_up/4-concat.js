#!/usr/bin/node

// print two arguments passed

const { argv } = require('node:process');

if (argv[2] === undefined && argv[3] === undefined) {
	console.log(argv[2] + ' is ' + argv[3]);
} else {
	console.log(argv[2] + ' is ' + argv[3]);
}
