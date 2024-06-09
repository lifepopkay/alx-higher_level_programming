#!/usr/bin/node
// compute the number of tasks completed

const request = require('request');
const Url = process.argv[2];

request(Url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const result = {}
  const data = JSON.parse(body);
  for (let i = 0 < body.length; i++) {
    if (data[i].completed === true) {
        if (result[data[i].userId] === undefined) {
            result[data[i].userId] = 0;
        }
        result[data[i].userId]++;
    }
    console.log(result);
  }
});