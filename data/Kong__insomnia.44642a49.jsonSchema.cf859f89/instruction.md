# Bug Report

### Describe the bug

The response schema validation is broken after a recent update. When trying to validate a response against a JSON schema, I'm getting syntax errors and the validation doesn't work at all.

### Reproduction

```js
const response = pm.response;

// This throws an error now
pm.test("Response matches schema", function() {
    pm.expect(response).to.have.jsonSchema({
        type: "object",
        properties: {
            name: { type: "string" }
        }
    });
});
```

The code just fails to execute properly. It looks like there's a syntax issue in the response validation code itself.

### Expected behavior

The schema validation should work as before - validating the response body against the provided JSON schema and throwing appropriate errors if the schema doesn't match.

### Additional context

This was working fine in the previous version. The issue appeared after the latest update. The validation function seems to have been modified but something went wrong with the code structure.

---
Repository: /testbed
