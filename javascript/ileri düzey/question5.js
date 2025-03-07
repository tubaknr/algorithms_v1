// Sıralanmamış bir tamsayı dizisi veridiğinde, eksik olan en küçük pozitif tam sayıyı bul.
// input = [1, 2, 0] -> output = 3
// input = [3,4,-1,1] -> output = 2

const sol = (arr) => {
  let pos = new Set();
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > 0) {
      pos.add(arr[i]);
    }
  }
  // console.log(pos);
  let smallest = 1;
  while (pos.has(smallest)) {
    smallest++;
  }
  return smallest;
};

// const findMin = (arr) => {
//   let loss = [];
//   arr = arr.sort((a, b) => a - b);
//   for (let i = 0; i < arr.length; i++) {
//     if (arr[i + 1] - arr[i] > 1) {
//       let diff = arr[i + 1] - arr[i];
//       for (let j = diff; j > 1; j--) {
//         // kaç sayı eksik var
//         loss.push(arr[i] + j - 1);
//       }
//     }
//   }
//   if (loss.length === 0) {
//     loss.push(arr[arr.length - 1] + 1);
//   }
//   loss.sort((a, b) => a - b);
//   if (loss[loss.length - 1] > 0) {
//     return loss[loss.length - 1];
//   } else {
//     return [];
//   }
// };

const findMin = (arr) => {
  let arrSet = new Set();

  for (let num of arr) {
    if (num > 0) {
      // SADECE POZİTİF SAYILARI EKLE.
      arrSet.add(num);
    }
  }
  let smallest = 1;
  while (arrSet.has(smallest)) {
    smallest++;
  }
  return smallest;
};

console.log(sol([1, 2, 0]));
console.log(sol([3, 4, -1, 1]));
