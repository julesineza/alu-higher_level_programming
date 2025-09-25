#!/usr/bin/node

const args = process.argv.slice(2)

a=parseInt(args[0])
b=parseInt(args[1])

function add(a, b) {
    if (!isNaN(a) && ! isNaN(b)){
        console.log(a+b);
    }
    else {
        console.log("NaN")
    }
}

add(a=parseInt(args[0]),b=parseInt(args[1]))