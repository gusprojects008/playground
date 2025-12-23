var addTwoPromises = async function(promise1, promise2) {
  const [v1, v2] = await Promise.all([promise1, promise2]);
  return v1 + v2;
};

const promise1 = new Promise(resolve => setTimeout(() => resolve(x), 20));
const promise2 = new Promise(resolve => setTimeout(() => resolve(x), 40));

//console.log(addTwoPromises(promise1.resolve(2), promise2.resolve(2));
console.log(addTwoPromises(promise1.resolve(4), promise2.resolve(4)));
