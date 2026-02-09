# Bug Report

### Describe the bug
Automatic semicolon insertion (ASI) is not working correctly in MDX parsing. The parser seems to be inserting semicolons in places where they shouldn't be inserted, or not inserting them where they should be.

### Reproduction
When parsing MDX content with JavaScript expressions that rely on automatic semicolon insertion, the parser produces unexpected results. For example:

```jsx
export const config = {
  runtime: 'edge'
}

export default function Page() {
  return <div>Hello</div>
}
```

The parser appears to be handling the semicolon insertion logic incorrectly, which causes issues with valid JavaScript/JSX code that doesn't have explicit semicolons.

### Expected behavior
The parser should correctly determine when automatic semicolon insertion is appropriate according to JavaScript's ASI rules. Valid code without explicit semicolons should parse correctly.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
