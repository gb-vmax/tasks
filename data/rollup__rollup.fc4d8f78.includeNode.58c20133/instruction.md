# Bug Report

### Describe the bug

I'm experiencing an issue with arrow functions that have destructured parameters. When the arrow function contains destructured parameters (like objects or arrays), the bundler seems to be incorrectly handling them during tree-shaking, causing the destructured parameters to not be included properly in the output.

### Reproduction

```js
// Example with object destructuring
const handler = ({ value, label }) => {
  console.log(value, label);
};

// Example with array destructuring
const process = ([first, second]) => {
  return first + second;
};

// When bundled, the destructured parameters are not being processed correctly
```

### Expected behavior

Arrow functions with destructured parameters should be handled the same way as regular parameters. The destructuring patterns in the parameters should be included and processed correctly during bundling.

### Additional context

This seems to affect arrow functions specifically - regular function declarations with destructured parameters work fine. The issue appears to be related to how the AST nodes are being traversed or included during the bundling process.

---
Repository: /testbed
