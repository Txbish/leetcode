/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let val = init;   // start with init
    for (let i = 0; i < nums.length; i++) {
        val = fn(val, nums[i]); // accumulate
    }
    return val;
};
