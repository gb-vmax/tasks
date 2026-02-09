# Bug Report

### Describe the bug

When creating a new gRPC request, the initialization is now setting default values that weren't there before. The request is being initialized with a pre-populated URL and metadata headers, which is unexpected behavior.

### Reproduction

```js
// Create a new gRPC request
const newRequest = init();

// Expected: url should be empty string
// Actual: url is set to 'https://buf.build'
console.log(newRequest.url); // outputs 'https://buf.build'

// Expected: metadata should be empty array
// Actual: metadata contains pre-populated headers
console.log(newRequest.metadata); 
// outputs:
// [
//   { name: 'content-type', value: 'application/grpc', ... },
//   { name: 'user-agent', value: 'grpc-insomnia-client', ... }
// ]
```

### Expected behavior

When initializing a new gRPC request:
- The `url` field should be an empty string `''`
- The `metadata` array should be empty `[]`

This allows users to start with a clean slate when creating new requests.

### Additional context

This seems to have changed recently. The initialization is now inferring a default URL from the reflection API module and adding default metadata headers automatically. This breaks existing workflows where we expect new requests to have no pre-filled values.

---
Repository: /testbed
