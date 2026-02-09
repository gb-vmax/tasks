# Bug Report

### Describe the bug

The error indicator (caret `^`) in code frames is appearing at the wrong column position. When an error occurs in source code, the visual indicator that points to the exact error location is offset and doesn't align with the actual column where the error occurred.

### Reproduction

```js
// When generating a code frame for an error at line 5, column 10
const source = `
function test() {
  const x = 1;
  const y = 2;
  const z = x + y;
}
`;

const frame = getCodeFrame(source, 5, 10);
console.log(frame);

// The caret (^) appears at the wrong position
// instead of pointing directly under the character at column 10
```

### Expected behavior

The error indicator should appear directly beneath the column number specified, pointing to the exact location of the error in the source code. Currently it's misaligned and makes it difficult to identify where the actual error is.

### Additional context

This affects error reporting and makes debugging more difficult since the visual indicator doesn't match the actual error location. The frame itself displays the correct lines, but the positioning of the `^` character is off.

---
Repository: /testbed
