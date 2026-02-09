# Bug Report

### Describe the bug

I'm encountering an issue with bold/strong text rendering in markdown. When I use double asterisks or double underscores to create bold text, the output is incorrect - it seems like the strong elements are not being processed properly.

### Reproduction

```js
const markdown = '**bold text**';
const result = remark().processSync(markdown);
// Expected: strong node with text children
// Actual: incorrect node type or structure
```

Also happens with:
```markdown
This is __bold text__ in a sentence.
```

### Expected behavior

Bold text should be parsed into proper `strong` nodes with the text content as children. The AST should contain a node with `type: "strong"` and an array of child nodes.

### System Info
- remark version: 15.0.1
- Node version: 18.x

The bold text appears to be parsed but the resulting node structure seems wrong. This is breaking downstream processing that expects standard strong nodes.

---
Repository: /testbed
