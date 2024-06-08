#!/usr/bin/node
// Reads and prinst the content of a file
// call the filestream
const fs = require('fs');

// get the file path from the first argument
const text = process.argv[2];

fs.readFile(text, 'utf8', (err, data) => {
  if (err) {
  // Print error if an error occured
    console.error(err);
    return;
  }
  // print the content of the file
  console.log(data);
});
