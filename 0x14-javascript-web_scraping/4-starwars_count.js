#!/usr/bin/node
// Prints the number of movies where
// the character "wedge Antiles" is present

const request = require('request');
const url = process.argv[2]
const wedgeAntillesId = 18;
const new_url = url + '/' + wedgeAntillesId

// MAke request to the url
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const data = JSON.parse(body).results;
  const chara_list = []

  for (let i = 0; i < data.length; i++) {
    const character = data[i].charaters;
    for (let j = 0; j < character.length; j++) {
      chara_list[j] = character[j].find('18');
    }
  } 
  console.log(chara_list);
});
