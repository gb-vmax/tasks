# Bug Report

### Describe the bug

After a recent update, the `jsonSchema` expectation method is not working as expected. When trying to validate response bodies against JSON schemas, the validation appears to be broken or not functioning at all.

### Reproduction

```js
pm.test("Response matches schema", function () {
    pm.response.to.have.jsonSchema({
        type: "object",
        properties: {
            id: { type: "number" },
            name: { type: "string" }
        },
        required: ["id", "name"]
    });
});
```

The test fails to validate even when the response body matches the schema correctly. It seems like the schema validation logic got disrupted.

### Expected behavior

The `jsonSchema` method should validate the response body against the provided JSON schema and pass when the structure matches.

### Additional context

This was working fine in previous versions. The issue started appearing after some recent changes to the response validation code. Other validation methods like `have.body` and `have.header` still work correctly, so it's specifically related to JSON schema validation.

---
Repository: /testbed
