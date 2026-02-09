# Bug Report

### Describe the bug

After a recent update, MDX code generation is producing malformed output with missing whitespace and content. The generated code appears to be trimmed incorrectly, causing syntax errors and breaking the build.

### Reproduction

When compiling MDX files with code blocks or inline expressions, the output is getting trimmed in unexpected ways:

```jsx
// Input MDX
export const value = 42;

function Component() {
  return <div>Hello World</div>
}
```

The generated output loses important whitespace between statements and may skip duplicate content that should actually appear multiple times in the output.

### Expected behavior

The MDX compiler should preserve all code content including whitespace and newlines as needed for valid JavaScript/JSX output. If the same code fragment needs to be written multiple times (e.g., for different parts of the component), it should appear multiple times in the output.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This is breaking our documentation site build. Any help would be appreciated!

---
Repository: /testbed
