#!/usr/bin/node

const args= process.argv.slice(2);


// Convert all arguments to integers
const numbers = args.map(x => parseInt(x, 10));

// If there are less than 2 numbers, print 0
if (numbers.length < 2) {
    console.log(0);
} else {
    let first = -Infinity;   // Biggest number
    let second = -Infinity;  // Second biggest number

    // Loop through all numbers
    for (let i = 0; i < numbers.length; i++) {
        const num = numbers[i];

        if (num > first) {
            // Found a new biggest number
            second = first; // Old biggest becomes second biggest
            first = num;
        } else if (num > second) {
            // Found a new second biggest number
            second = num;
        }
    }

    console.log(second);
}
