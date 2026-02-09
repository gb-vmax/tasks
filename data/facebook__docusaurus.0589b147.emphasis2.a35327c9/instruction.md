# Bug Report

### Describe the bug

I'm experiencing an issue with markdown emphasis rendering. When trying to use italic text (emphasis), the output is showing as bold (strong) instead. This is affecting all emphasized text in my markdown documents.

### Reproduction

```js
// Parse markdown with emphasis
const markdown = '*italic text*';
const result = parse(markdown);

// Expected: { type: "emphasis", children: [...] }
// Actual: { type: "strong" }
```

When processing markdown that should render as italic/emphasized text, the parser is incorrectly creating strong (bold) nodes instead of emphasis nodes.

### Expected behavior

Text wrapped in single asterisks or underscores should be rendered as emphasized/italic text, not bold. The AST node should have type `"emphasis"` with a `children` property containing the text content.

### Additional context

This seems to affect all emphasis syntax in markdown files. Bold text (double asterisks) still works correctly, but single asterisk emphasis is broken.

---
Repository: /testbed
