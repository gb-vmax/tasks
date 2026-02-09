# Bug Report

### Describe the bug

I'm encountering an issue with markdown rendering where strong/bold text is not being formatted correctly. When I use double asterisks or double underscores to create bold text, the output is malformed.

### Reproduction

```js
const markdown = '**bold text**';
// Expected output: **bold text**
// Actual output: *bold text* (or similar incorrect format)
```

Also happens with underscores:
```js
const markdown = '__bold text__';
// Not rendering with proper bold markers
```

### Expected behavior

Bold text should be properly wrapped with double markers (`**` or `__`) on both sides. The opening and closing markers should match the input format.

### Additional context

This seems to affect all instances of strong/bold text formatting. Regular emphasis (single asterisk/underscore) appears to work fine, but the double marker syntax is broken.

---
Repository: /testbed
