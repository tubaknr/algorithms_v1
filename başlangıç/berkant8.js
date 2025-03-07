// 123->321; -123-> -321; 120-> 21.

const solution = (num) => {
  // işareti baştan at, sonra Math.sign ile ekle.
  let digits = Math.abs(num).toString().split("").reverse();
  return Number(digits.join("")) * Math.sign(num);
};

console.log(sol(120));
console.log(sol(-123));
console.log(sol(123));
