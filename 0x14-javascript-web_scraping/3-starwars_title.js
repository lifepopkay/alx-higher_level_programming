#!/usr/bin/node
// get start war titlee

const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Define the URL with the provided movie ID
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make the request to the Star Wars API
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
	  return;
  }
  const data = JSON.parse(body);
  console.log(`${data.title}`);
});
