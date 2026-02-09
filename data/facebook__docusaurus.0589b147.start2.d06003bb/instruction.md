# Bug Report

### Describe the bug

When using MDX with constructs that have the `partial` property set, the parser is incorrectly setting `context.currentConstruct`. The logic appears to be inverted - it's only setting the current construct when `construct.partial` is true, but it should be doing the opposite.

Additionally, when a construct name is disabled, the `nok` callback is being called with the construct name instead of the code point, which causes unexpected behavior in error handling.

### Reproduction

```js
// Create a parser with a non-partial construct
const construct = {
  name: 'myConstruct',
  partial: false,
  tokenize: function(effects, ok, nok) {
    // tokenize implementation
  }
}

// When this construct is processed, context.currentConstruct 
// is not being set because partial is false
// Expected: context.currentConstruct should be set for non-partial constructs
```

Also reproducible when a construct is disabled:

```js
// When a construct is in the disable list
// The nok callback receives the construct name instead of the code
// This breaks the expected callback signature
```

### Expected behavior

1. `context.currentConstruct` should be set when `construct.partial` is **false** (not true)
2. The `nok` callback should receive the `code2` parameter, not the `construct.name`

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
