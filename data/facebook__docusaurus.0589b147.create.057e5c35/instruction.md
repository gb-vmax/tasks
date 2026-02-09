# Bug Report

### Describe the bug

The `no-untranslated-text` ESLint rule is not catching untranslated text in JSX elements as expected. It seems like the rule is only triggering on `<Translate>` components instead of flagging other components that contain untranslated text.

### Reproduction

```jsx
// This should be flagged but isn't
<div>Hello World</div>

// This should be flagged but isn't
<span>Some untranslated text</span>

// Only this seems to trigger the rule now
<Translate>Text here</Translate>
```

The rule appears to have inverted logic - it's only checking elements that ARE `<Translate>` components rather than checking everything EXCEPT `<Translate>` components.

### Expected behavior

The rule should flag any JSX element containing untranslated text strings, except when the element is already wrapped in a `<Translate>` component (which handles translation).

### Additional context

Also noticing some odd behavior with JSX fragments - the rule doesn't seem to be triggering correctly when fragments contain mixed content (text + other elements).

---
Repository: /testbed
