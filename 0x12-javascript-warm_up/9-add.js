#!/usr/bin/node

const process = require('process');
const args = process.argv;

function add (a, b) {
  return (a + b);
}

const num1 = parseInt(args[2]);
const num2 = parseInt(args[3]);

console.log(add(num1, num2));
