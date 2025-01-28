var TimeLimitedCache = function() {
    const cache = new Map();
 
   function set(key, value, duration) {
     const itemExist = cache.get(key);
     if (itemExist) {
       cache.set(key,{ value, duration:Date.now()+duration });
       return true;
     } else {
         cache.set(key,{value,duration:Date.now()+duration})
       return false;
     }
   }
   function get(key) {
     const item = cache.get(key);
     if (item && item.duration > Date.now()) {
       return item.value;
     } else {
       return -1;
     }
   }
   function count() {
     let count = 0;
     cache.forEach((value,) => {
         if (value.duration > Date.now()) {
         count += 1;
       }
     });
     return count;
   }
   return { set, get, count };  
 };
 
 /** 
  * @param {number} key
  * @param {number} value
  * @param {number} duration time until expiration in ms
  * @return {boolean} if un-expired key already existed
  */
 TimeLimitedCache.prototype.set = function(key, value, duration) {
     
 };
 
 /** 
  * @param {number} key
  * @return {number} value associated with key
  */
 TimeLimitedCache.prototype.get = function(key) {
     
 };
 
 /** 
  * @return {number} count of non-expired keys
  */
 TimeLimitedCache.prototype.count = function() {
     
 };
 
 /**
  * const timeLimitedCache = new TimeLimitedCache()
  * timeLimitedCache.set(1, 42, 1000); // false
  * timeLimitedCache.get(1) // 42
  * timeLimitedCache.count() // 1
  */