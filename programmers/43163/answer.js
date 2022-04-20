function solution(begin, target, words) {
  const n = words.length;

  const match = (str1, str2) => {
    let count = 0;
    for (let i = 0; i < str1.length; i++) {
      if (str1[i] !== str2[i]) count++;
    }
    return count <= 1;
  };

  const bfs = (begin, target, words) => {
    let q = [[begin, 0]];
    let visited = Array(n).fill(false);

    while (q.length) {
      now = q.shift();
      if (now[0] == target) return now[1];
      for (let i = 0; i < n; i++) {
        if (!visited[i] && match(words[i], now[0])) {
          visited[i] = true;
          q.push([words[i], now[1] + 1]);
        }
      }
    }
    return 0;
  };
  return bfs(begin, target, words);
}

console.log(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]));
