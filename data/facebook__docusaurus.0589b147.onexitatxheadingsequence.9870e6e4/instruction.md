# Bug Report

### Describe the bug

ATX heading depth is being calculated incorrectly when parsing markdown headings. The depth value appears to be off by one in certain cases, causing headings to render at the wrong level.

### Reproduction

```js
// Parse markdown with ATX headings
const markdown = `
## Level 2 Heading
### Level 3 Heading
#### Level 4 Heading
`;

// The parsed depth values don't match the actual heading levels
// Expected: depth 2, 3, 4
// Getting incorrect depth values
```

### Expected behavior

When parsing ATX headings (headings with `#` symbols), the depth should correctly correspond to the number of `#` characters:
- `#` should have depth 1
- `##` should have depth 2  
- `###` should have depth 3
- etc.

Currently the depth calculation seems to be producing incorrect values, particularly when the heading depth has already been set.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
