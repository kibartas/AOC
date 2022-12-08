const input = require("fs")
  .readFileSync(require("path").join(__dirname, "input.txt"), "utf8")
  .trim()
  .split(",")
  .map((el) => parseInt(el));

let result = 0;

let max = 0;

const sum = input.reduce((acc, el) => {
  if (el > max) max = el;
  return el + acc;
}, 0);

const average = Math.floor(sum / input.length);

result = 1e8;

for (let i = 0; i < 2 * average; i++) {
  const fuelUsed = input.reduce((acc, el) => {
    return acc + Math.abs(i - el);
  }, 0);
  if (fuelUsed < result) result = fuelUsed;
}

console.log({ result });
