const input = `Sensor at x=2150774, y=3136587: closest beacon is at x=2561642, y=2914773
Sensor at x=3983829, y=2469869: closest beacon is at x=3665790, y=2180751
Sensor at x=2237598, y=3361: closest beacon is at x=1780972, y=230594
Sensor at x=1872170, y=78941: closest beacon is at x=1780972, y=230594
Sensor at x=3444410, y=3965835: closest beacon is at x=3516124, y=3802509
Sensor at x=3231566, y=690357: closest beacon is at x=2765025, y=1851710
Sensor at x=3277640, y=2292194: closest beacon is at x=3665790, y=2180751
Sensor at x=135769, y=50772: closest beacon is at x=1780972, y=230594
Sensor at x=29576, y=1865177: closest beacon is at x=255250, y=2000000
Sensor at x=3567617, y=3020368: closest beacon is at x=3516124, y=3802509
Sensor at x=1774477, y=148095: closest beacon is at x=1780972, y=230594
Sensor at x=1807041, y=359900: closest beacon is at x=1780972, y=230594
Sensor at x=1699781, y=420687: closest beacon is at x=1780972, y=230594
Sensor at x=2867703, y=3669544: closest beacon is at x=3516124, y=3802509
Sensor at x=1448060, y=201395: closest beacon is at x=1780972, y=230594
Sensor at x=3692914, y=3987880: closest beacon is at x=3516124, y=3802509
Sensor at x=3536880, y=3916422: closest beacon is at x=3516124, y=3802509
Sensor at x=2348489, y=2489095: closest beacon is at x=2561642, y=2914773
Sensor at x=990761, y=2771300: closest beacon is at x=255250, y=2000000
Sensor at x=1608040, y=280476: closest beacon is at x=1780972, y=230594
Sensor at x=2206669, y=1386195: closest beacon is at x=2765025, y=1851710
Sensor at x=3932320, y=3765626: closest beacon is at x=3516124, y=3802509
Sensor at x=777553, y=1030378: closest beacon is at x=255250, y=2000000
Sensor at x=1844904, y=279512: closest beacon is at x=1780972, y=230594
Sensor at x=2003315, y=204713: closest beacon is at x=1780972, y=230594
Sensor at x=2858315, y=2327227: closest beacon is at x=2765025, y=1851710
Sensor at x=3924483, y=1797070: closest beacon is at x=3665790, y=2180751
Sensor at x=1572227, y=3984898: closest beacon is at x=1566446, y=4774401
Sensor at x=1511706, y=1797308: closest beacon is at x=2765025, y=1851710
Sensor at x=79663, y=2162372: closest beacon is at x=255250, y=2000000
Sensor at x=3791701, y=2077777: closest beacon is at x=3665790, y=2180751
Sensor at x=2172093, y=3779847: closest beacon is at x=2561642, y=2914773
Sensor at x=2950352, y=2883992: closest beacon is at x=2561642, y=2914773
Sensor at x=3629602, y=3854760: closest beacon is at x=3516124, y=3802509
Sensor at x=474030, y=3469506: closest beacon is at x=-452614, y=3558516`;

function parseInput() {
  const sensors = [];
  const beacons = [];

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

    sensors.push({
      x: sensorX,
      y: sensorY,
    });

    beacons.push({
      x: beaconX,
      y: beaconY,
    });
  }

  return {
    sensors,
    beacons,
  };
}

const y = 2000000;

function calcDistance(a, b) {
  return Math.abs(a.x - b.x) + Math.abs(a.y - b.y);
}

function addSpecialPossitions(specialPossitions, inputs) {
  for (let i = 0; i < inputs.length; i++) {
    specialPossitions.add(`${inputs[i].x},${inputs[i].y}`);
  }
}

function mapImpossiblePositions(specialPositions, sensors, beacons) {
  const impossiblePositions = new Set();
  for (let i = 0; i < sensors.length; i++) {
    const sensor = sensors[i];
    const beacon = beacons[i];
    let distance = calcDistance(sensor, beacon) + 1;
    let yOffset = Math.abs(y - sensor.y);

    for (let j = 0; j < distance - yOffset; j++) {
      if (!specialPositions.has(`${sensor.x + j},${y}`)) {
        impossiblePositions.add(`${sensor.x + j},${y}`);
      }
      if (!specialPositions.has(`${sensor.x - j},${y}`)) {
        impossiblePositions.add(`${sensor.x - j},${y}`);
      }
    }
  }

  return impossiblePositions;
}

function main() {
  const { sensors, beacons } = parseInput();
  const specialPossitions = new Set();
  addSpecialPossitions(specialPossitions, sensors);
  addSpecialPossitions(specialPossitions, beacons);
  const impossiblePositions = mapImpossiblePositions(
    specialPossitions,
    sensors,
    beacons
  );

  console.log(impossiblePositions.size);
}

main();
