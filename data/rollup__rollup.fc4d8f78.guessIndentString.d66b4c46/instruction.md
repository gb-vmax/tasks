# Bug Report

### Describe the bug

The automatic indentation detection is not working correctly when analyzing source code. When I have code that uses spaces for indentation, the detected indent string is incorrect - it seems to be using the maximum number of spaces found instead of the minimum.

### Reproduction

```js
const code = `
function test() {
  const x = 1;
    const y = 2;
}
`;

// The guessed indent should be 2 spaces (the minimum indentation level)
// but it's returning 4 spaces instead
```

When processing code with mixed indentation levels (like 2 spaces and 4 spaces), the indent detection picks the largest spacing instead of the smallest common denominator. This causes issues when trying to maintain consistent formatting.

### Expected behavior

The indentation detection should identify the minimum number of spaces used for indentation, not the maximum. In code with 2-space and 4-space indents, it should detect 2 spaces as the base indent level.

### Additional context

This seems to have changed recently. The detection used to work correctly and would find the smallest indent unit, but now it's doing the opposite.

---
Repository: /testbed
