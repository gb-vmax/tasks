# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX tokenizer where constructs with `resolveAll` are being added to the `resolveAllConstructs` array multiple times, causing duplicate processing. This seems to be affecting the parsing behavior.

### Reproduction

```js
// When a construct is processed multiple times with resolveAll defined
const construct = {
  resolveAll: function(events) {
    // This gets called multiple times for the same construct
    return events;
  }
}

// The construct gets added to resolveAllConstructs array repeatedly
// instead of being added only once
```

### Expected behavior

Constructs with `resolveAll` should only be added to the `resolveAllConstructs` array once, not every time `addResult` is called with that construct. The condition should check if the construct is NOT already in the array before adding it.

### Additional context

This is happening in the `addResult` function within the tokenizer. The logic for checking whether to add a construct to `resolveAllConstructs` appears to be inverted - it's adding constructs that are already in the array instead of adding constructs that aren't in the array yet.

---
Repository: /testbed
