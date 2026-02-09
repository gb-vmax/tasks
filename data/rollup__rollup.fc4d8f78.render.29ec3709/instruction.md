# Bug Report

### Describe the bug

When using JSX with `jsx.mode: 'preserve'`, the expression container braces `{}` are being incorrectly removed from the output. The expressions themselves are preserved, but the surrounding braces that indicate them as JSX expressions are stripped out, which breaks the JSX syntax.

### Reproduction

```jsx
// Input JSX
const element = <div>{someVariable}</div>;

// With jsx.mode: 'preserve', expected output:
<div>{someVariable}</div>

// Actual output (braces removed):
<div>someVariable</div>
```

This appears to affect all JSX expression containers when preserve mode is enabled. The expressions are rendered but the `{` and `}` delimiters are removed, resulting in invalid JSX output.

### Expected behavior

When `jsx.mode` is set to `'preserve'`, the entire JSX syntax including expression container braces should be preserved in the output. Only when the mode is set to transform modes (like `'automatic'` or `'classic'`) should the braces be removed as part of the transformation process.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
