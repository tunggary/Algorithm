function solution(salaries, days) {
  currentInfo = [];
  n = salaries.length;
  for (let i = 0; i < n; i++) {
    currentInfo.push([0, 0]);
  }

  for (let day = 0; day < days; day++) {
    for (let i = 0; i < n; i++) {
      currentInfo[i][0] += 1;
      if (currentInfo[i][0] == salaries[i][0]) {
        currentInfo[i][0] = 0;
        currentInfo[i][1] += salaries[i][1];
      }
    }
  }
  for (let i = 0; i < n; i++) {
    if (currentInfo[i][0] >= 1 || currentInfo[i][1] == 0) {
      currentInfo[i][0] = 0;
      currentInfo[i][1] += salaries[i][1];
    }
  }

  let sum = 0;
  for (let i = 0; i < n; i++) {
    sum += currentInfo[i][1];
  }
  return sum;
}

// console.log(
//   solution(
//     [
//       [2, 100],
//       [3, 120],
//       [4, 180],
//       [7, 250],
//     ],
//     6
//   )
// );
// console.log(
//   solution(
//     [
//       [2, 1],
//       [3, 2],
//       [4, 3],
//       [5, 4],
//     ],
//     1
//   )
// );
// console.log(
//   solution(
//     [
//       [1, 1000],
//       [1, 1000],
//     ],
//     3650
//   )
// );

let a = [
  [85, 1],
  [91, 2],
  [88, 3],
];
let totalScore = [0, 0];
let stdTotalScore = [];
let n = a.length;
let v = new Array(4);
console.log(v);
