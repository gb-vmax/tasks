# Bug Report

### Describe the bug
When using JSX with `jsx.mode` set to `'preserve'`, the closing tags are being incorrectly transformed. Instead of preserving the original JSX syntax, the closing tags appear to be replaced with unexpected characters.

### Reproduction
```jsx
// Input JSX code with jsx.mode: 'preserve'
const element = <div>Hello</div>

// Expected output: JSX should be preserved as-is
// Actual output: Closing tag is transformed incorrectly
```

### Steps to reproduce:
1. Configure rollup with JSX mode set to `'preserve'`
2. Write a component with JSX closing tags
3. Build the project
4. Observe that closing tags are not preserved correctly

### Expected behavior
When `jsx.mode` is set to `'preserve'`, the JSX syntax should remain unchanged in the output, including both opening and closing tags.

### System Info
- Rollup version: latest
- jsx.mode: 'preserve'

---
Repository: /testbed
