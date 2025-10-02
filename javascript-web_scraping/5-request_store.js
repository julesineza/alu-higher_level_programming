#!/usr/bin/node 

const args = process.argv.slice(2)
const fs = require("fs");
const request = require('request')
const url = args[0]
const filename = args[1]

request(url,(error,Response,body) => {
    if (error) {
        console.log(error)
    }

    fs.writeFile(filename,body,'utf-8',(err) => {
        if (err) {
            console.log(err)
            return
        }
    })
})