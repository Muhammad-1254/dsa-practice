/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    let tempArr = []
    const newArr = []

    for (let i =0;i<arr.length;i++){
        tempArr.push(arr[i])
        if (tempArr.length== size){
            newArr.push(tempArr)
            tempArr = []
        }
    }
    if (tempArr.length){
        newArr.push(tempArr)
    }
    return newArr


};




arr = [1,9,6,3,2], size = 3
arr = [1,2,3,4,5], size = 1

arr = [8,5,3,2,6], size = 6


console.log(chunk(arr, size))
