#!/usr/bin/node

class Rectangle {
    constructor (w,h) {
        this.width = w;
        this.height = h;
    }

    print(params) {
        for (let i = 0; i < this.height; i++) {
        let row = "";
        for (let j = 0; j < this.width; j++) {
            row += "X";
        }
        console.log(row);}
    }

    rotate () {
        this.width=this.height
        this.height=this.width
    }

    double () {
        this.width = this.width *2
        this.height = this.height * 2
    }
}

const r1 = new Rectangle(2, 3);
console.log('Normal:');
r1.print();

console.log('Double:');
r1.double();
r1.print();

console.log('Rotate:');
r1.rotate();
r1.print();

module.exports =Rectangle;