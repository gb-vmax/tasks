# Bug Report

### Describe the bug

After a recent update, the application seems to have syntax issues that prevent it from running properly. When trying to execute requests with plugins, I'm encountering unexpected behavior or errors related to the plugin hook execution.

### Reproduction

The issue appears when:
1. Setting up a request with plugin hooks enabled
2. Attempting to execute the request
3. The application fails to process the request correctly

It looks like there might be some code structure problems in the HAR processing module. The request plugin hooks aren't being applied as expected.

### Expected behavior

Plugin hooks should execute normally and the request should be processed without any structural errors in the code.

### Additional context

This started happening after the latest changes. The code doesn't seem to be properly structured - there appears to be duplicate function definitions or misplaced code blocks in the `_applyRequestPluginHooks` function in `packages/insomnia/src/common/har.ts`.

---
Repository: /testbed
