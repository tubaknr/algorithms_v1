// [2,7,11,15], 9 => 2+7=9 -> return [0,1]

const solution = (arr, num) => {
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[i] + arr[j] == num) {
        return [i, j];
      }
    }
  }
};

// HASH MAP
const solution2 = (arr, num) => {
  let map = {};
  for (let i = 0; i < arr.length; i++) {
    let comp = num - arr[i];
    if (map[comp] !== undefined) {
      return [map[comp], i];
    }
    map[arr[i]] = i;
  }
};

const solution5 = (arr, num) => {
  let seen = new Set();
  for (let i = 0; i < arr.length; i++) {
    let comp = num - arr[i];
    if (seen.has(comp)) {
      return [arr.indexOf(comp), i];
    }
    seen.add(arr[i]);
    // console.log(seen);
  }
};

// SET
const solution3 = (arr, num) => {
  let seen = new Set();
  for (let i = 0; i < arr.length; i++) {
    let comp = num - arr[i];
    if (comp in seen) {
      return [seen[comp], i];
    }
    seen[arr[i]] = i;
    console.log(seen);
  }
};

console.log(solution6([2, 7, 11, 15], 9));
