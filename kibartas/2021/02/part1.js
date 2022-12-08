const input = require("fs")
  .readFileSync(require("path").join(__dirname, "input.txt"), "utf8")
  .trim();

let depth = 0;
let horizontal = 0;
input.split("\n").forEach((element) => {
  const pair = element.split(" ");

  if (pair[0] === "forward") {
    horizontal += parseInt(pair[1]);
  } else if (pair[0] === "down") {
    depth += parseInt(pair[1]);
  } else if (depth - pair[1] < 0) {
    depth = 0;
  } else {
    depth -= pair[1];
  }
});
let result = horizontal * depth;
console.log({ result });
