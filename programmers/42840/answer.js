function solution(answers) {
  var answer = [];
  const n = answers.length;
  const answer1 = [1, 2, 3, 4, 5];
  const answer2 = [2, 1, 2, 3, 2, 4, 2, 5];
  const answer3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
  let count = [0, 0, 0];

  for (let i = 0; i < n; i++) {
    if (answers[i] == answer1[i % 5]) count[0]++;
    if (answers[i] == answer2[i % 8]) count[1]++;
    if (answers[i] == answer3[i % 10]) count[2]++;
  }

  max_value = Math.max(...count);
  if (max_value == count[0]) answer.push(1);
  if (max_value == count[1]) answer.push(2);
  if (max_value == count[2]) answer.push(3);
  return answer;
}

solution([1, 3, 2, 4, 2]);
