#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  // Parse JSON response
  const data = JSON.parse(body);
  const films = data.results;

  // Count films where character ID 18 appears
  let count = 0;
  for (const film of films) {
    if (film.characters.some(charUrl => charUrl.includes('/18/'))) {
      count++;
    }
  }

  console.log(count);
});
