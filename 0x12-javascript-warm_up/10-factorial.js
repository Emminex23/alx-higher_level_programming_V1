#!/usr/bin/node

const process = require('process');
const args = process.argv;
const x = parseInt(args[2]);

function factorial (n) {
  if (n >= 1) {
    return n * factorial(n - 1);
  } else {
    return 1;
  }
}

console.log(factorial(x));
