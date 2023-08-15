#!/usr/bin/node

const string = 'C is fun';
let x = parseInt(process.argv[2]);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  while (x > 0) {
    console.log(string);
    x--;
  }
}
