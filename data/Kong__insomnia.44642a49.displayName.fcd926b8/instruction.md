# Bug Report

### Describe the bug

I'm experiencing a syntax error in the response template tag configuration. After a recent update, the templating system seems to have broken code structure where a function definition `getResponseFieldHelp` was inserted in the middle of an object property definition, causing the entire template tag to fail.

### Reproduction

When trying to use the Response template tag in the UI:

1. Open any request
2. Try to add a Response template tag
3. The template tag selector either throws an error or doesn't load properly

The issue appears to be in the `local-template-tags.ts` file where the object structure for the response field argument is malformed.

### Expected behavior

The Response template tag should load correctly and allow users to:
- Select response field type (body, header, raw, url)
- See appropriate display names for each field type
- Configure filters for body/header extraction

### Additional context

This seems to have broken after some refactoring where a helper function was added but placed incorrectly within the object literal definition. The `displayName` property definition appears to be split with function code inserted between the property and its closing brace.

---
Repository: /testbed
