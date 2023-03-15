#!/usr/bin/node

const process = require('process');
const x = process.argv.slice(2).map(arg => parseInt(arg));

if (x < 2) {
  console.log(0);
} else {
  let maxNum = x[0];
  let secondMax = -Infinity;

  for (let i = 0; i < x.length; i++) {
    if (x[i] > maxNum) {
      secondMax = maxNum;
      maxNum = x[i];
    } else if (x[i] > secondMax && x[i] < maxNum) {
      secondMax = x[i];
    }
  }
  console.log(secondMax === -Infinity ? 0 : secondMax);
}
