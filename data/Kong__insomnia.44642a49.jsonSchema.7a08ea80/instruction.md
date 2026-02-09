# Bug Report

### Describe the bug

There appears to be a syntax error in the response validation code that's breaking the SDK. When trying to use response assertions, I'm getting unexpected behavior or errors.

### Reproduction

```js
pm.test("Validate response", function () {
    pm.response.to.not.have.jsonSchema({
        type: "object",
        properties: {
            id: { type: "number" }
        }
    });
});
```

When running this, the code doesn't execute properly. It seems like there's a structural issue in the response object's assertion methods.

### Expected behavior

The `jsonSchema` validation should work correctly with the `not` negation, and the response object should be properly structured without syntax errors.

### Additional context

This seems to have been introduced recently. The code structure around the response assertions looks malformed - there's a function definition (`formatSchemaErrors`) appearing in the middle of an object literal, which would cause parsing issues.

---
Repository: /testbed
