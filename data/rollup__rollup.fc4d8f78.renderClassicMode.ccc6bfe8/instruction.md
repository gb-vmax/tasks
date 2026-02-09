# Bug Report

### Describe the bug

When using JSX fragments with a custom JSX factory that has nested properties (e.g., `React.createElement`), the generated code is incorrect. The factory variable name is being duplicated in the output, causing runtime errors.

### Reproduction

```jsx
/** @jsx React.createElement */
/** @jsxFrag React.Fragment */

const fragment = (
  <>
    <div>Hello</div>
    <div>World</div>
  </>
);
```

### Expected behavior

The compiled output should correctly reference the JSX factory without duplication. For a factory like `React.createElement`, it should generate something like:
```js
React.createElement(React.Fragment, null, ...)
```

### Actual behavior

The factory variable appears to be included twice in the generated code, resulting in invalid JavaScript that fails at runtime.

### System Info
- Rollup version: latest
- JSX pragma: Custom factory with nested properties

---
Repository: /testbed
