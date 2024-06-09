#!/usr/bin/node
// Prints the number of movies where
// the character "wedge Antiles" is present

const request = require('request');
const url = process.argv[2];
let count = 0;

// Make request to the url
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const data = JSON.parse(body).results;

  // iterate through the json result
  for (let i = 0; i < data.length; i++) {
    const character = data[i].characters;
    // iterate through the character
    for (let j = 0; j < character.length; j++) {
      if (character[j].search('18') > 0) {
        count++;
      }
    }
  } 
  console.log(count);
});
