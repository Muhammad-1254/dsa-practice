/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function (arr1, arr2) {
  const result = new Map();

  for (const item of arr1) {
    result.set(item.id, item);
  }

  for (const item of arr2) {
    const arr1Item = result.get(item.id);
    if (arr1Item) {
      const updatedItem = { ...item };
      for (const key of Object.keys(arr1Item)) {
        if (!item.hasOwnProperty(key)) {
          updatedItem[key] = arr1Item[key];
        }
      }
      result.set(updatedItem.id, updatedItem);
    } else {
      result.set(item.id, item);
    }
  }
  return Array.from(result.values(), (x) => x).sort((a,b)=>a.id-b.id);
};
const arr1 = [
    {"id": 2, "x": 3, "y": 6},
    {"id": 1, "x": 2, "y": 3},
]
const arr2 = [
    {"id": 3, "x": 0, "y": 0},
    {"id": 2, "x": 10, "y": 20},
]
console.log(join(arr1, arr2));
