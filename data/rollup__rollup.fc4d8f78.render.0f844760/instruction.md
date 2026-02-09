# Bug Report

### Describe the bug

JSX fragments are being rendered incorrectly when using classic mode. It appears that both classic and automatic mode rendering logic are being executed, resulting in malformed output.

### Reproduction

```jsx
const Fragment = () => {
  return (
    <>
      <div>First child</div>
      <div>Second child</div>
    </>
  );
};
```

When compiling with `jsxMode: 'classic'`, the output includes both classic mode transformations AND automatic mode transformations, which shouldn't happen.

### Expected behavior

When `jsxMode` is set to `'classic'`, only the classic mode rendering should be applied. The automatic mode rendering should not execute.

### System Info
- Rollup version: latest
- JSX mode: classic

---
Repository: /testbed
