# Bug Report

### Describe the bug

I'm experiencing an issue with `stripNumberPrefix` where it seems to be applying the number prefix parser twice on the filename, causing unexpected behavior when stripping number prefixes from file paths.

### Reproduction

```js
const parser = (str) => {
  // Simple parser that strips leading numbers and dash
  const match = str.match(/^(\d+)-(.+)$/);
  if (match) {
    return { filename: match[2] };
  }
  return { filename: str };
};

// This should return "myDoc" but returns something unexpected
const result = stripNumberPrefix("001-myDoc", parser);
console.log(result); // Expected: "myDoc"
```

When the parser is called on a string like `"001-myDoc"`, the function appears to be processing the result multiple times instead of just once, leading to incorrect output.

### Expected behavior

The `stripNumberPrefix` function should call the parser once on the input string and return the stripped filename. For example:
- Input: `"001-myDoc"` → Expected output: `"myDoc"`
- Input: `"05-myFolder"` → Expected output: `"myFolder"`

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
