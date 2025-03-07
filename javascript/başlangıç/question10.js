// i1 = [2,4,3], i2=[5,6,4]
// 342 + 465 = 807
// output = [7,0,8]

const solution = (arr1, arr2) => {
  let num1 = Number(arr1.reverse().join(""));
  let num2 = Number(arr2.reverse().join(""));
  const sums = num1 + num2;
  return sums.toString().split("").reverse().map(Number);
};

console.log(sol([2, 4, 3], [5, 6, 4]));
