# Bug Report

### Describe the bug

I'm experiencing an issue with the response object where the `jsonBody` assertion seems to be incomplete or corrupted. When trying to use `expect(response).to.have.jsonBody()` in my pre-request or test scripts, the behavior is completely broken.

### Reproduction

```js
pm.test("Check JSON response", function() {
    const response = pm.response;
    
    // This should work but throws unexpected errors
    pm.expect(response).to.have.jsonBody({
        id: 123,
        name: "test"
    });
});
```

The response validation just fails without any clear error message or the assertion doesn't execute properly at all.

### Expected behavior

The `jsonBody` assertion should properly validate the response JSON body against the expected object. It should either pass when the JSON matches or fail with a clear error message indicating what didn't match.

### Additional context

This seems to have broken recently. The code for handling JSON body assertions appears to be cut off or malformed - it looks like there might have been an incomplete refactoring or merge conflict that wasn't resolved properly. The assertion chain just stops working after trying to use `jsonBody`.

---
Repository: /testbed
