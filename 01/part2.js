const input = require("fs")
  .readFileSync(require("path").join(__dirname, "input.txt"), "utf8")
  .trim();

let result = 0;
const arr = input.split("\n");
let lastSum = 999;
for (let i = 0; i < arr.length; i++) {
  let sum = 0;
  if (i + 2 === arr.length) break;
  for (let j = i; j < i + 3; j++) {
    sum += parseInt(arr[j]);
  }
  if (sum > lastSum) result++;
  lastSum = sum;
}

console.log({ result });
