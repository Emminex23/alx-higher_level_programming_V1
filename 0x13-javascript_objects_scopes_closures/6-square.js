#!/usr/bin/node

class Square extends require('./5-square') {
  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row += 'c';
        }
        console.log(row);
      }
    } else {
      super.print();
    }
  }
}
module.exports = Square;
