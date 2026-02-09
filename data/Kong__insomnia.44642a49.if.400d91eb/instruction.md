# Bug Report

### Describe the bug

I'm experiencing an issue with gRPC automocking where proto types are not being properly detected. When trying to generate mock data for protobuf messages, the type checking logic seems to be inverted, causing the automock functionality to fail silently or produce incorrect results.

### Reproduction

```js
// Define a protobuf message with nested types
const myProtoType = {
  fieldsArray: [
    { name: 'field1', type: 'string' },
    { name: 'field2', type: 'int32' }
  ]
}

// Try to generate mock data
const mockData = generateMockFromProto(myProtoType)

// Expected: Mock data should be generated
// Actual: Type is not recognized as a valid proto type
```

When the automock tries to validate proto types, it incorrectly identifies valid Type objects as non-proto types, preventing mock generation from working properly.

### Expected behavior

The `isProtoType` function should correctly identify valid protobuf Type objects and return `true` when a valid type is passed in. Mock data should be generated successfully for valid proto definitions.

### System Info
- Insomnia version: latest
- OS: macOS

This seems to have started recently and is blocking our ability to use the automock feature for gRPC testing.

---
Repository: /testbed
