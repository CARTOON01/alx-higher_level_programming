#!/usr/bin/node

module.exports = class Rectangle {
    constructor (w, h) {
            if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
            }
    }

    print () {
        let str = '';
        let w = this.width;
        let h = this.height;

        while (w > 0){
            console.log(str);
            w--;
        }
        while (h > 0){
            str += 'X';
            h--;
        }
    }
};