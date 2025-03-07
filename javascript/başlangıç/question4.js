// input n=5 => 5 elemanlı diziz oluştur ve tplamları 0 olsun.
const solution = (num) => {
  let arr = [];
  if (num % 2 == 1) {
    arr.push(0);
  }
  // 0 ekledik; 1 den başlayacağız.
  for (let i = 1; i < num / 2; i++) {
    arr.push(i);
    arr.push(-i);
  }
  return arr;
};

console.log(sol(7));
