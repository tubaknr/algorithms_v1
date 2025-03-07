// fibonacci
// 0, 1, 1, 2, 3, 5, 8, 13, 21 , 34, ...

const fibonacci = (num) => {
  let list = [0, 1];
  let a = list[0];
  let b = list[1];
  let temp;
  if (num == 1) {
    return [list[0]];
  }
  for (let i = 0; i < num - 2; i++) {
    temp = a + b;
    a = b;
    b = temp;
    list.push(temp);
  }
  return list;
};

const fibo = (num) => {
  if (num < 0) {
    return [];
  }
  if (num === 1) {
    return [0];
  }
  if (num === 2) {
    return [0, 1];
  }
  let arr = [0, 1];

  for (let i = 2; i < num; i++) {
    arr.push(arr[i - 1] + arr[i - 2]);
  }
  return arr;
};

const fiboIterative = (num) => {
  if (num <= 1) {
    return [0];
  }
  let arr = [0, 1];
  for (let i = 2; i < num; i++) {
    arr.push(arr[i - 1] + arr[i - 2]);
  }
  return arr;
};

const fibo1 = num => {
  let arr = [0, 1];
  for (let i = 0; i < num - 2; i++){
    arr.push(arr[i] + arr[i + 1]);
  }
  return arr;
}

console.log(fibo2(1));
console.log(fibo2(8));
