# Bug Report

### Describe the bug

I'm experiencing an issue with gRPC service definitions where message type definitions are incorrectly being treated as service definitions. This causes the application to attempt processing message types as if they were service definitions, leading to unexpected behavior when working with gRPC proto files.

### Reproduction

```js
// When loading a proto file with both message and service definitions
const protoFile = `
  message UserRequest {
    string name = 1;
  }
  
  service UserService {
    rpc GetUser (UserRequest) returns (UserResponse);
  }
`;

// Message definitions are incorrectly identified as service definitions
// This causes issues when trying to enumerate actual services
```

### Steps to reproduce:
1. Load a proto file containing message type definitions
2. Attempt to filter/identify service definitions
3. Message types are not properly filtered out and are treated as services

### Expected behavior

Message type definitions should be properly distinguished from service definitions. Only actual service definitions should be processed as services, while message types should be filtered out correctly.

### System Info
- Insomnia version: latest
- OS: Any

---
Repository: /testbed
