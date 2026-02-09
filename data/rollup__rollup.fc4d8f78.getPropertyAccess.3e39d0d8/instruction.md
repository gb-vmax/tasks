# Bug Report

### Describe the bug

I'm experiencing an issue with property access generation in code snippets. When generating code for object property access, the output is incorrect for properties that contain special characters or spaces.

### Reproduction

```js
// For a property name like "user-id" or "first name"
const propertyName = "user-id";

// Expected output: ["user-id"]
// Actual output: .user-id (which is invalid JavaScript)
```

Similarly, for valid property names:

```js
// For a property name like "userId"
const propertyName = "userId";

// Expected output: .userId
// Actual output: [userId] (missing quotes, which is invalid)
```

### Expected behavior

- Valid property names (like `userId`, `name`, etc.) should use dot notation: `.userId`
- Invalid property names (like `user-id`, `first name`, etc.) should use bracket notation with proper quoting: `["user-id"]`

The generated code snippets are currently producing invalid JavaScript syntax.

### System Info
- Latest version from main branch

---
Repository: /testbed
