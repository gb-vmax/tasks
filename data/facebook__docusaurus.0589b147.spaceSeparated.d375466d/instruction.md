# Bug Report

### Describe the bug

I'm experiencing an issue with space-separated attribute values in MDX components. When passing arrays or strings with multiple spaces to attributes that expect space-separated values, the output has inconsistent spacing.

### Reproduction

```js
// Example 1: Array input
const classList = ['btn', 'btn-primary', 'active'];
// Expected: "btn btn-primary active"
// Getting: inconsistent spacing with extra spaces

// Example 2: String input with multiple spaces
const classes = "header   main    footer";
// Expected: "header main footer" (normalized single spaces)
// Getting: double spaces between some words
```

When I pass these values to MDX components, the spacing in the rendered output doesn't match what I expect. Sometimes there are extra spaces, and the normalization seems inconsistent.

### Expected behavior

Space-separated values should be consistently normalized to single spaces between items, regardless of whether the input is an array or a string with multiple spaces.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
