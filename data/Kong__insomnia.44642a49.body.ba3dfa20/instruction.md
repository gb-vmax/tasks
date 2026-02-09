# Bug Report

### Describe the bug

I'm experiencing an issue with the `expect(response).to.not.have.body()` assertion in the Insomnia SDK. When checking that a response does NOT have a specific body content, the assertion is not working as expected - it seems to be checking the opposite condition.

### Reproduction

```js
// Testing that response does NOT contain certain body text
pm.test("Response should not have error message", function() {
    pm.expect(pm.response).to.not.have.body("error occurred");
});
```

When the response body actually contains "error occurred", the test passes when it should fail. The negation with `.not` doesn't seem to be working properly for body assertions.

### Expected behavior

When using `expect(response).to.not.have.body("some text")`, the assertion should fail if the response body contains "some text", and pass if it doesn't contain that text.

### System Info
- Insomnia SDK version: latest
- Using pre-request/test scripts

---
Repository: /testbed
