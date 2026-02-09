# Bug Report

### Describe the bug

I'm encountering an issue where constructs that should be disabled are still being processed instead of being rejected. It seems like the disable check is inverted - constructs are only rejected when they're NOT in the disable list, which is the opposite of what should happen.

### Reproduction

```js
const parser = {
  constructs: {
    disable: {
      null: ['someConstruct']
    }
  }
}

const context = {
  parser: parser,
  currentConstruct: null
}

// When processing a construct named 'someConstruct'
// Expected: construct should be rejected (nok called)
// Actual: construct is allowed to proceed
```

### Expected behavior

When a construct's name is included in `context.parser.constructs.disable.null`, it should be rejected and the `nok` callback should be called. Currently, it appears to do the opposite - only rejecting constructs that are NOT in the disable list.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
