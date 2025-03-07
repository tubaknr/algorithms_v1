// abcabcbb -> abc en uzun alt dizgi. uzunluğu 3. output = 3.
// bbbbbb -> b -> 1.

const seriesLengthFinder = (str) => {
  let map = {}; // (hash map): Harflerin en son hangi indekslerde geçtiğini saklar.
  let start = 0; // Tekrarlanan karakterleri geçip yeni alt diziyi başlatan indeks.
  let max = 0; // Şu ana kadar bulunan en uzun tekrarsız alt dizinin uzunluğu.
  for (let i = 0; i < str.length; i++) {
    if (map[str[i]] !== undefined) {
      start = Math.max(start, map[str[i]] + 1);
    }
    map[str[i]] = i;
    max = Math.max(max, i - start + 1);
  }
  return max - 1;
};

console.log(finder("abcabcdd"));
// console.log(seriesLengthFinder("bbbbbb"));
