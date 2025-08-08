class InvalidShapeException extends Error {
  constructor(message) {
    super(message);
    this.name = "InvalidShapeException";
  }
}

class NegativeDimensionException extends Error {
  constructor(message) {
    super(message);
    this.name = "NegativeDimensionException";
  }
}

function calculateRectangleArea(length, width) {
  if (typeof length !== "number" || typeof width !== "number") {
    throw new InvalidShapeException("无效的尺寸。长度和宽度必须是数字。");
  }
  if (length <= 0 || width <= 0) {
    throw new NegativeDimensionException("无效的尺寸。长度和宽度必须是正数。");
  }
  return length * width;
}

console.log(calculateRectangleArea(5, 4)); // 输出: 20
console.log(calculateRectangleArea("5", 4)); // 抛出InvalidShapeException
console.log(calculateRectangleArea(-5, 4)); // 抛出NegativeDimensionException