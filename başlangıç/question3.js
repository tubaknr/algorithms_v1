// [555, 901, 899, 1276, 12] basamak sayısı çift olan kaç sayı var?

const solution = (arr) => {
  return arr.filter((a) => a.toString().length % 2 == 0).length;
};

console.log(sol([555, 901, 899, 1276, 12]));
