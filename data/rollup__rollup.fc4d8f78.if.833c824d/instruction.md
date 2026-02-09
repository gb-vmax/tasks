# Bug Report

### Describe the bug

When removing annotations from code, I'm getting an error where the code tries to access an undefined annotation. It seems like the loop is going out of bounds when iterating through the annotations array.

### Reproduction

```js
const node = {
  annotations: [
    { start: 0, end: 10 },
    { start: 15, end: 25 },
    { start: 30, end: 40 }
  ]
}

// Call removeAnnotations
node.removeAnnotations(code)
// Error: Cannot read property 'start' of undefined
```

### Expected behavior

All annotations should be removed without throwing an error. The loop should iterate through each annotation correctly and remove them from the code.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
