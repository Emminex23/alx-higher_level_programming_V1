#!/usr/bin/node

const fs = require('fs');

// Read the contents of the file that contains myVar
const filePath = './100-main.js';
const fileContent = fs.readFileSync(filePath, 'utf-8');

// Replace the value of myVar with 333
const newContent = fileContent.replace(/myVar\s*=\s*.*/, 'myVar = 333');

// Write the modified contents back to the file
fs.writeFileSync(filePath, newContent);
