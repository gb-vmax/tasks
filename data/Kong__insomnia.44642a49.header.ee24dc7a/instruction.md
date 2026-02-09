# Bug Report

### Describe the bug

I'm encountering a syntax error in the response object code. It looks like there's some malformed code in the `not.have.header` section that's preventing the SDK from working properly.

When trying to use response assertions with `.not.have.header()`, the code fails to execute due to what appears to be a parsing issue in the response.ts file.

### Reproduction

```js
const response = pm.response;

// This should work but throws an error
pm.expect(response).to.not.have.header('X-Custom-Header');
```

The error occurs when trying to use any negative header assertions. It seems like there's corrupted or misplaced code in the response object implementation.

### Expected behavior

The `.not.have.header()` assertion should work correctly and verify that a specific header is not present in the response.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
