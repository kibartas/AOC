const input = require("fs")
  .readFileSync(require("path").join(__dirname, "input.txt"), "utf8")
  .trim();

let lastEl = 999;
let result = 0;
input.split("\n").forEach((el) => {
  el = parseInt(el);
  if (el > lastEl) result++;
  lastEl = el;
});

console.log({ result });
