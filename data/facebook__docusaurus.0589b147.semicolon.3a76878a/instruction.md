# Bug Report

### Describe the bug

I'm encountering unexpected parsing errors when working with MDX files. The parser is throwing "Unexpected token" errors for valid JavaScript/MDX syntax that should be accepted.

### Reproduction

```jsx
const Component = () => {
  return <div>Hello</div>;
};

export default Component;
```

When parsing this valid MDX content, the parser incorrectly reports an unexpected token error even though the syntax is completely valid. The semicolons after statements are being treated as syntax errors when they shouldn't be.

### Expected behavior

The parser should accept valid JavaScript syntax with semicolons without throwing unexpected token errors. Semicolons are valid statement terminators and should be parsed correctly.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
