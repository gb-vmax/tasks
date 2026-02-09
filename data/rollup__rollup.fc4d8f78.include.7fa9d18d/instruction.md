# Bug Report

### Describe the bug

Arrow function parameters are not being handled correctly during tree-shaking. When using destructuring or other non-identifier parameters in arrow functions, they seem to be getting dropped from the output bundle.

### Reproduction

```js
// Input code
const fn = ({ x, y }) => {
  console.log(x, y);
};

fn({ x: 1, y: 2 });
```

When this gets bundled, the destructured parameters are missing from the output, causing the function to not work as expected.

Also noticed this happens with:
- Array destructuring: `([a, b]) => a + b`
- Rest parameters: `(...args) => args.length`
- Default parameters with objects: `({ x = 5 }) => x`

### Expected behavior

All arrow function parameters, regardless of their pattern type (destructuring, rest, defaults, etc.), should be included in the bundled output.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
