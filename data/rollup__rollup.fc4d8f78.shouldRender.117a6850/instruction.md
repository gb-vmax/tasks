# Bug Report

### Describe the bug

JSX text nodes containing only whitespace or empty strings are not being rendered correctly. When a JSX text node has content that evaluates to an empty string (`""`), it's being treated as if it should not render, but it should actually be rendered as it's a valid string value.

### Reproduction

```jsx
const Component = () => {
  return (
    <div>
      {/* Empty string should be rendered */}
      {""}
      <span>test</span>
    </div>
  );
};
```

The empty string text node is not being included in the output even though it's a valid value that should be rendered.

### Expected behavior

Empty strings (`""`) should be rendered as they are valid string values. The current behavior seems to be treating empty strings the same as `null` or `undefined`, but they should be distinguished - empty strings are valid content while `null`/`undefined` should not render.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
