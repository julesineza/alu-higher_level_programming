#!/usr/bin/node 

const args = process.argv.slice(2)
const request = require('request')
const url = args[0]


request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const todos = JSON.parse(body);
  const users = {};

  for (const todo of todos) {
    if (todo.completed === true) {
      if (users[todo.userId] === undefined) {
        users[todo.userId] = 1;
      } else {
        users[todo.userId] += 1;
      }
    }
  }

  console.log(users);
});