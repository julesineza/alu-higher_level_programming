#!/usr/bin/node

const args = process.argv.slice(2);

const request = require('request');
const urlrequest = 'https://swapi-api.alx-tools.com/api/films/' + args[0] + '/';

request(urlrequest, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
