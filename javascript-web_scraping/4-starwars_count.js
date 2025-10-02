#!/usr/bin/node 


const args = process.argv.slice(2)

const request = require('request')

const url =  "https://swapi-api.alx-tools.com/api/people/18"

request(url,(error,response,body) => {
    if (error) {
        console.log(error)
        return
    }

    data = JSON.parse(body)
    const movies=data.films.length;
    console.log(movies)

})