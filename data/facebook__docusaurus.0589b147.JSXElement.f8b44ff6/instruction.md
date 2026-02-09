# Bug Report

### Describe the bug

The ESLint rule `string-literal-i18n-messages` is now incorrectly flagging non-`Translate` JSX elements as violations when they contain non-text children. The rule seems to have inverted its logic - it's checking the wrong elements and reporting errors on components that shouldn't be validated at all.

### Reproduction

```jsx
// This should NOT trigger an error but now does
<div>
  <span>Hello</span>
  {someVariable}
</div>

// This SHOULD trigger an error but now doesn't
<Translate>
  <span>Hello</span>
  {someVariable}
</Translate>
```

The rule is now checking all JSX elements EXCEPT `Translate` components, which is the opposite of what it should do. Regular JSX elements like `div`, `span`, etc. are being reported as violations when they have mixed children, while actual `Translate` components are being ignored.

### Expected behavior

The rule should only validate `Translate` components and ignore all other JSX elements. Non-text children should only be flagged as errors when they appear inside `Translate` components, not in regular HTML/JSX elements.

### System Info
- Package: @docusaurus/eslint-plugin

---
Repository: /testbed
