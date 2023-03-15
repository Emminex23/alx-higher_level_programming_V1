#!/usr/bin/node

const process = require('process');
const args = process.argv;
const i = parseInt(args[2]);

if (isNaN(i)) {
  console.log('Missing size');
} else {
  for (let x = 1; x <= i; x++) {
    let row = '';
    for (let y = 1; y <= i; y++) {
      row += 'X';
    }
    console.log(row);
  }
}
