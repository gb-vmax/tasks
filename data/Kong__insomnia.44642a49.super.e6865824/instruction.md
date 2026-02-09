# Bug Report

### Describe the bug

I'm encountering a syntax error when trying to use the RequestAuth class. The code appears to be malformed and won't compile/run properly.

### Reproduction

```js
const auth = new RequestAuth({
  type: 'basic',
  basic: [
    { key: 'username', value: 'testuser' },
    { key: 'password', value: 'testpass' }
  ]
});
```

When I try to create a RequestAuth instance with valid auth options, I get an error. The class seems to be broken and can't be instantiated at all.

### Expected behavior

The RequestAuth constructor should successfully create an instance when provided with valid authentication options. The code should compile and execute without syntax errors.

### System Info
- insomnia-sdk version: latest
- Node.js version: 18.x

---
Repository: /testbed
