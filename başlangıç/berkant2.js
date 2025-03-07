// [[4,3,2,-1], [3,-2,-1,6], [5,-4,0,-1]] kaç - li değer var?

const solution = (arr) => {
  return arr //büyük array
    .map((row) => row.filter((r) => r < 0).length) // [1, 2, 2]
    .reduce((a, b) => a + b, 0); // 1+2+2=5!!!!!! // kümülatif toplam.
};

const solution2 = (arr) => {
  let newArr = [];
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr[i].length; j++) {
      if (arr[i][j] < 0) {
        newArr.push(arr[i][j]);
      }
    }
  }
  return newArr.length;
};

console.log(
  sol([
    [4, 3, 2, -1],
    [3, -2, -1, 6],
    [5, -4, 0, -1],
  ])
);
