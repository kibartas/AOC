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

const alphabet = "abcdefghijklmnopqrstuvwxyz";

function mapElevations() {
  const result = [];
  let startingPoint = {
    x: 0,
    y: 0,
    elevation: 0,
  };
  let endPoint = null;
  const lines = input.split("\n");
  for (let i = 0; i < lines.length; i++) {
    for (let j = 0; j < lines[i].length; j++) {
      const point = lines[i][j];
      if (point === "E") {
        endPoint = {
          x: j,
          y: i,
          elevation: 26,
        };
        result.push(endPoint);
      } else {
        const elevation = alphabet.indexOf(point) + 1;
        result.push({
          x: j,
          y: i,
          elevation,
        });
      }
    }
  }

  return [result, startingPoint, endPoint];
}

function isClimable(currentPoint, destination) {
  return currentPoint.elevation - destination.elevation >= -1;
}

function isVisited(visitedPoints, point) {
  return visitedPoints.find(
    (visitedPoint) => visitedPoint.x === point.x && visitedPoint.y === point.y
  );
}

function findAllAvailableDestinations(elevations, currentPoint, visitedPoints) {
  const result = [];
  const { x, y } = currentPoint;
  const availablePoints = [
    { x: x - 1, y },
    { x: x + 1, y },
    { x, y: y - 1 },
    { x, y: y + 1 },
  ];
  for (const point of availablePoints) {
    const elevation = elevations.find(
      (elevation) => elevation.x === point.x && elevation.y === point.y
    );
    if (
      elevation &&
      isClimable(currentPoint, elevation) &&
      !isVisited(visitedPoints, elevation)
    ) {
      result.push(elevation);
    }
  }
  return result;
}

function orderDestinationsByProximityToEndPoint(
  availableDestinations,
  endPoint
) {
  return availableDestinations.sort((a, b) => {
    const aProximity = calculateProximity(a, endPoint);
    const bProximity = calculateProximity(b, endPoint);
    return aProximity - bProximity;
  });
}

function calculateProximity(currentPoint, endPoint) {
  return (
    Math.abs(currentPoint.x - endPoint.x) +
    Math.abs(currentPoint.y - endPoint.y)
  );
}

const allPaths = [];
let currentClosestPath = null;
function findAllPaths(elevations, currentPoint, endPoint, visitedPoints) {
  const availableDestinations = findAllAvailableDestinations(
    elevations,
    currentPoint,
    visitedPoints
  );
  if (
    currentClosestPath === null ||
    calculateProximity(currentPoint, endPoint) <
      calculateProximity(currentClosestPath, endPoint)
  ) {
    currentClosestPath = currentPoint;
  }
  for (const destination of orderDestinationsByProximityToEndPoint(
    availableDestinations,
    endPoint
  )) {
    if (destination.x === endPoint.x && destination.y === endPoint.y) {
      visitedPoints.push(destination);
      allPaths.push(visitedPoints);
      console.log(allPaths);
    } else {
      const newVisitedPoints = [...visitedPoints, destination];
      const currentShortestPath = findShortestRoute();
      console.log(calculateProximity(destination, endPoint));
      if (!currentShortestPath) {
        findAllPaths(elevations, destination, endPoint, newVisitedPoints);
      } else {
        if (newVisitedPoints.length < currentShortestPath.length) {
          findAllPaths(elevations, destination, endPoint, newVisitedPoints);
        }
      }
    }
  }
}

function findShortestRoute() {
  let shortestRoute = null;
  for (const path of allPaths) {
    if (!shortestRoute) {
      shortestRoute = path;
    } else {
      if (path.length < shortestRoute.length) {
        shortestRoute = path;
      }
    }
  }
  return shortestRoute;
}

function main() {
  const [elevations, startingPoint, endPoint] = mapElevations(input);
  let currentPoint = startingPoint;
  console.log(endPoint);
  findAllPaths(elevations, currentPoint, endPoint, []);
  console.log(findShortestRoute().length);
}

main();
