# Bug Report

### Describe the bug

I'm encountering an issue with the automock functionality where mock generation seems to be behaving incorrectly for certain field types. When generating mocks for protobuf messages, some fields are not being mocked properly and the recursion logic appears broken.

### Reproduction

```js
// When mocking a protobuf message with nested types
const schema = {
  fields: {
    nested: {
      type: 'SomeProtoType',
      resolvedType: { /* proto definition */ }
    }
  }
}

// The mock generation either:
// 1. Doesn't handle the nested type correctly
// 2. Gets stuck in infinite recursion
// 3. Returns unexpected values for scalar fields
```

### Expected behavior

The automock should correctly generate mock values for all field types including:
- Nested protobuf types
- Scalar fields that resolve to null
- Fields that need to be resolved recursively

The current behavior seems to have the logic inverted - it's processing fields when it shouldn't and skipping fields when it should process them.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
