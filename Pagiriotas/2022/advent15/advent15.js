const input = `Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3`;

function parseInput() {
  const sensors = [];
  const beacons = [];
  let smallestX = 10000000000;
  let smallestY = 10000000000;
  let largestX = 0;
  let largestY = 0;

  const lines = input.split("\n");
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const parts = line.split(":");
    const sensor = parts[0].split(",");
    const beacon = parts[1].split(",");
    const sensorX = parseInt(sensor[0].split("=")[1]);
    const sensorY = parseInt(sensor[1].split("=")[1]);
    const beaconX = parseInt(beacon[0].split("=")[1]);
    const beaconY = parseInt(beacon[1].split("=")[1]);

    if (sensorX < smallestX) {
      smallestX = sensorX;
    }

    if (beaconX < smallestX) {
      smallestX = beaconX;
    }

    if (sensorY < smallestY) {
      smallestY = sensorY;
    }

    if (beaconY < smallestY) {
      smallestY = beaconY;
    }

    if (sensorX > largestX) {
      largestX = sensorX;
    }

    if (beaconX > largestX) {
      largestX = beaconX;
    }

    if (sensorY > largestY) {
      largestY = sensorY;
    }

    if (beaconY > largestY) {
      largestY = beaconY;
    }

    sensors.push({
      x: sensorX,
      y: sensorY,
    });

    beacons.push({
      x: beaconX,
      y: beaconY,
    });
  }

  if (smallestX < 0) {
    for (let i = 0; i < sensors.length; i++) {
      const sensor = sensors[i];
      const beacon = beacons[i];
      sensor.x -= smallestX;
      beacon.x -= smallestX;
    }
    largestX = largestX - smallestX;
    smallestX = 0;
  }

  if (smallestY < 0) {
    for (let i = 0; i < sensors.length; i++) {
      const sensor = sensors[i];
      const beacon = beacons[i];
      sensor.y -= smallestY;
      beacon.y -= smallestY;
    }
    largestY = largestY - smallestY;
    smallestY = 0;
  }

  const biggestOffset = calculateBiggestOffset(sensors, beacons);

  for (let i = 0; i < sensors.length; i++) {
    const sensor = sensors[i];
    const beacon = beacons[i];
    sensor.x += biggestOffset;
    sensor.y += biggestOffset;
    beacon.x += biggestOffset;
    beacon.y += biggestOffset;
  }

  return {
    sensors,
    beacons,
    smallestX,
    smallestY,
    largestX,
    largestY,
    biggestOffset,
  };
}

function calculateBiggestOffset(sensors, beacons) {
  let biggestOffset = 0;
  for (let i = 0; i < sensors.length; i++) {
    const sensor = sensors[i];
    const beacon = beacons[i];
    const offset =
      Math.abs(sensor.x - beacon.x) + Math.abs(sensor.y - beacon.y);
    if (offset > biggestOffset) {
      biggestOffset = offset;
    }
  }
  return biggestOffset;
}

function createCave(smallestX, smallestY, largestX, largestY, biggestOffset) {
  const cave = [];
  for (let y = smallestY - biggestOffset; y <= largestY + biggestOffset; y++) {
    const row = [];
    for (
      let x = smallestX - biggestOffset;
      x <= largestX + biggestOffset;
      x++
    ) {
      row.push(".");
    }
    cave.push(row);
  }
  return cave;
}

function addUniqueTakenSpot(takenSpots, spot) {
  if (takenSpots.filter((s) => s.x === spot.x && s.y === spot.y).length === 0) {
    takenSpots.push(spot);
  }
}

function drawShapeAroundInRadius(cave, x, y, radius, takenSpots) {
  for (let i = radius; i >= 0; i--) {
    let yOffset = radius - i;
    for (let j = x - radius + yOffset; j <= x + radius - yOffset; j++) {
      if (
        cave[y + yOffset] !== undefined &&
        cave[y + yOffset][j] !== undefined &&
        cave[y + yOffset][j] === "."
      ) {
        const spot = { x: j, y: y + yOffset };
        addUniqueTakenSpot(takenSpots, spot);
        cave[y + yOffset][j] = "#";
      }
      if (
        cave[y - yOffset] !== undefined &&
        cave[y - yOffset][j] !== undefined &&
        cave[y - yOffset][j] === "."
      ) {
        const spot = { x: j, y: y - yOffset };
        addUniqueTakenSpot(takenSpots, spot);
        cave[y - yOffset][j] = "#";
      }
    }
  }
}

function placeSensorsAndBeacons(cave, sensors, beacons, takenSpots) {
  for (let i = 0; i < sensors.length; i++) {
    const sensor = sensors[i];
    const beacon = beacons[i];
    cave[sensor.y][sensor.x] = "S";
    cave[beacon.y][beacon.x] = "B";
    const radius =
      Math.abs(sensor.x - beacon.x) + Math.abs(sensor.y - beacon.y);
    drawShapeAroundInRadius(cave, sensor.x, sensor.y, radius, takenSpots);
  }
}

function paintCave(cave) {
  for (let y = 0; y < cave.length; y++) {
    const row = cave[y];
    let line = "";
    for (let x = 0; x < row.length; x++) {
      line += row[x];
    }
    console.log(line);
  }
}

function paintCaveToFile(cave) {
  const fs = require("fs");

  let content = "";
  for (let y = 0; y < cave.length; y++) {
    const row = cave[y];
    let line = "";
    for (let x = 0; x < row.length; x++) {
      line += row[x];
    }
    content += line + "\n";
  }

  fs.writeFile("cave.txt", content, function (err) {
    if (err) {
      return console.log(err);
    }
    console.log("The file was saved!");
  });
}

function calculateTakenSpotsAtY(y, takenSpots) {
  return takenSpots.filter((s) => s.y === y).length;
}

function main() {
  const {
    sensors,
    beacons,
    smallestX,
    smallestY,
    largestX,
    largestY,
    biggestOffset,
  } = parseInput();
  const cave = createCave(
    smallestX,
    smallestY,
    largestX,
    largestY,
    biggestOffset
  );
  const takenSpots = [];
  placeSensorsAndBeacons(cave, sensors, beacons, takenSpots);
  paintCave(cave);
  paintCaveToFile(cave);
  console.log(calculateTakenSpotsAtY(10 + biggestOffset, takenSpots));
}

main();
