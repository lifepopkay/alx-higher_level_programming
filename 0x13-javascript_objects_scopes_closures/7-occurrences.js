#!/usr/bin/node
// count the occurences of elements

exports.nbOccurences = function (list, searchElement) {
  
  let numOcc = 0;
  let i = 0;
  while (i < list.length) {
    if (searchElement === list[i]) {
      numOcc++;
      i++;
  }
  return numOcc;
}
