function bfs(x, y, visited, board, target, key) {
  const n = visited.length;
  const dx = [1, -1, 0, 0];
  const dy = [0, 0, 1, -1];
  let sum = 1;
  let q = [[x, y]];
  visited[x][y] = key;

  while (q.length != 0) {
    let now = q.shift();
    for (let i = 0; i < 4; i++) {
      let nx = now[0] + dx[i];
      let ny = now[1] + dy[i];
      if (0 <= nx && nx < n && 0 <= ny && ny < n) {
        if (!visited[nx][ny] && board[nx][ny] == target) {
          visited[nx][ny] = key;
          sum += 1;
          q.push([nx, ny]);
        }
      }
    }
  }
  return [visited, sum];
}

function solution(board) {
  let n = board.length;
  let answer = -1;
  let visited = Array.from(Array(n), () => Array(n).fill(false));
  let key = 1;
  let valueDict = {};

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (!visited[i][j]) {
        const target = board[i][j];
        returnValue = bfs(i, j, visited, board, target, key);
        visited = returnValue[0];
        valueDict[key] = returnValue[1];
        key += 1;
      }
    }
  }
  for (let i = 0; i < n; i++) {
    sum = valueDict[visited[i][0]];
    prev = visited[i][0];
    for (let j = 0; j < n - 1; j++) {
      if (visited[i][j] != visited[i][j + 1]) {
        prev = visited[i][j + 1];
        sum += valueDict[visited[i][j + 1]];
      }
    }
    answer = Math.max(answer, sum);
  }
  for (let j = 0; j < n; j++) {
    sum = valueDict[visited[0][j]];
    prev = visited[0][j];
    for (let i = 0; i < n - 1; i++) {
      if (visited[j][i] != visited[i][j + 1]) {
        prev = visited[i][j + 1];
        sum += valueDict[visited[i][j + 1]];
      }
    }
    answer = Math.max(answer, sum);
  }
  console.log(answer);
  return answer;
}

solution(["ABBBBC", "AABAAC", "BCDDAC", "DCCDDE", "DCCEDE", "DDEEEB"]);
