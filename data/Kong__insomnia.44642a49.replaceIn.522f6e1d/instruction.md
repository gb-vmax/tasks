# Bug Report

### Describe the bug
The `replaceIn` method on the `Environment` class appears to be missing or broken. When trying to use template string interpolation with environment variables, the method is not available or throws an error.

### Reproduction
```js
const env = new Environment();
env.set('baseUrl', 'https://api.example.com');
env.set('apiKey', 'secret123');

// This fails - replaceIn method is not working
const result = env.replaceIn('{{baseUrl}}/users?key={{apiKey}}');
```

### Expected behavior
The `replaceIn` method should interpolate environment variables into the template string and return something like:
```
https://api.example.com/users?key=secret123
```

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
