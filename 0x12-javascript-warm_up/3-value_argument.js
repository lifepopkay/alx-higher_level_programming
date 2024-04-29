#!/usr/bin/node

// Prints the first argument passed

const { argv } = require('node:process');

if (argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
