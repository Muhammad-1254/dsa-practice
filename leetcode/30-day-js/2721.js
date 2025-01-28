/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    return new Promise((resolve, reject) => {
    const arr = []
    let arrIndex = 0
    functions.forEach((fn,i)=>{
        try {
            fn()
            .then(res=>{
                arr[i] = res
                arrIndex++
                if(arrIndex==functions.length){
                    resolve(arr)
                }
            })
            .catch(err=>{
                reject(err)
            })
        } catch (error) {
            reject(error)
        }
    })
  });  
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */