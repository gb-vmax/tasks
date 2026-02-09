# Bug Report

### Describe the bug

I'm experiencing an issue with lazy line detection in markdown parsing. It appears that lazy continuation lines are being incorrectly identified, causing the parser to treat certain lines as lazy when they shouldn't be (or vice versa).

### Reproduction

```js
const remark = require('remark');

const markdown = `
> quote line 1
  continuation line
> quote line 3
`;

const result = remark.parse(markdown);
// The continuation line is incorrectly parsed
```

When parsing blockquotes or other containers with continuation lines, the lazy line detection seems inverted - lines that should be treated as lazy continuations are not being recognized correctly, and lines that shouldn't be lazy are being marked as such.

### Expected behavior

The parser should correctly identify lazy continuation lines based on whether we're still within the same container depth. Continuation lines should be properly associated with their parent containers.

### Additional context

This seems to affect how the parser tracks container state and line offsets. The issue manifests when parsing multi-line containers like blockquotes, lists, or other nested structures where lazy continuation is relevant.

---
Repository: /testbed
