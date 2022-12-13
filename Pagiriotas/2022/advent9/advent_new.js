const { exit } = require("process");

function readMovements() {
  const movements = [];
  const fs = require("fs");
  const input = fs.readFileSync("input.txt", "utf8");
  const lines = input.split("\n");
  lines.forEach((line) => {
    const splitedLine = line.split(" ");
    const movement = {
      direction: splitedLine[0],
      distance: parseInt(splitedLine[1]),
    };
    movements.push(movement);
  });
  return movements;
}

function moveHead(head, direction) {
  switch (direction) {
    case "U":
      head.y += 1;
      break;
    case "D":
      head.y -= 1;
      break;
    case "R":
      head.x += 1;
      break;
    case "L":
      head.x -= 1;
      break;
  }
}

function calculateDistance(head, tail) {
  return Math.abs(head.x - tail.x) + Math.abs(head.y - tail.y);
}

function moveTailByOne(head, tail) {
  if (head.x > tail.x && head.y === tail.y) {
    tail.x = tail.x + 1;
  } else if (head.x < tail.x && head.y === tail.y) {
    tail.x = tail.x - 1;
  } else if (head.y > tail.y && head.x === tail.x) {
    tail.y = tail.y + 1;
  } else if (head.y < tail.y && head.x === tail.x) {
    tail.y = tail.y - 1;
  }
}

function moveTailDiagonally(head, tail) {
  //by x
  if (tail.x + 2 === head.x && tail.y + 1 === head.y) {
    tail.x += 1;
    tail.y += 1;
  } else if (tail.x + 2 === head.x && tail.y - 1 === head.y) {
    tail.x += 1;
    tail.y -= 1;
  } else if (tail.x - 2 === head.x && tail.y + 1 === head.y) {
    tail.x -= 1;
    tail.y += 1;
  } else if (tail.x - 2 === head.x && tail.y - 1 === head.y) {
    tail.x -= 1;
    tail.y -= 1;
  }
  //by y
  else if (tail.y + 2 === head.y && tail.x + 1 === head.x) {
    tail.y += 1;
    tail.x += 1;
  } else if (tail.y - 2 === head.y && tail.x + 1 === head.x) {
    tail.y -= 1;
    tail.x += 1;
  } else if (tail.y + 2 === head.y && tail.x - 1 === head.x) {
    tail.y += 1;
    tail.x -= 1;
  } else if (tail.y - 2 === head.y && tail.x - 1 === head.x) {
    tail.y -= 1;
    tail.x -= 1;
  }

  //by 2
  else if (tail.x + 2 === head.x && tail.y + 2 === head.y) {
    tail.x += 1;
    tail.y += 1;
  } else if (tail.x - 2 === head.x && tail.y - 2 === head.y) {
    tail.x -= 1;
    tail.y -= 1;
  } else if (tail.x + 2 === head.x && tail.y - 2 === head.y) {
    tail.x += 1;
    tail.y -= 1;
  } else if (tail.x - 2 === head.x && tail.y + 2 === head.y) {
    tail.x -= 1;
    tail.y += 1;
  }
}

function isHeadDiagonalToTail(head, tail) {
  return (
    (head.x + 1 === tail.x && head.y + 1 === tail.y) ||
    (head.x + 1 === tail.x && head.y - 1 === tail.y) ||
    (head.x - 1 === tail.x && head.y + 1 === tail.y) ||
    (head.x - 1 === tail.x && head.y - 1 === tail.y)
  );
}

function moveTail(head, tail) {
  const distance = calculateDistance(head, tail);
  if (distance === 0) return;
  else if (distance === 1) return;
  else if (distance === 2 && !isHeadDiagonalToTail(head, tail)) {
    moveTailByOne(head, tail);
  } else if (distance === 3 || distance === 4) {
    moveTailDiagonally(head, tail);
  }
}

function addUniqueVisited(visited, tail) {
  if (visited.some((visited) => visited.x === tail.x && visited.y === tail.y))
    return;
  visited.push({ x: tail.x, y: tail.y });
}

function main() {
  const movements = readMovements();
  const head = {
    x: 0,
    y: 0,
  };
  const tail = {
    x: 0,
    y: 0,
  };
  const visited = [];
  movements.forEach((movement) => {
    for (let i = 0; i < movement.distance; i++) {
      moveHead(head, movement.direction);
      moveTail(head, tail);
      addUniqueVisited(visited, tail);
    }
  });
  console.log(visited.length);
}

function generateTails(tailCount) {
  const tails = [];
  for (let i = 0; i < tailCount; i++) {
    tails.push({ x: 0, y: 0 });
  }
  return tails;
}

function main2() {
  const tailsCount = 9;
  const movements = readMovements();
  const head = {
    x: 0,
    y: 0,
  };
  const tails = generateTails(tailsCount);
  const visited = [];
  movements.forEach((movement) => {
    for (let i = 0; i < movement.distance; i++) {
      for (let j = 0; j < tailsCount; j++) {
        if (j === 0) {
          moveHead(head, movement.direction);
          moveTail(head, tails[j]);
        } else {
          moveTail(tails[j - 1], tails[j]);
        }
      }
      const lastTail = tails[tailsCount - 1];
      addUniqueVisited(visited, lastTail);
      appendStringToFile(JSON.stringify(head, null, 2));
      appendStringToFile(JSON.stringify(tails, null, 2));
    }
  });
  console.log(visited.length);
}

function appendStringToFile(string) {
  const fs = require("fs");
  fs.appendFileSync("output.txt", string);
}
main2();
