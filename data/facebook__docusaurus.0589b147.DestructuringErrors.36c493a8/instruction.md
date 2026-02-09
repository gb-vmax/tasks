# Bug Report

### Describe the bug

I'm encountering an issue with parsing MDX files that contain destructuring patterns. It seems like the parser is incorrectly handling certain destructuring syntax, leading to unexpected parsing behavior.

### Reproduction

```jsx
// This MDX code fails to parse correctly
export const { a, b } = props;

function Component({ x, y }) {
  return <div>{x + y}</div>
}
```

When I try to use destructuring in MDX files, the parser doesn't handle it properly. This appears to be related to how the parser tracks destructuring errors internally.

### Expected behavior

The parser should correctly handle destructuring patterns in both export statements and function parameters without throwing errors or misidentifying syntax issues.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
