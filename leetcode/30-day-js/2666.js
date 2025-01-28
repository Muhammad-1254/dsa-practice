/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function (fn) {

    return function (...args) {
        let ans = undefined;
        if (!fn) return ans;
        else ans = fn(...args);

        fn = undefined;
        return ans;
    };
};

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */
