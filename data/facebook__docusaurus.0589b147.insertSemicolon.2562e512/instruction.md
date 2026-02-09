# Bug Report

### Describe the bug

I'm encountering a parsing error when working with JSX/MDX code that should allow automatic semicolon insertion (ASI). The parser is now throwing unexpected errors for valid JavaScript code where semicolons should be automatically inserted.

### Reproduction

```jsx
const Component = () => {
  return (
    <div>
      {someValue}
    </div>
  )
}
```

When parsing MDX content with expressions that rely on ASI, the parser incorrectly rejects valid code. This happens specifically in cases where:
1. There's a line break after a statement
2. The next token is a closing brace
3. No explicit semicolon is present

### Expected behavior

The parser should automatically insert semicolons according to JavaScript ASI rules. Code that was previously valid should continue to parse without errors.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This seems to have broken after a recent update. The same MDX files that parsed successfully before are now failing.

---
Repository: /testbed
