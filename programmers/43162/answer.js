function solution(n, computers) {
  var answer = 0;
  let visited = Array(n).fill(false);

  let dfs = (computers, visited, i) => {
    if (visited[i]) return;

    visited[i] = true;
    for (let j in computers[i]) {
      if (computers[i][j] == 1) {
        dfs(computers, visited, j);
      }
    }
  };

  for (let i = 0; i < n; i++) {
    if (!visited[i]) {
      answer++;
      dfs(computers, visited, i);
    }
  }
  return answer;
}
