# Bug Report

### Describe the bug

I'm encountering a syntax error in the Response object when trying to use the `to.have.jsonSchema()` assertion. It appears that the code structure for the `jsonSchema` method got corrupted or improperly formatted during a recent update.

### Reproduction

```js
pm.test("Response matches JSON schema", function() {
    pm.response.to.have.jsonSchema({
        type: "object",
        properties: {
            name: { type: "string" }
        }
    });
});
```

When running this test, the script fails to execute properly. The assertion methods seem to be malformed in the response object.

### Expected behavior

The `jsonSchema` assertion should work correctly and validate the response body against the provided JSON schema. The method should be properly defined within the assertion chain.

### Additional context

This appears to affect the structure of the response assertions. The code for handling JSON schema validation looks like it might have been accidentally broken during refactoring - the function definitions seem to be in the wrong place or the object structure is incomplete.

---
Repository: /testbed
