# Bug Report

### Describe the bug

After updating to the latest version, the response body assertion is failing when checking if the body does NOT contain certain text. The `to.not.have.body()` assertion seems to be broken.

### Reproduction

```js
const response = {
  text: () => "Hello World"
}

// This throws an error even though the body doesn't contain "Goodbye"
expect(response).to.not.have.body("Goodbye")
```

When the response body is "Hello World" and I assert that it should NOT have the body "Goodbye", it's throwing an error instead of passing. The assertion logic appears to be inverted.

### Expected behavior

The `to.not.have.body()` assertion should pass when the response body does NOT match the expected value. Currently it seems to fail in this scenario.

### System Info
- SDK version: latest
- Node version: 18.x

---
Repository: /testbed
