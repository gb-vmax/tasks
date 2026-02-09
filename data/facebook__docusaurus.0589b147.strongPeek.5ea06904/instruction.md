# Bug Report

### Describe the bug

When using markdown rendering with strong/bold text, the output is incorrect when the `strong` option is not set or is falsy. Instead of falling back to the default `*` delimiter, it appears to be using an empty string or unexpected value.

### Reproduction

```js
const state = {
  options: {
    // strong option not set or set to falsy value
    strong: null
  }
};

// Rendering bold text should fall back to default delimiter
// but instead produces incorrect output
```

### Expected behavior

When the `strong` option is not defined or is falsy, the markdown renderer should fall back to using `*` as the default delimiter for strong/bold text. The peek function should return the configured delimiter or the default `*` character.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
