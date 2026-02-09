# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where brace contexts are not being handled correctly. It seems like the parser is returning the wrong context level when checking brace types, which causes unexpected parsing behavior for JSX expressions and object literals.

### Reproduction

When parsing MDX content with nested braces or JSX expressions, the parser appears to be looking at the wrong context level. This affects how braces are interpreted - whether they should be treated as block statements, object literals, or JSX expression containers.

```mdx
export const config = {
  title: 'Test'
}

<Component prop={{ nested: 'value' }} />
```

The parser seems to be checking the parent context incorrectly, leading to misidentification of brace types in certain scenarios.

### Expected behavior

The parser should correctly identify the current context by looking at the appropriate level in the context stack. Braces should be properly classified based on their actual parent context, not an incorrect offset in the context array.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This appears to be related to how the context stack is being accessed in the `curContext()` method. The wrong array index is being used to retrieve the current parsing context.

---
Repository: /testbed
