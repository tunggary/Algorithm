let answer = new Set();

const is_prime = (x) => {
  if (x <= 1) return false;
  for (let i = 2; i <= Number(Math.sqrt(x)); i++) if (x % i == 0) return false;
  return true;
};

const dfs = (str1, str2) => {
  if (str1 !== "") {
    if (is_prime(Number(str1))) {
      answer.add(Number(str1));
    }
  }

  for (let i = 0; i < str2.length; i++) {
    dfs(str1 + str2[i], str2.slice(0, i) + str2.slice(i + 1, str2.length));
  }
};

function solution(numbers) {
  dfs("", numbers);
  return answer.size;
}

console.log(solution("17"));
