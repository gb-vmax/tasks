# Bug Report

### Describe the bug
After a recent update, nested environment variables are being flattened with dot notation instead of preserving their hierarchical structure. When I define environment variables with nested objects, they get converted to flattened keys like `parent.child.property` instead of maintaining the original nested object structure.

### Reproduction
```js
const env = new Environment('test', {
  database: {
    host: 'localhost',
    port: 5432,
    credentials: {
      username: 'admin',
      password: 'secret'
    }
  }
});

// Expected: env.get('database') should return the nested object
// Actual: Can only access via env.get('database.host'), env.get('database.port'), etc.
```

### Expected behavior
Environment variables should maintain their nested object structure. When I set a nested object in the environment, I should be able to retrieve it as a nested object, not as flattened dot-notation keys.

For example:
- `env.get('database')` should return `{ host: 'localhost', port: 5432, credentials: {...} }`
- Not require accessing each property individually via `database.host`, `database.port`, etc.

This breaks backward compatibility with existing scripts that rely on accessing nested environment objects.

### System Info
- insomnia-sdk version: latest
- Platform: All platforms

---
Repository: /testbed
