# Bug Report

### Describe the bug

ATX heading depth is being set incorrectly when parsing markdown. The heading level appears to be calculated based on the wrong value, resulting in all headings potentially having the same depth value instead of reflecting the actual number of `#` characters.

### Reproduction

```js
const remark = require('remark');
const markdown = `
# Heading 1
## Heading 2
### Heading 3
`;

const ast = remark.parse(markdown);
console.log(ast.children[0].depth); // Expected: 1
console.log(ast.children[1].depth); // Expected: 2
console.log(ast.children[2].depth); // Expected: 3
```

### Expected behavior

Each heading node should have a `depth` property that corresponds to the number of `#` characters:
- `#` should have depth 1
- `##` should have depth 2
- `###` should have depth 3
- etc.

### Actual behavior

The depth values are not being calculated correctly based on the heading sequence tokens.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
