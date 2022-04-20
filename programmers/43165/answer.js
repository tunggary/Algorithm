function solution(numbers, target) {
  const n = numbers.length;
  if (n === 0 && target === 0) {
    return 1;
  } else if (n === 0) {
    return 0;
  } else {
    let array = numbers.slice(1, numbers.length);
    return solution(array, target - numbers[0]) + solution(array, target + numbers[0]);
  }
}

console.log(solution([1, 1, 1, 1, 1], 3));
