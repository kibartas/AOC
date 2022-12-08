const input = require("fs")
  .readFileSync(require("path").join(__dirname, "input.txt"), "utf8")
  .trim();

const lines = input.split("\n");

const pairs = lines
  .map((line) => {
    return line.split(" -> ").map((pair) => {
      return pair.split(",");
    });
  })
  .map((pair) => [
    [parseInt(pair[0][0]), parseInt(pair[0][1])],
    [parseInt(pair[1][0]), parseInt(pair[1][1])],
  ]);

const points = {};

let count = 0;

pairs.forEach((pair) => {
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
      if (points[key]) {
        points[key]++;
      } else {
        points[key] = 1;
      }
    }
  } else if (pair[0][1] === pair[1][1]) {
    if (pair[0][0] > pair[1][0]) {
      from = pair[0][0];
      to = pair[1][0];
    } else {
      from = pair[1][0];
      to = pair[0][0];
    }
    for (let i = from; i >= to; i--) {
      const key = `${i},${pair[0][1]}`;
      if (points[key]) {
        points[key]++;
      } else {
        points[key] = 1;
      }
    }
  } else {
    if (pair[0][0] > pair[1][0] && pair[0][1] > pair[1][1]) {
      let fromX = pair[0][0];
      let toX = pair[1][0];
      let fromY = pair[0][1];
      let toY = pair[1][1];
      while (fromX >= toX && fromY >= toY) {
        const key = `${fromX},${fromY}`;
        if (points[key]) points[key]++;
        else points[key] = 1;
        fromX--;
        fromY--;
      }
    } else if (pair[0][0] > pair[1][0] && pair[0][1] < pair[1][1]) {
      let fromX = pair[0][0];
      let toX = pair[1][0];
      let fromY = pair[0][1];
      let toY = pair[1][1];
      while (fromX >= toX && fromY <= toY) {
        const key = `${fromX},${fromY}`;
        if (points[key]) points[key]++;
        else points[key] = 1;
        fromX--;
        fromY++;
      }
    } else if (pair[0][0] < pair[1][0] && pair[0][1] > pair[1][1]) {
      let fromX = pair[0][0];
      let toX = pair[1][0];
      let fromY = pair[0][1];
      let toY = pair[1][1];
      while (fromX <= toX && fromY >= toY) {
        const key = `${fromX},${fromY}`;
        if (points[key]) points[key]++;
        else points[key] = 1;
        fromX++;
        fromY--;
      }
    } else if (pair[0][0] < pair[1][0] && pair[0][1] < pair[1][1]) {
      let fromX = pair[0][0];
      let toX = pair[1][0];
      let fromY = pair[0][1];
      let toY = pair[1][1];
      while (fromX <= toX && fromY <= toY) {
        const key = `${fromX},${fromY}`;
        if (points[key]) points[key]++;
        else points[key] = 1;
        fromX++;
        fromY++;
      }
    } else {
      const key = `${pair[0][0]},${pair[0][1]}`;
      if (points[key]) points[key]++;
      else points[key] = 1;
    }
  }
});

count = Object.values(points).filter((point) => point > 1).length;

console.log({ count });
