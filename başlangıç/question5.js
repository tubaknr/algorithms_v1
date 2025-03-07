// n=434 => 4*3*4 - 4+3+4 = 48-11 = 37 result.


const solution = (num) => {
  let digits = num.toString().split("").map(Number);
  const mults = digits.reduce((a, b) => a * b, 1);
  const sums = digits.reduce((a, b) => a + b, 0);
  return mults - sums;
};

console.log(sol(434));
