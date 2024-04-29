#!/usr/bin/node

exports.addMeMaybe = function (n, newFunction) {
  newFunction.call(this, n + 1);
};
