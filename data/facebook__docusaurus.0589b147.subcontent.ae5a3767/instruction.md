# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where line breaks in nested content (like lists or blockquotes) are being handled incorrectly. The parser seems to be calculating positions/offsets wrong, which causes content to be misaligned or merged together when it shouldn't be.

### Reproduction

```js
const markdown = `
- First item with
  multiple lines
  
- Second item
`;

const result = remark.parse(markdown);
// The output shows incorrect positioning/structure
```

When parsing markdown with multi-line list items or nested structures that contain line breaks, the resulting AST has incorrect position information. This affects any downstream processing that relies on accurate source positions.

### Expected behavior

The parser should correctly track line breaks and position offsets in nested content structures. Each line break should be accounted for properly in the position calculations.

### Additional context

This seems to affect specifically the subcontent processing logic where void tokens with line breaks are involved. The issue manifests when there are multiple nested structures with breaks between them.

---
Repository: /testbed
