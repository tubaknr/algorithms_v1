// asal çarpanlarını bul? input 69 ise output [3,23] olmalı.

const solution = (num) => {
  let factors = [];
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i == 0) {
      factors.push(i);
      num /= i;
    }
  }
  if (num > 1) {
    factors.push(num);
  }
  return factors;
};

const solution2 = (num) => {
  let start = 2;
  let factors = [];
  while (num >= 2) {
    if (num % start == 0) {
      factors.push(start);
      num /= start;
    }
    start++;
  }
  return factors;
};

console.log(sol(69));
