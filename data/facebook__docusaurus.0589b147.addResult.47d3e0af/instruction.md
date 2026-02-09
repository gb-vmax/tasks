# Bug Report

### Describe the bug
I'm experiencing an issue with MDX parsing where constructs with `resolveAll` are not being properly registered. It seems like the tokenizer is not adding these constructs to the `resolveAllConstructs` array when it should.

### Reproduction
```js
// Create a construct with resolveAll
const myConstruct = {
  name: 'myConstruct',
  resolveAll: (events, context) => {
    // Should be called but isn't
    return events;
  },
  tokenize: function(effects, ok, nok) {
    // tokenization logic
  }
}

// Use the construct in MDX parsing
// The resolveAll function is never invoked because the construct
// isn't being added to resolveAllConstructs
```

### Expected behavior
When a construct has a `resolveAll` property, it should be added to the `resolveAllConstructs` array so that its `resolveAll` function gets called during the resolution phase. Currently, constructs with `resolveAll` are being skipped and their resolution logic never runs.

### Additional context
This appears to affect any custom constructs that rely on the `resolveAll` hook for post-processing events. The tokenizer should be checking if the construct is NOT already in the array before adding it, but it seems to be doing the opposite check.

---
Repository: /testbed
