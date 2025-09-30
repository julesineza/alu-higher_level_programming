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



module.exports =Rectangle;