#!/usr/bin/node

const Base = require('./5-square');

modulel.exports = class Square extends Base {
    charPrint (c) {
        let str = '';
        let w = this.width;
        let h = this.height;
        let ch;
        c ? ch = c : ch = 'X';
        while (w > 0) {
            str += ch;
            w--;
        }
        while (h > 0) {
            console.log(str);
            h--;
        }
    }
};