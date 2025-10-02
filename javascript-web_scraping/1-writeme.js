#!/usr/bin/node

const fs = require('fs');
const args = process.argv.slice(2);

const filename = args[0];
const text = args[1];

fs.writeFile(filename, text, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
