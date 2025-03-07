// nums1=[1,3], nums=[2] -> median of [1,2,3] is 2.
// nums1=[1,3], nums=[2,4] -> median of [1,2,3,4] is 2+3 / 2 = 2.5.


const solution = (arr1, arr2) => {
  let newArr = arr1.concat(...arr2).sort((a, b) => a - b);
  if (newArr.length % 2 == 1) {
    return newArr[Math.floor(newArr.length / 2)];
  } else {
    let middle1 = newArr[newArr.length / 2 - 1];
    let middle2 = newArr[newArr.length / 2];
    return (middle1 + middle2) / 2;
  }
};

console.log(sol([1, 3], [2]));
console.log(sol([1, 3], [2, 4]));
