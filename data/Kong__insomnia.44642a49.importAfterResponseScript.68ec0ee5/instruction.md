# Bug Report

### Describe the bug

When importing Postman collections, after-response scripts (test scripts) are not being imported correctly. It appears that the importer is looking for the wrong event type, causing test scripts to be completely missing from the imported requests.

### Reproduction

1. Create a Postman collection with a request that has a test script (after-response script)
2. Add some test code in the "Tests" tab in Postman:
```js
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});
```
3. Export the collection from Postman
4. Import the collection into Insomnia
5. Check the imported request - the test script is missing

### Expected behavior

The test scripts from Postman should be imported and available in the after-response script section of the request. The importer should correctly identify and extract scripts from the `test` event listener in the Postman collection format.

### Additional context

This seems to affect all requests with test scripts. Pre-request scripts might be working fine, but the after-response/test scripts are not being picked up during import.

---
Repository: /testbed
