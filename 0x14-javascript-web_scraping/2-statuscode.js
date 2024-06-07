#!/usr/bin/node
// Display the status code of a
// get request

// fetch the url for the command
const Url = process.argv[2];

const { url } = require('inspector');
// Pass command into the request module
const request = require('request');

request(url, function(err, response, body) {
    if (err) {
        console.error('code:', response.statusCode);
        return;
    }
    console.log('code:', response.statusCode);
});