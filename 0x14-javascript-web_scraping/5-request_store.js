#!/usr/bin/node
// Get the contents of a webpage
// and stores in a file

const request = require('request');
const Url = process.argv[2];
const file = process.argv[3];
const fs = require('fs');


request(Url, 'utf-8', (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  fs.writeFileSync(file, body);
});