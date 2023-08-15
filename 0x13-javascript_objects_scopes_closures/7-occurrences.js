#!/usr/bin/node

exports.nbOccurrences = function ( list, searchElement ) {
    const newList = list.filter( element => element === searchElement );
    return newList.length;
}