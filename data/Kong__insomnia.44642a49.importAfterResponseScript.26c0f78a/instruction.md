# Bug Report

### Describe the bug

When importing Postman collections, the after-response scripts (test scripts) are not being imported correctly. Instead of importing the test event scripts, it appears that the wrong event type is being processed, and only the first line of multi-line scripts is being captured.

### Reproduction

1. Create a Postman collection with a request that has a test script (after-response event)
2. Add a multi-line test script, for example:
```js
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});
pm.test("Response time is less than 200ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(200);
});
```
3. Export the collection and import it into Insomnia
4. The test script is either missing or incomplete

### Expected behavior

All test scripts (after-response scripts) should be imported completely with all lines preserved. The test event listener should be processed correctly to capture the full script content.

### System Info
- Insomnia version: latest
- OS: Cross-platform issue

---
Repository: /testbed
