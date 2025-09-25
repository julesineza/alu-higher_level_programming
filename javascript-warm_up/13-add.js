#!/usr/bin/node


function add(a, b) {
    return a + b;
}

// Make it visible outside (export it)
module.exports = {
    add
};
