/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
  let tempArr = [];
  while (n > 0) {
    for (const item of arr) {
      if (Array.isArray(item)) {
        tempArr.push(...item);
      } else {
        tempArr.push(item);
      }
    }
    arr = tempArr 
    tempArr = []
    n--;
  }

  return arr
};

// let arr = [1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]
// let n = 0

// let arr = [1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]];
// let n = 1;

let arr = [[1, 2, 3], [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]
let n = 2
console.log(flat(arr, n));
