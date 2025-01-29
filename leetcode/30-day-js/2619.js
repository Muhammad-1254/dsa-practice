/**
 * @return {null|boolean|number|string|Array|Object}
 */
Array.prototype.last = function (arr) {
    if(this.length)
        return this[this.length-1]
    return -1
};

nums = [1, 2, 3];
nums = [];
nums = [null, {}, 3];

console.log(nums.last());
