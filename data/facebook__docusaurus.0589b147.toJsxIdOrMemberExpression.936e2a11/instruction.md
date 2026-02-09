# Bug Report

### Describe the bug

I'm encountering an issue with JSX member expressions when using nested component references. The component hierarchy seems to be inverted or incorrectly constructed when dealing with namespaced/member components.

### Reproduction

```js
// When trying to use a nested JSX component like:
<Foo.Bar.Baz />

// The resulting member expression structure appears to be incorrect
// Expected: Foo.Bar.Baz
// Actual: Only the first identifier is used, or the nesting is reversed
```

For example, if I have a component structure like `UI.Button.Primary`, the JSX transformation doesn't properly chain the member expressions together.

### Expected behavior

JSX member expressions should be properly nested from left to right. For a component reference like `A.B.C`, it should create a structure where:
- `A` is the base object
- `B` is accessed as a member of `A`
- `C` is accessed as a member of `A.B`

### System Info
- @mdx-js/mdx version: 3.0.0

This seems to affect any JSX code that uses dotted component names. Let me know if you need more details to reproduce this!

---
Repository: /testbed
