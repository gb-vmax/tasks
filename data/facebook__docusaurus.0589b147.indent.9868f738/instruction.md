# Bug Report

### Describe the bug

The `indent` function is not properly indenting strings that contain newlines. When a multi-line string is passed to the function, only the lines after the first newline get indented, but the first line and subsequent lines are missing the proper indentation.

### Reproduction

```js
const str = `line1
line2
line3`;

const indented = indent(str);
console.log(indented);

// Current output:
// line1
//   line2
//   line3

// Expected output:
//   line1
//   line2
//   line3
```

### Expected behavior

All lines in the string should be indented by 2 spaces, including the first line. The function should add proper indentation to the beginning of the string and after each newline character.

### Additional context

This affects route generation where multi-line strings need consistent indentation for proper code formatting. The generated output currently has inconsistent indentation which could cause issues with code structure.

---
Repository: /testbed
