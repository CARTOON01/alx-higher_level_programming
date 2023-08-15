#!/usr/bin/node

const fs = require('fs');
const array = process.argv;
let data;
fs.readFile(`./${array[2]}`, 'utf-8', (err, d) => {
  if (err) {
    console.error(err);
    return;
  }
  data = d;
  fs.readFile(`./${array[3]}`, 'utf-8', (err, d) => {
    if (err) throw err;
    data += d;
    fs.writeFile(`./${array[4]}`, data, (err) => {
      if (err) throw err;
    });
  });
});