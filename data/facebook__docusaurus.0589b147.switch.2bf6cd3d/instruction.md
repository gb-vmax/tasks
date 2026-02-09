# Bug Report

### Describe the bug

Magic comments in JSX/TSX code blocks are not being recognized properly. When using comment directives like `highlight-next-line` or `highlight-start` in JSX/TSX files, they don't work as expected.

### Reproduction

```jsx
function MyComponent() {
  return (
    <div>
      {/* highlight-next-line */}
      <p>This line should be highlighted</p>
    </div>
  );
}
```

The JSX-style comments (`{/* ... */}`) are not being parsed correctly, so the highlighting directive is ignored.

### Expected behavior

Magic comments in JSX/TSX code blocks should work the same way they do in regular JavaScript code blocks. Both `//` style comments and `{/* */}` JSX comments should be recognized for highlighting and other directives.

### System Info
- Docusaurus version: latest
- Language: JSX/TSX code blocks

This seems to have started recently. Regular JS files work fine, but JSX/TSX files don't pick up the magic comments anymore.

---
Repository: /testbed
