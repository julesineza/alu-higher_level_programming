#!/usr/bin/node

const args = process.argv.slice(2);

const num = parseInt(args[0]);

if (!isNaN(num)) {
    for (let i = 0; i < num; i++) {
        let row = "";
        for (let j = 0; j < num; j++) {
            row += "X";
        }
        console.log(row);}
} else {
    console.log("Missing number of occurrences");
}