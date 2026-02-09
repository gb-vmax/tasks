# Bug Report

### Describe the bug

I'm encountering an issue with ATX heading parsing where the heading depth is being calculated incorrectly. When parsing markdown headings (the ones with `#` symbols), the depth value seems to be off by one.

### Reproduction

```js
const markdown = `
# Heading 1
## Heading 2
### Heading 3
`;

// Parse the markdown
const result = remark.parse(markdown);

// The heading depths are incorrect:
// - "# Heading 1" is parsed with depth 0 instead of 1
// - "## Heading 2" is parsed with depth 1 instead of 2
// - "### Heading 3" is parsed with depth 2 instead of 3
```

### Expected behavior

ATX headings should have their depth property set correctly based on the number of `#` symbols:
- `#` should have depth 1
- `##` should have depth 2
- `###` should have depth 3
- etc.

Currently, all heading depths appear to be off by one, making them unusable for generating proper heading hierarchies or table of contents.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
