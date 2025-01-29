/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    const results = {}
    let key = undefined

    for(let i =0;i<this.length;i++){
        key = fn(this[i])
            key = key.toString()
            if(results[key]){
                results[key].push(this[i])
            }else{
                results[key] = [this[i]]
            }
    }
    return results
};


// const array = [
//     {"id":"1"},
//     {"id":"1"},
//     {"id":"2"}
//   ]
//  function fn(item) { 
//     return item.id; 
// }

const array = [
    [1, 2, 3],
    [1, 3, 5],
    [1, 5, 9]
  ]
   function fn(list) { 
    return String(list[0]); 
  }


// const   array =["","",""]
// function fn(n) { return String(n); }
console.log(
  array.groupBy(fn) 

)
