// input = [-1, 0, 1, 2, -1, -4] toplamı 0 eden benzersiz üçlüleri bir arayde bir araya topla.
// output = [[-1, 0, 1], [-1, -1, 2]]
const sumThree = (arr) => {
  let left = 0;
  let right = 0;
  let sum = 0;
  let sums = [];
  arr = arr.sort((a, b) => a - b);
  for (let i = 0; i < arr.length; i++) {
    if (i > 0 && arr[i] === arr[i - 1]) {
      continue;
    }
    left = i + 1;
    right = arr.length - 1;
    while (left < right) {
      sum = arr[left] + arr[i] + arr[right];
      if (sum < 0) {
        left++;
      } else if (sum > 0) {
        right--;
      } else {
        sums.push([arr[left], arr[i], arr[right]]);
        left++;
        right--;
        while (left < right && arr[left] === arr[left - 1]) left++;
        while (left < right && arr[right] === arr[right + 1]) right--;
      }
    }
  }
  return sums;
};

console.log(sol([-1, 0, 1, 2, -1, -4]));
