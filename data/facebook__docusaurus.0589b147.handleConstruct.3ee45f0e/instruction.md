# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where constructs with `partial: true` are not being handled correctly. It seems like the logic for setting `context.currentConstruct` has been inverted - now it's only being set when `construct.partial` is true, but it should be set when it's NOT partial.

Additionally, there appears to be a problem with how context and fields are being merged when creating the tokenize context. The order of arguments in `Object.assign(Object.create(...), ...)` seems backwards, which could cause fields to not be properly inherited.

### Reproduction

```js
// When processing a non-partial construct
const construct = {
  name: 'myConstruct',
  partial: false,
  tokenize: function(effects, ok, nok) {
    // ... tokenizer logic
  }
}

// The context.currentConstruct is not being set correctly
// This breaks constructs that rely on checking the current construct state
```

### Expected behavior

1. When `construct.partial` is false (or undefined), `context.currentConstruct` should be set to the construct
2. When `construct.partial` is true, `context.currentConstruct` should NOT be modified
3. Fields should be properly merged with the context prototype chain so that field properties take precedence

### System Info
- Package: @mdx-js/mdx@3.0.0
- Node version: Latest

This is causing parsing failures for certain MDX documents that worked previously. Any help would be appreciated!

---
Repository: /testbed
