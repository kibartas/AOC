const input = `abaccccccccccccccaaaccccaaaaaaaaaaaaaccccccaacccccccccccccccccccccccccccccaaaaaa
abaaccaacccccccccaaaaaccccaaaaaaaaaaaaaccccaaacccccccccccccccccccccccccccccaaaaa
abaaccaaacccccccaaaaaacccaaaaaaaaaaaaaacaaaaaaaaccccccccaacccccccccccccccccccaaa
abcaaaaaaaacccccaaaaaacccaaaaaaaaaaaaaacaaaaaaaacccccccaaaacccccccccccccccccaaaa
abcaaaaaaaaccccccaaaaaccaaaaaaaaccaaaaaccaaaaaaccccccccaaaaccaaaccccccccccccaaac
abccaaaaaacccccccaaaaccaaaaaaaaaacaaaacccaaaaaacccccccccakkaaaaaacccccccccccaacc
abccaaaaaacccccccccccccaaaaaaaaaaccccccccaaaaaaccccccckkkkkkkaaacccccccccccccccc
abccaaaaaaccccccccccccccccaaaaaaaaaccccccaacaaacccccckkkkkkkkkaccccccaccaaaccccc
abccaacaaacccccaaccccccccaaacacaaaacaaccccccccccccccakkkoppkkkkicccccaaaaaaccccc
abccccccccccccaaaccccccccaacccccaaaaaaccccccccccccccjkkooppppkiicccccccaaaaccccc
abccccccccccaaaaaaaaccccccccccaaaaaaaccccccccccccccjjjooopppppiiiicccccccaaacccc
abaaacccccccaaaaaaaacccccccaacaaaaaaccccccccccccccjjjjooouuppppiiiiiicccccaacccc
abaaaccccccccaaaaaaccccccccaaaccaaaaacccccccccccjjjjjooouuuupppiiiiiiiiccccacccc
abaaaaaacccccaaaaaacccccaaaaaaaaaacaaaccccccccjjjjjjooouuuuuupppppiiiiiicccccccc
abaaaaaacccccaaaaaacccccaaaaaaaaaacccccccccccjjjjjooooouuxxuupppppqqqijjjccccccc
abaaaacccccaaaaccaaccccccaaaaaaccccccccccccciijjnooooouuuxxxuuupqqqqqqjjjdddcccc
abaaaaaccaaaaaaccacccccccaaaaaaccccccccccaaiiiinnootttuuxxxxuuvvvvvqqqjjjdddcccc
abaaaaaccaaaaaacaaaccaaccaaaaaaccccccccccaaiiinnnntttttuxxxxxvvvvvvqqqjjjdddcccc
abaaccacccaaaaacaaaaaaaccaaccaaccccccccccaaiiinnnttttxxxxxxxyyyyyvvqqqjjjdddcccc
abcccccccaaaaacccaaaaaaccccccaaaaacccccccaaiiinnntttxxxxxxxyyyyyvvvqqqjjjddccccc
SbcccccccaaaaacaaaaaaaaccccccaaaaaccccccccciiinnntttxxxEzzzzyyyyvvqqqjjjdddccccc
abcccccccccccccaaaaaaaaaccccaaaaaaccccccccciiinnnntttxxxxyyyyyvvvvqqjjjdddcccccc
abcccccccccccccaaaaaaaaaacccaaaaaacccccccccciiinnnttttxxxyyyyyvvvqqqjjjdddcccccc
abccccccccccccccccaaaaaaacccaaaaaaccccccccccciiinnnntttwyyywyyyvvrrrkkjdddcccccc
abcccccccccccccccaaaaaaaaccccaaaccccccccccccciiihnnnttwwwywwyyywvrrrkkkeeccccccc
abcccccccccccccccaaaaaaaaccccccccccccccccccccchhhmmmsswwwwwwwwwwwvrrkkkeeccccccc
abcccccccaacccccccacaaacccccccccccccccccccaacchhhhmmsswwwwwswwwwwrrrkkkeeccccccc
abcccccccaaaccacccccaaacccccccccccccccaaccaaccchhhmmssswwwssrrwwwrrrkkkeeccccccc
abcccccccaaaaaaacccccccccccaaaccccccccaaaaaaccchhhmmssssssssrrrrrrrrkkkeeaaacccc
abcccccaaaaaaaaccccccccccccaaaaccccccccaaaaaaachhhmmmssssssllrrrrrrkkkeeeaaacccc
abccccaaaaaaaaaccccccccccccaaaacccccccccaaaaacchhhmmmmsssllllllllkkkkkeeeaaacccc
abccccaaaaaaaaaccccccccccccaaacccccccccaaaaacccchhhmmmmmlllllllllkkkkeeeeaaccccc
abcccccccaaaaaaccccccccccaacccccccaaccaaacaacccchhhmmmmmlllgfflllkkffeeeaaaacccc
abccccccaaaaaaaccccccccccaaaaaaaaaaaaaccccaacccchhhggmmmggggffffffffffeaaaaacccc
abccaacccaacccaaaaccaccccaaaaaaaaaaaaacccccccccccgggggggggggffffffffffaacccccccc
abaaaaccaaaccccaaaaaaccccaaaaaacaaaaaaccccccccccccgggggggggaaaaccffccccccccccccc
abaaaacccccccccaaaaaaccaaaaaaaaaaaaaacccccccccccccccgggaaaaaaaacccccccccccccccca
abaaaaacccccccaaaaaaaccaaaaaaaaaaaaaacccccccccccccccccaaacccaaaaccccccccccccccaa
abaaaaacaaaaccaaaaaaaacaaaaaaaaaaaccccccccccccccccccccaaaccccaaaccccccccccaaacaa
abaaaaacaaaaccaaaaaaaaaaaaaaaaaaacccccccccccccccccccccccccccccccccccccccccaaaaaa
abaaacccaaaaccccaaaccccaaaaaaaaaaacccccccccccccccccccccccccccccccccccccccccaaaaa`;

