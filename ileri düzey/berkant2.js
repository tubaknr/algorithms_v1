// romen characters
// I 1
// V 5
// X 10
// L 50
// C 100
// D 500
// M 1000

// input= 123 -> output = CXXIII

const solution = (num) => {
  let str = [["I", "V"], ["X", "L"], ["C", "D"], ["M"]];

  let i = 0;
  let res = "";
  let temp = 0;
  while (num > 0) {
    temp = num % 10; // HEP KALAN SAYININ SON BASAMAĞINI ALARAK
    if (temp === 9) {
      // IX
      res = str[i][0] + str[i + 1][0] + res;
    } else if (temp === 4) {
      // IV
      res = str[i][0] + str[i][1] + res;
    } else if (temp >= 5) {
      // V, VI, VII, VIII
      res = str[i][1] + str[i][0].repeat(temp - 5) + res;
    } else {
      // I, II, III
      res = str[i][0].repeat(temp) + res;
    }

    num = Math.floor(num / 10); // SONDAN BİRER BASAMAKA ATARAK. SAĞDAN SOLA.
    i++;
  }
  return res;
};

console.log(sol2(123));
console.log(solution(123));
console.log(sol2(256));
console.log(solution(256));
// console.log(solution3(123));
// console.log(solution3(256));
