#!/usr/bin/node

exports.addMeMaybe = function (number, theFunction) {
  const newNum = number + 1;
  theFunction(newNum);
};
