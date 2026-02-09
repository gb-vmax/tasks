# Bug Report

### Describe the bug

When updating request objects, the `update()` function appears to have duplicate code blocks that causes syntax errors. The function definition is duplicated and the control flow logic for checking request types is broken, leading to unreachable code.

### Reproduction

```ts
import { update } from './request-operations';

const grpcRequest = {
  _id: 'req_1',
  type: 'GrpcRequest',
  name: 'Test Request'
};

// Attempting to update a request
await update(grpcRequest, { name: 'Updated Name' });
```

### Expected behavior

The `update()` function should properly handle updates for all request types (GrpcRequest, WebSocketRequest, and regular Request) without syntax errors or unreachable code.

### System Info

- Insomnia version: latest
- Node version: 18.x

The function definition appears twice in the file and there's unreachable code after the return statements. This seems to have been introduced in a recent change to add patch sanitization logic.

---
Repository: /testbed
