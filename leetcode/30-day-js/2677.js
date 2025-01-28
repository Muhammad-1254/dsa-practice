/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    const newArr = []
    let tempArr = []
    let count = 0
     for(let i =0;i<arr.length;i++){
        tempArr.push(arr[i])
        count++
        if(count== size){
            newArr.push(tempArr)
            tempArr = []
            count =0
        }else if(i+size>=arr.length){
            newArr.push(arr.splice(i,i+size))
            break
        }
    
     }
    return newArr 
    };
    