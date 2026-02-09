# Bug Report

### Describe the bug

After a recent update, I'm encountering issues with parsing MDX content that contains closing parentheses or braces. The parser seems to be failing or behaving incorrectly when it encounters these characters, particularly in JSX expressions.

### Reproduction

```jsx
const Component = () => {
  return (
    <div>
      {someFunction()}
    </div>
  )
}
```

When trying to parse MDX content with code like above, the parser doesn't handle the closing parentheses and braces correctly. It appears that the context tracking for these tokens is broken.

### Expected behavior

The MDX parser should correctly handle closing parentheses (`)`) and closing braces (`}`) in JSX expressions and update the parsing context appropriately. The parser should be able to distinguish between expression contexts and statement contexts when encountering these closing tokens.

### Additional context

This seems to have started happening after some changes to the remark-mdx vendor file. The issue specifically affects the `updateContext` handling for `parenR` and `braceR` token types.

---
Repository: /testbed
