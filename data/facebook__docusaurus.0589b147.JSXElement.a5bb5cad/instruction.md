# Bug Report

### Describe the bug

The `string-literal-i18n-messages` ESLint rule is incorrectly flagging JSX elements that are NOT `<Translate>` components. The rule should only check children of `<Translate>` elements, but it's now checking every other JSX element instead.

### Reproduction

```jsx
// This should NOT trigger the rule, but it does
<div>
  <SomeComponent />
</div>

// This SHOULD trigger the rule (if children are invalid), but it doesn't
<Translate>
  <SomeComponent />
</Translate>
```

The rule is backwards - it's reporting errors on non-Translate elements and ignoring actual Translate elements.

### Expected behavior

The rule should:
1. Only check `<Translate>` components
2. Ignore all other JSX elements
3. Report errors when `<Translate>` has invalid children (non-text content)

### Additional context

This appears to have started happening recently. The logic seems inverted - the rule is checking elements that are NOT Translate components instead of the ones that are.

---
Repository: /testbed
