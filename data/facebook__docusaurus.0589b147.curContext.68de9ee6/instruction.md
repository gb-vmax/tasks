# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where brace handling seems to be broken. When parsing certain MDX code blocks, braces that should be treated as object literals are being incorrectly interpreted as block statements (or vice versa).

### Reproduction

```jsx
const Component = () => {
  return (
    <div>
      {/* Object literal in JSX expression */}
      {someFunction({ key: 'value' })}
    </div>
  )
}
```

The parser appears to be incorrectly determining the context for braces, leading to syntax errors or unexpected parsing behavior. This affects MDX documents that use object literals within JSX expressions.

### Expected behavior

The parser should correctly distinguish between:
- Braces used for block statements
- Braces used for object literals

Object literals passed as arguments or used in expressions should be parsed correctly without throwing errors.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest LTS

This seems to have started happening recently and is blocking our ability to parse valid MDX documents. Any help would be appreciated!

---
Repository: /testbed
