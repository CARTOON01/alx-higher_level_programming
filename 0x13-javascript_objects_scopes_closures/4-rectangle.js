#!/usr/bin/node

modulel.exports = class Rectangle {
    constructor(w, h) {
        if (w > 0 && h > 0) {
            this.width = w;
            this.height = h;
        }
    }

    print () {
        let str = '';
        let w = this.width;
        let h = this.height;

        while (w > 0) {
            str += 'X';
            w--;
        }
        while (h > 0) {
            console.log(str);
            h--;
        }
    }
    rotate () {
        [this.width, this.height] = [this.height, this.width];
    }
    double () {
        this.width *= 2;
        this.height *= 2;
    }
};