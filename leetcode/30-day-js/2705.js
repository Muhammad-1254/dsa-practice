/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */

var compactObject = function (obj) {
  if (typeof obj !== "object") return;

  let result = undefined;
  if (Array.isArray(obj)) {
    result = [];
    for (const item of obj) {
      if (typeof item === "object" && item!==null) {
        result.push(compactObject(item));
      } else {
        if (Boolean(item)) {
          result.push(item);
        }
      }
    }
  } else {
    result = {};
    for (const [key, item] of Object.entries(obj)) {
      if (typeof item === "object" && item!==null) {
        result[key]  = compactObject(item)
      } else {
        if (Boolean(item)) {
          result[key] = item;
        }
      }
    }
  }

  return result;
};

obj = [null, 0, false, 1];
// Output: [1]
// obj = [null, 0, 5, [0], [false, 16]]
// Output: [5, [], [16]]

// obj = { a: null, b: [false, 1] };
//  Output: {"b": [1]}

console.log(compactObject(obj));

