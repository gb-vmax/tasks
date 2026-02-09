# Bug Report

### Describe the bug

I'm experiencing an issue with JSX expression containers when using JSX transform modes other than `preserve`. The code generation seems to be removing the wrong parts of the source code, resulting in corrupted output.

### Reproduction

```jsx
const element = <div>{someExpression}</div>
```

When transpiling with JSX mode set to anything other than `preserve`, the output is malformed. It appears that the closing brace `}` and potentially other parts of the expression container are being removed incorrectly.

### Expected behavior

The JSX expression container should be properly unwrapped, removing only the curly braces `{` and `}` while preserving the expression itself. The generated code should be valid JavaScript.

### System Info
- Rollup version: latest
- JSX mode: automatic (also happens with classic)

Has anyone else encountered this? The issue seems to have appeared recently.

---
Repository: /testbed
