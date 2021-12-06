const input = require("fs")
  .readFileSync(require("path").join(__dirname, "input.txt"), "utf8")
  .trim();

const lines = input.split("\n");

const pairs = lines.map((line) => {
  return line.split(" -> ").map((pair) => {
    return pair.split(",");
  });
});

const oneDirectionalPairs = pairs
  .filter((pair) => pair[0][0] === pair[1][0] || pair[0][1] === pair[1][1])
  .map((pair) => [
    [parseInt(pair[0][0]), parseInt(pair[0][1])],
    [parseInt(pair[1][0]), parseInt(pair[1][1])],
  ]);

const points = {};

let count = 0;
const alternatePoints = {};

oneDirectionalPairs.forEach((pair) => {
  let from;
  let to;
  if (pair[0][0] === pair[1][0]) {
    if (pair[0][1] > pair[1][1]) {
      from = pair[0][1];
      to = pair[1][1];
    } else {
      from = pair[1][1];
      to = pair[0][1];
    }
    for (let i = from; i >= to; i--) {
      const key = `${pair[0][0]},${i}`;
      if (key === "409,65") console.log(from, to);
      if (points[key]) {
        points[key]++;
      } else {
        points[key] = 1;
      }
    }
  } else {
    if (pair[0][0] > pair[1][0]) {
      from = parseInt(pair[0][0]);
      to = parseInt(pair[1][0]);
    } else {
      from = parseInt(pair[1][0]);
      to = parseInt(pair[0][0]);
    }
    for (let i = from; i >= to; i--) {
      const key = `${i},${pair[0][1]}`;
      if (points[key]) {
        points[key]++;
      } else {
        points[key] = 1;
      }
    }
  }
});

count = Object.values(points).filter((point) => point > 1).length;

console.log({ count });
