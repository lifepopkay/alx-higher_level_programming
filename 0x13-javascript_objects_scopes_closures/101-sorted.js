#!/usr/bin/node

// import dict of user id and compute by occurence

const dict = require('./101-data').dict;

const newDict = {};
for (const uId in dict) {
  const occurences = dict[uId];
  if (occurences in newDict) {
    newDict[occurences].push(uId);
  } else {
    newDict[occurences] = [uId];
  }
}
console.log(newDict);
