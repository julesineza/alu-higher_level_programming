#!/usr/bin/node

const args = process.argv.slice(2);

// Check if the first element exists
if (args[0] === undefined) {
    console.log("No argument");
} else {
    console.log(args[0]);
}