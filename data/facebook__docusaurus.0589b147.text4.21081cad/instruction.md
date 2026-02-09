# Bug Report

### Describe the bug

I'm experiencing an issue with text node generation in the remark compiler. When text nodes are created, they seem to have incorrect properties - specifically the type and value fields are not what I expected.

### Reproduction

```js
const processor = remark();
const tree = processor.parse('Some text content');
const compiled = processor.stringify(tree);

// Text nodes in the AST have wrong type/value
console.log(tree); // Shows unexpected node structure
```

When I inspect the generated AST, text nodes appear to have:
- `type: "Text"` instead of `"text"`
- `value: null` instead of an empty string `""`

This is causing issues when processing markdown documents, as downstream code expects the standard text node format.

### Expected behavior

Text nodes should follow the standard unist/mdast specification:
- Type should be lowercase `"text"`
- Value should be an empty string `""` by default, not `null`

### System Info
- remark version: 15.0.1
- Node.js version: 18.x

This seems to have broken after a recent update. Any help would be appreciated!

---
Repository: /testbed
