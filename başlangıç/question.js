// [8,4,6,2,3] -> output = [4,2,4,2,3], birbirinden çıakrarak ilerle.


const solution = (arr) => {
  return arr.map((ele, i) => {
    for (let j = i + 1; j < arr.length; j++) {
      if (ele > arr[j]) {
        return ele - arr[j];
      }
    }
    return ele;
  });
};

const solution2 = arr => {
  return arr.map((ele, i) => {
    for (let j = i + 1; j < arr.length; j++){
      if (ele > arr[j]) {
        return ele - arr[j];
      }
    }
    // j=i+1 kalmadığında; i son elemana geldiğinde.
    return ele;
  })

}

console.log(solution2([8, 4, 6, 2, 3]));
