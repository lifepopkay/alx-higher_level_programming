#!/usr/bin/node
// Display the status code of a
// get request

// fetch the url for the command
const url = process.argv[2];

// Pass command into the request module
const request = require('request');

request(url, function(err, response) {
  if (err) {
    console.error(err);
    return;
  }
  console.log(`code:, ${response.statusCode}`);
});
