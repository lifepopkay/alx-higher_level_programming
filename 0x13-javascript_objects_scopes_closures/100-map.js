#!/usr/bin/node

// import and compute new array

const compt = require('./100-data').list;

console.log(compt);

const newArray = compt.map((num, index) => num * index);

console.log(newArray);
