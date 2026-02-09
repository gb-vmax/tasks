# Bug Report

### Describe the bug

I'm experiencing an issue with entity parsing where the output is not being captured correctly. When parsing text containing HTML entities, the parsed result appears to be empty or incorrect.

### Reproduction

```js
const result = parseEntities('Hello &amp; world', {
  text: (value, position) => {
    console.log('Text:', value);
  }
});

// Expected: result contains "Hello & world"
// Actual: result is empty or missing the parsed content
```

The text callback is being called but with an empty string instead of the actual parsed content. It seems like the internal queue is being cleared before it's added to the result.

### Expected behavior

The `parseEntities` function should return the correctly parsed text with HTML entities decoded. The text callback should receive the actual content that was queued up, not an empty string.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
