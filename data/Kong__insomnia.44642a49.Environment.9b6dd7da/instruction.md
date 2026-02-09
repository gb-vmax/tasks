# Bug Report

### Describe the bug

I'm encountering a syntax error when trying to use the environment variable management features. The application fails to start or load properly, and I'm seeing errors related to the environments module.

### Reproduction

```js
const env = new Environment('test-env', {});

// Trying to set a variable
env.set('API_KEY', 'my-secret-key');

// Application crashes or fails to load
```

### Expected behavior

The Environment class should work correctly and allow setting/unsetting variables without any errors. The module should load and execute without syntax issues.

### Additional context

This seems to have started happening recently. The environment variable operations were working fine before, but now the entire module appears to be broken. I can't even import the Environment class without running into problems.

The issue appears to be in the `packages/insomnia-sdk/src/objects/environments.ts` file, but I'm not sure what's causing it. It looks like there might be some incomplete code or malformed syntax somewhere in the file.

---
Repository: /testbed
