# Bug Report

### Describe the bug
When using the `to.have.header` assertion in the response object, I'm getting a syntax error. It looks like there's a malformed code block in the response.ts file that's breaking the header validation functionality.

### Reproduction
```js
pm.test("Check response header", function () {
    pm.response.to.have.header('Content-Type');
});
```

When trying to use the header assertion, the code fails to parse properly. It seems like there's some incorrectly formatted code that got introduced recently.

### Expected behavior
The `to.have.header` assertion should work correctly for checking if a response contains a specific header. The code should compile and execute without syntax errors.

### Additional context
This appears to affect the basic header checking functionality. The issue seems to be in the response.ts file where the header validation logic is defined. The code structure looks broken with what appears to be a misplaced function definition inside the object literal.

---
Repository: /testbed
