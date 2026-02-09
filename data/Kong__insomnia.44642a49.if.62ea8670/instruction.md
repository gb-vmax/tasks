# Bug Report

### Describe the bug

After a recent update, the `removeWhere` function appears to have duplicate code that's causing syntax errors. The function definition seems to be malformed with code appearing both before and after the actual function declaration.

### Reproduction

When trying to use the database's `removeWhere` method, the application fails to start or compile due to a syntax error in the database module.

```js
// Attempting to remove documents matching a query
await database.removeWhere('request', { parentId: workspaceId });
```

The code in `packages/insomnia/src/common/database.ts` shows the `removeWhere` function has code defined outside of its body, followed by the function declaration itself, and then more code that looks like the original implementation.

### Expected behavior

The `removeWhere` function should be properly structured with a single, valid function body. It should successfully remove documents matching the given query along with their descendants.

### System Info
- Insomnia version: latest
- Node version: 18.x

---
Repository: /testbed
