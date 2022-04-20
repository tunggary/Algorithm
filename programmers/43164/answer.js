function solution(tickets) {
  var answer = [];
  const n = tickets.length;
  graph = {};
  for (let i = 0; i < n; i++) {
    if (graph[tickets[i][0]] == undefined) {
      graph[tickets[i][0]] = [tickets[i][1]];
    } else {
      graph[tickets[i][0]].push(tickets[i][1]);
    }
  }

  for (let i in graph) {
    graph[i].sort();
  }

  stack = ["ICN"];
  while (stack.length > 0) {
    now = stack[stack.length - 1];
    if (graph[now] == undefined || graph[now].length == 0) {
      answer.push(stack.pop());
    } else {
      stack.push(graph[now].shift());
    }
  }
  answer.reverse();
  return answer;
}
