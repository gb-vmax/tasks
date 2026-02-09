# Bug Report

### Describe the bug

When using JSX with text nodes that contain only whitespace, the output is not being properly serialized. The text content appears to be rendered without JSON stringification, which causes invalid JavaScript output.

### Reproduction

```jsx
const element = (
  <div>
    {/* Text node with whitespace that gets normalized to empty string */}
    
  </div>
);
```

When the JSX text node contains whitespace that gets normalized away (trimmed and merged), the resulting output is not properly quoted as a string literal. This leads to syntax errors in the generated code.

### Expected behavior

All JSX text nodes should be properly JSON-stringified in the output when not in preserve mode, even when they normalize to empty strings. The current behavior seems to skip the stringification step in certain cases.

### System Info
- Rollup version: latest
- JSX mode: automatic/classic (non-preserve)

---
Repository: /testbed
