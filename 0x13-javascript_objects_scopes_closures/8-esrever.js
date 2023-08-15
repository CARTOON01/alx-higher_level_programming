#!/usr/bin/node

exports.init = function (list) {
    const newList = [];
    let index = 0;
    const len = list.length;;
    while (index < len) {
        newList.push(list.pop());
        index++;
    }
    return newList;
};