function parseInput() {
  const result = {
    start: {},
    end: {},
    map: [],
    possibleStartingPoints: [],
  };
  const lines = input.split("\n");
  result.map = lines.map((line, y) =>
    [...line].map((value, x) => {
      if (value === "S") {
        result.start = {
          y,
          x,
        };
        return 0;
      }
      if (value === "E") {
        result.end = { y, x };
        return 25;
      }
      if (value === "a") {
        result.possibleStartingPoints.push({ y, x });
      }
      return value.charCodeAt(0) - "a".charCodeAt(0);
    })
  );
  return result;
}

function pointAsNumber(x, y) {
  return y * 10000 + x;
}
function pointAsString(int) {
  return {
    y: Math.floor(int / 10000),
    x: int % 10000,
  };
}

function getNeighbors(x, y, map) {
  const result = [];
  if (y + 1 < map.length && map[y + 1][x] <= map[y][x] + 1) {
    result.push(pointAsNumber(x, y + 1));
  }
  if (y - 1 >= 0 && map[y - 1][x] <= map[y][x] + 1) {
    result.push(pointAsNumber(x, y - 1));
  }
  if (x + 1 < map[y].length && map[y][x + 1] <= map[y][x] + 1) {
    result.push(pointAsNumber(x + 1, y));
  }
  if (x - 1 >= 0 && map[y][x - 1] <= map[y][x] + 1) {
    result.push(pointAsNumber(x - 1, y));
  }
  return result;
}

function dijkstra(map, start, end) {
  const dist = {};
  const prev = {};
  let queue = [];
  for (let y = 0; y < map.length; y++) {
    for (let x = 0; x < map[y].length; x++) {
      const id = pointAsNumber(x, y);
      dist[id] = Infinity;
      queue.push(id);
    }
  }
  dist[pointAsNumber(start.x, start.y)] = 0;

  while (queue.length) {
    let u = null;
    for (const current of queue) {
      if (u === null || dist[current] < dist[u]) {
        u = current;
      }
    }
    if (u === pointAsNumber(end.x, end.y)) {
      break;
    }
    queue = queue.filter((x) => x !== u);

    const point = pointAsString(u);
    const neighbors = getNeighbors(point.x, point.y, map);
    for (const v of neighbors) {
      if (queue.includes(v)) {
        const alt = dist[u] + 1;
        if (alt < dist[v]) {
          dist[v] = alt;
          prev[v] = u;
        }
      }
    }
  }
  return {
    dist,
    prev,
  };
}

function main1() {
  const { end, start, map } = parseInput();
  const data = dijkstra(map, start, end);
  const distance = data.dist[pointAsNumber(end.x, end.y)];
  console.log(distance);
}

function main2() {
  const { end, start, map, possibleStartingPoints } = parseInput();
  const possibleShortestDistances = [];
  console.log(possibleStartingPoints.length);
  for (let i = 0; i < possibleStartingPoints.length; i++) {
    const point = possibleStartingPoints[i];
    const data = dijkstra(map, point, end);
    const distance = data.dist[pointAsNumber(end.x, end.y)];
    possibleShortestDistances.push(distance);
    console.log(i, distance);
  }
  console.log(possibleShortestDistances);
}

main2();
