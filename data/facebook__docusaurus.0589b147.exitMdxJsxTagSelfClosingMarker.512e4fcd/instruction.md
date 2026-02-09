# Bug Report

### Describe the bug

Self-closing JSX tags in MDX are not being recognized correctly. When using self-closing syntax like `<Component />`, the parser doesn't properly mark the tag as self-closing, which causes rendering issues.

### Reproduction

```jsx
// This self-closing tag is not parsed correctly
<MyComponent />

// Expected to be recognized as self-closing
<Image src="test.jpg" />
```

After parsing, these tags are not being flagged with `selfClosing: true` in the AST, even though they use the self-closing syntax.

### Expected behavior

Self-closing JSX tags should be properly identified and marked with the `selfClosing` property set to `true` in the parsed output. This is necessary for correct rendering and transformation of MDX content.

### System Info
- remark-mdx version: 3.0.0

---
Repository: /testbed
