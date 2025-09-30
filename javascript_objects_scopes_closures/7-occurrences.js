#!/usr/bin/node

function nbOccurences (list, searchElement) {
    let count = 0
    for (let item of list) {
        if (item === searchElement) {
            count= count +1
        }
    }
    return count
}


module.exports = nbOccurences;