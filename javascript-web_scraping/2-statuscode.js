#!/usr/bin/node

const args = process.argv.slice(2);

const request = require('request');
const url = args[0];

request(url, (error, response) => {
  if (error) {
    console.log(error);
    return;
  }
  console.log(`code: ${response.statusCode}`);
});
