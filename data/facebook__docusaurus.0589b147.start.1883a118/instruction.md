# Bug Report

### Describe the bug

I'm experiencing an issue with HTML text parsing in markdown content. When processing inline HTML, the parser seems to be creating duplicate or malformed token structures that cause unexpected behavior in the output.

### Reproduction

```js
const markdown = `Some text with <span>inline HTML</span> content`;

// Process the markdown
const result = remark().parse(markdown);

// The HTML text tokens appear to be incorrectly structured
console.log(result);
```

### Expected behavior

The HTML text should be tokenized correctly with proper entry/exit pairs for `htmlTextData`. Currently it seems like the token structure is broken, possibly with duplicate entries that don't have corresponding exits.

### Additional context

This appears to affect any markdown content that includes inline HTML tags. The parser enters the `htmlTextData` state but the token tree structure doesn't look right when inspecting the output.

---
Repository: /testbed
