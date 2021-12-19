const input = require("fs")
  .readFileSync(require("path").join(__dirname, "input.txt"), "utf8")
  .trim()
  .split("\n")
  .map((el) => el.split(" | ").map((iel) => iel.split(" ")));

// 1, 4, 7, 8
const digits = {
  1: ["c", "f"],
  4: ["b", "c", "d", "f"],
  7: ["a", "c", "f"],
  8: ["a", "b", "c", "d", "e", "f", "g"],
};

let result = 0;
input.forEach((el) => {
  el[1].forEach((inEl) => {
    if (
      Object.values(digits).filter((iel) => {
        return iel.length === inEl.length;
      }).length !== 0
    )
      result++;
  });
});

console.log({ result });
