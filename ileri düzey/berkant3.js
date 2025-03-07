// input = ['redact', 'redux', 'red'] -> output = 're'

const sol = arr => {
  let same = "";
  outer : for (let i = 0; i < arr[0].length; i++){
    // console.log(arr[0][i]); // r
    inner : for (let j = 0; j < arr.length; j++){
      if (arr[0][i] !== arr[j][i]) {
        break outer;
      }
    }
    same += arr[0][i];
  }
  return same;
}

console.log(sol(["redact", "redux", "red"]));


const longest = (arr) => {
  let temp = "";
  let res = "";
  outer: for (let i = 0; i < arr[0].length; i++) {
    temp = arr[0][i]; // r
    inner: for (let j = 1; j < arr.length; j++) {
      if (temp !== arr[j][i]) {
        break outer;
      }
    }
    res += temp;
  }
  return res;
};

// console.log(longest(["redact", "redux", "red"]));
