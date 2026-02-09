# Bug Report

### Describe the bug

When using JSX fragments with a custom factory (classic JSX runtime), the output is incorrectly duplicating the factory name in the generated code. The factory variable name appears twice in the output, causing invalid JavaScript.

### Reproduction

```jsx
/** @jsx h */
/** @jsxFrag h.Fragment */

function App() {
  return (
    <>
      <div>Content</div>
    </>
  );
}
```

With a custom JSX factory like `React.createElement` or `h.Fragment`, the generated output includes the factory name twice, resulting in something like:

```js
/*#__PURE__*/React.React.createElement.Fragment(...)
```

instead of the expected:

```js
/*#__PURE__*/React.createElement.Fragment(...)
```

### Expected behavior

The factory variable should only appear once in the generated code. For a factory like `React.createElement`, it should output `React.createElement(...)` not `React.React.createElement(...)`.

### System Info
- Rollup version: latest
- JSX pragma: custom factory

This seems to have started happening recently. The classic JSX runtime mode is affected but automatic mode works fine.

---
Repository: /testbed
