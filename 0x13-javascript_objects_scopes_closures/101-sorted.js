#!/usr/bin/node

const dict = require('./101-data').dict;

const keys = [];
const newDict = [];
for  (const key of object.values(dict)) {
    if (!keys.includes(key)) {
        keys.push(key);
    }
}
keys.forEach((key) => {
    const val =  [];
    for (const k of Object.keys(dict)) {
        if (dict[k] === key) {
            val.push(k);
        }
    }
    newDict[key] = val;
});
console.log(newDict);