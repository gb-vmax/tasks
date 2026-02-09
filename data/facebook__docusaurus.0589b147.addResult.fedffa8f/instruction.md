# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where certain constructs are being processed incorrectly. It appears that some events are being duplicated or not properly resolved when parsing markdown content with nested or complex structures.

### Reproduction

```js
const parser = createParser();
const result = parser.parse(`
# Heading

Some text with **bold** and *italic*.

- List item 1
- List item 2
`);

// The parsed events contain duplicates or incorrect structure
console.log(result.events);
```

When parsing markdown with multiple formatting constructs (like bold, italic, lists), the resulting event stream seems to have extra events or missing events compared to what's expected.

### Expected behavior

The parser should generate a clean event stream where each construct is resolved exactly once and all events are properly ordered without duplicates.

### Additional context

This seems to affect documents with multiple nested constructs. Simple documents parse fine, but once you add combinations of formatting (bold + italic, lists with formatted text, etc.), the event stream gets corrupted.

---
Repository: /testbed
