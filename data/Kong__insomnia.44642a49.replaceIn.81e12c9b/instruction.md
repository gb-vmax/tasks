# Bug Report

### Describe the bug

The `replaceIn` method in the Variables class is not working correctly. When trying to use template interpolation with variables, I'm getting an error because the method is calling `render` on the wrong object.

### Reproduction

```js
const variables = new Variables();
variables.set('apiUrl', 'https://api.example.com');
variables.set('endpoint', '/users');

// This should interpolate the variables into the template
const result = variables.replaceIn('{{ apiUrl }}{{ endpoint }}');
// Expected: 'https://api.example.com/users'
// Actual: TypeError - context.render is not a function
```

### Expected behavior

The `replaceIn` method should properly interpolate variables into the template string and return the rendered result. Instead, it's trying to call a `render` method on the context object which doesn't exist.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
