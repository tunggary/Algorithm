function solution(s) {
  s = s.slice(2, s.length - 2);
  s = s.split("},{");
  dict = {};
  for (let i in s) {
    numArr = s[i].split(",");
    for (let j in numArr) {
      if (dict[numArr[j]]) {
        dict[numArr[j]] += 1;
      } else {
        dict[numArr[j]] = 1;
      }
    }
  }
  sortDict = [];
  for (let i in dict) {
    sortDict.push([dict[i], i]);
  }
  sortDict.sort((a, b) => b[0] - a[0]);
  return sortDict.map((ele) => Number(ele[1]));
}

console.log(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"));
