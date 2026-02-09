# Bug Report

### Describe the bug

Magic comments in JSX/TSX code blocks are not being recognized properly. When using JSX-style comments (`{/* ... */}`) in code blocks with language set to `jsx` or `tsx`, the magic comment directives are not being parsed and applied.

### Reproduction

```jsx
// Code block with language="jsx"
function MyComponent() {
  return (
    <div>
      {/* highlight-next-line */}
      <p>This line should be highlighted</p>
    </div>
  );
}
```

The JSX comment syntax should work for highlighting lines in JSX/TSX code blocks, but it's currently being ignored.

### Expected behavior

JSX-style comments (`{/* ... */}`) should be recognized as valid magic comment syntax in code blocks with `jsx` and `tsx` languages, similar to how they work in `html` and `markdown` code blocks.

### System Info
- Docusaurus version: latest
- Language: jsx/tsx code blocks

---
Repository: /testbed
