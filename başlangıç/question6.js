// nums = [1, 2, 3, 4, 4, 3, 2, 1], n = 4
// output = [1,4,2,3,3,2,4,1] => nums ın 4 birim ardındaki değeri koy.


const solution = (arr, num) => {
  let newArr = [];
  for (let i = 0; i < num; i++) {
    newArr.push(arr[i]);
    newArr.push(arr[i + num]);
  }
  return newArr;
};

console.log(sol([1, 2, 3, 4, 4, 3, 2, 1], 4));
