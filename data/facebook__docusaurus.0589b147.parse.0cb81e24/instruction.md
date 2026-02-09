# Bug Report

### Describe the bug

I'm encountering an issue with the `parse()` method in the remark processor. When parsing markdown content, the arguments passed to the parser function appear to be in the wrong order, causing unexpected behavior.

### Reproduction

```js
const processor = remark();
const file = 'Hello **world**!';

// Parsing fails or produces incorrect results
const tree = processor.parse(file);
```

The parser seems to be receiving arguments in an unexpected order. When I inspect what's being passed to custom parsers, the file object and string content are swapped compared to what the parser expects.

### Expected behavior

The parser should receive the string content as the first argument and the file object as the second argument, allowing it to correctly parse the markdown and generate the syntax tree.

### System Info
- remark version: 15.0.1
- Node version: Latest

This seems to have broken after a recent update. The parser is likely expecting `(string, file)` but receiving `(file, string)` instead.

---
Repository: /testbed
