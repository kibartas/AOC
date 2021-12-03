const input = require("fs")
  .readFileSync(require("path").join(__dirname, "input.txt"), "utf8")
  .trim();

const binaryStrings = input.split("\n");
const length = binaryStrings.length;
let gamma = "";
let epsilon = "";
const stringLength = binaryStrings[0].length;
const sums = new Array(stringLength).fill(0);
binaryStrings.forEach((string) => {
  for (let i = 0; i < stringLength; i++) {
    sums[i] += parseInt(string[i]);
  }
});

sums.forEach((sum) => {
  if (sum > length / 2) {
    gamma += "1";
    epsilon += "0";
  } else {
    gamma += "0";
    epsilon += "1";
  }
});

let gammaDecimal = 0;
let epsilonDecimal = 0;

let multiplier = 1;
for (let i = gamma.length - 1; i >= 0; i--) {
  gammaDecimal += parseInt(gamma[i]) * multiplier;
  epsilonDecimal += parseInt(epsilon[i]) * multiplier;
  multiplier *= 2;
}

const result = gammaDecimal * epsilonDecimal;

console.log({ result });
