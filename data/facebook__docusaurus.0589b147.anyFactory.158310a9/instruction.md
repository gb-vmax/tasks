# Bug Report

### Describe the bug

I'm experiencing an issue with the `remark` parser where condition matching seems to be inverted. When I use multiple test conditions with what should be an "any" matcher (OR logic), it's behaving like "none" or inverted logic instead.

### Reproduction

```js
const unified = require('unified');
const remarkParse = require('remark-parse');
const { is } = require('unist-util-is');

const processor = unified().use(remarkParse);

const tree = processor.parse('# Hello\n\nWorld');

// Try to find nodes matching ANY of these conditions
const matcher = (node) => {
  return is(node, 'heading') || is(node, 'paragraph');
};

// The matching logic seems inverted - nodes that SHOULD match are not being found
// and nodes that shouldn't match ARE being found
```

### Expected behavior

When using OR conditions (any of multiple tests should pass), nodes matching at least one condition should be selected. Currently it seems like the logic is backwards - it's only returning true when nodes DON'T match any of the conditions.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This is causing issues in my markdown processing pipeline where I need to select nodes based on multiple possible types. The behavior changed recently and I'm not sure if this is a regression or if I'm misunderstanding something about how the matchers are supposed to work.

---
Repository: /testbed
