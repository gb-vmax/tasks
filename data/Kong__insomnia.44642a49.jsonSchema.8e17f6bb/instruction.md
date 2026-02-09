# Bug Report

### Describe the bug
When using `to.have.jsonSchema()` in response assertions, the validation is not working as expected. It seems like the schema validation logic has changed and is now behaving differently than before.

### Reproduction
```js
pm.test("Response should match JSON schema", function() {
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

When running this test against a valid response that matches the schema, the assertion behaves unexpectedly. The schema validation doesn't seem to be processing the schema object correctly.

### Expected behavior
The `to.have.jsonSchema()` assertion should validate the response body against the provided JSON schema and pass when the response matches the schema structure.

### System Info
- Insomnia SDK version: latest
- Using pre-request/test scripts

---
Repository: /testbed
