// inputs: [-2,1,-3,4,-1,2,1,-5,4] => output = -4. tekrar edenleri sil, topla.

const solution = (arr) => {
  let newArr = [...new Set(arr)];
  return newArr.reduce((a, b) => a + b, 0);
};

console.log(sol([-2, 1, -3, 4, -1, 2, 1, -5, 4]));
