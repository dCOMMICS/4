const arr = ['shoes', 'clothes', 'shelter'];

// old and longer way //

let newArr = [...arr];

newArr[1] = 'car';

console.log(newArr); 

// ['shoes', 'car', 'shelter']; // clothes were replaced with car


// new and descent way of replcing

newArr = arr.with(1,'car');

console.log(newArr);
