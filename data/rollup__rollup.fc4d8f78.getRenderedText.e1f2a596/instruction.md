# Bug Report

### Describe the bug

JSX text content is not being rendered correctly when it contains whitespace. The whitespace handling seems to be broken - text that should have spaces between words is getting merged incorrectly, and leading/trailing whitespace is being handled in the wrong order.

### Reproduction

```jsx
const element = <div>
  Hello   World
</div>

// Expected output: "Hello World"
// Actual output: Text is processed incorrectly
```

Another example:
```jsx
const element = <span>  Text with spaces  </span>

// The whitespace trimming and merging appears to happen in the wrong sequence
```

### Expected behavior

JSX text nodes should:
1. First merge consecutive whitespace into single spaces
2. Then trim leading/trailing whitespace

The text should be normalized properly so that multiple spaces become single spaces, and any leading or trailing whitespace is removed correctly.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
