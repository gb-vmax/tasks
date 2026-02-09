# Bug Report

### Describe the bug
When using `to.not.have.jsonSchema()` in the response assertions, I'm getting a syntax error. It looks like there's an issue with the code structure - the assertion method is not properly integrated into the response object.

### Reproduction
```js
pm.test("Response validation", function () {
    pm.response.to.not.have.jsonSchema({
        type: "object",
        properties: {
            name: { type: "string" }
        }
    });
});
```

### Expected behavior
The negative assertion should work without throwing a syntax error. The code should properly validate that the response does NOT match the given JSON schema.

### System Info
- Insomnia SDK version: latest
- Node version: 18.x

The positive assertion `pm.response.to.have.jsonSchema()` seems to work fine, but when trying to use the negative form with `to.not.have.jsonSchema()`, the test runner fails to parse the code properly.

---
Repository: /testbed
