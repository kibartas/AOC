const input = require("fs")
  .readFileSync(require("path").join(__dirname, "input.txt"), "utf8")
  .trim()
  .split(",");

let fishes = {};

input.forEach((fish) => {
  fish = parseInt(fish);
  if (fishes[fish]) fishes[fish]++;
  else fishes[fish] = 1;
});

for (let i = 0; i < 256; i++) {
  const newFishes = {};
  for (let j = 8; j > 0; j--) {
    if (fishes[j] === undefined) continue;
    newFishes[j - 1] = fishes[j];
  }
  if (fishes[0]) {
    newFishes[8] = fishes[0];
    if (newFishes[6]) {
      newFishes[6] += fishes[0];
    } else {
      newFishes[6] = fishes[0];
    }
  }
  fishes = { ...newFishes };
}

let result = Object.values(fishes).reduce((el, acc) => el + acc, 0);
console.log({ result });
