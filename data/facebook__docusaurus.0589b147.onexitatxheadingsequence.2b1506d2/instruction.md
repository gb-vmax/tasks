# Bug Report

### Describe the bug

ATX headings (headings using `#` syntax) are not being parsed correctly. The depth calculation appears to be off, and headings are either not being recognized or assigned the wrong level.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

// Parse a simple heading
const ast = processor.parse('## Heading Level 2');

console.log(ast.children[0].depth);
// Expected: 2
// Actual: incorrect depth value
```

Also happens with other heading levels:

```markdown
# Level 1
### Level 3
#### Level 4
```

The depth property on the heading nodes doesn't match the actual number of `#` characters used.

### Expected behavior

The `depth` property of ATX heading nodes should correctly reflect the heading level (number of `#` characters). For example:
- `#` should have depth 1
- `##` should have depth 2
- `###` should have depth 3
- etc.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
