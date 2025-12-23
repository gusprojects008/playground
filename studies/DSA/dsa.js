var createHelloWorld = function() {
    return function() {
        return "Hello World";
    }
};

var reduce = function(nums, fn, init) {
  let curr = init;
  for (let i = 0;i<nums.length;i++) {
    curr = fn(curr, nums[i]);
  }
  return curr;
};

// Function Composition
var compose = function(functions) {
  return function(x) {
    let result = x;
    for (let i = functions.length - 1; i >= functions.length - 1; i--) {
      result = functions[i](result);
    }
    return result;
  }
};

var argumentsLength = function(...args) {
  return args.length
};

var once = function(fn) {
    let flag = false;
  return function(...args) {
    if (!flag) {
      flag = true;
      return fn(...args);
    } else {
      return undefined;
    };
  }
};

// Within our function expression:
var memoize = function(fn) {
  /* that will be used as a cache, that is, to record the arguments already used and their respective results 
  according to the function that was called that used the arguments at the time of the function call. */
  const cache = {};
  /* We will return a new function that receives an unspecified number of arguments, and we will simply check if the passed arguments
  have already been used in another function call. To check this, we need to convert the "args" array into a string to use it as a key
  for our cache, for example: "[1,2]": 3 because fn sums the arguments "[1,2]". */
  return function(...args) {
    /* In this way, we return the value associated with the cached key if the key, that is, the passed arguments, already exist as a
    cached key. */
    const key = JSON.stringify(args);
    console.log(key);
    if (key in cache) {
      return cache[key];
    }
    console.log("args: ", args);
    console.log("...args: ", ...args);
    /* Otherwise, we call the callback function "fn" and call its method (apply) to apply/pass the list of arguments "args" to it,
    and in this way, we store the result of the operations in the constant result. And we return result. */
    const result = fn.apply(this, args);
    cache[key] = result;
    return result;
  };
};

// We created an asynchronous function that receives two promise objects
var addTwoPromises = async function(promise1, promise2) {
  /* We defined two constants to store the result of each promise, resulting from the "all()" method on the promise and return the
  result of each one in the order promises passed as argument to "all()". */
  /* But the important detail is that internally, both promises return results at different times: the firt returns a value after
  40 milliseconds, and the second returns a value after 20 milliseconds, Therefore, we must use "await" to wait for the result of both promises, and in this way, return the sum of the two values. */
  const [v1, v2] = await Promise.all([promise1, promise2]);
  return v1 + v2;
};

const promise1 = new Promise(resolve => setTimeout(() => resolve(4), 40));
const promise2 = new Promise(resolve => setTimeout(() => resolve(4), 20));

xxxxxxccccvvvvwsz

var sleeeasn  
