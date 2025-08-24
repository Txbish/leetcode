/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function (arr, fn) {
  const ret = Array(arr.length);
  for (let i = 0; i < arr.length; i++) {
    ret[i] = fn(arr[i], i); // pass element, index, and array
  }
  return ret;
};
