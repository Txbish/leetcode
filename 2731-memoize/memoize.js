/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
  let arr = {};
  return function (...args) {
    let key = JSON.stringify(args); // turn args into a string key
    if (key in arr) {
      return arr[key];
    }
    arr[key] = fn(...args);
    return arr[key];
  };
}

/**
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1
 */
