"use strict";

/**
 * @param {string} val
 * @return {Object}
 */

val = 5;
val2 = 5;

var expect = function expect(val) {
  return {
    toBe: function toBe(val2) {
      if (val === val2) return true;else throw new Error("Not Equal");
    },
    notToBe: function notToBe(val2) {
      if (val !== val2) return true;else throw new Error("Equal");
    }
  };
};

try {
  console.log(expect(val).toBe(val2)); // This will either log true or throw an error if val !== val2
} catch (error) {
  console.error(error.message); // This will catch and log the error message if the above condition fails
}

try {
  console.log(expect(val).notToBe(val2)); // This will either log true or throw an error if val === val2
} catch (error) {
  console.error(error.message); // This will catch and log the error message if the above condition fails
}
/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */