class Circle {

    static pi = Math.PI;

    constructor(radius) {
        this.radius = radius;
    }

    static createCircle(radius) {
        return new Circle(radius);
    }

    gerArea() {
        return Circle.pi * this.radius ** 2;
    }

    getCircumference() {
        return 2 * Circle.pi * this.radius;
    }

    toString() {
        return `Circle with radius ${this.radius}`;
    }
}

const circle = Circle.createCircle(10);
const circleArea = circle.gerArea();
const circleCircumference = circle.getCircumference();
const circleString = circle.toString();

console.log(circleArea);
console.log(circleCircumference);
console.log(circleString);