# Bug Report

### Describe the bug

I'm encountering an issue with ATX heading parsing in markdown. When parsing headings with `#` symbols (ATX-style headings), the depth property is not being set correctly on the heading nodes.

### Reproduction

```js
const markdown = `
# Heading 1
## Heading 2
### Heading 3
`;

// Parse the markdown
const result = remark().parse(markdown);

// Expected: heading nodes should have depth: 1, 2, 3
// Actual: depth property is undefined or incorrect
console.log(result.children[0].depth); // undefined or wrong value
console.log(result.children[1].depth); // undefined or wrong value
console.log(result.children[2].depth); // undefined or wrong value
```

### Expected behavior

When parsing ATX-style headings (lines starting with `#`), the resulting AST nodes should have a `depth` property that matches the number of `#` symbols. For example:
- `# Heading` should produce a node with `depth: 1`
- `## Heading` should produce a node with `depth: 2`
- `### Heading` should produce a node with `depth: 3`

Currently, the depth property is either not being set or has an incorrect value.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
