# Bug Report

### Describe the bug

Magic comments in JSX/TSX code blocks are not being recognized properly. When using highlight comments like `// highlight-next-line` or `// highlight-start` in JSX/TSX files, they don't work as expected.

### Reproduction

```jsx
function MyComponent() {
  return (
    <div>
      {/* highlight-next-line */}
      <p>This should be highlighted</p>
    </div>
  );
}
```

The JSX-style comment `{/* highlight-next-line */}` is not being detected, even though it's the standard way to write comments in JSX code.

### Expected behavior

Magic comments in JSX/TSX code blocks should support JSX-style comments (`{/* */}`) in addition to regular JavaScript comments. The highlighted line should be properly marked when using JSX comment syntax.

### Additional context

This seems to affect both `jsx` and `tsx` language code blocks. Regular JS/TS files work fine with `//` style comments, but JSX files need the `{/* */}` syntax for comments within the JSX markup.

---
Repository: /testbed
