#!/usr/bin/node

const process = require('process');
const args = process.argv;
const x = parseInt(args[2]);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  let message = '';
  for (let i = 0; i < x; i++) {
    message += 'C is fun\n';
  }
  console.log(message.trim());
}
