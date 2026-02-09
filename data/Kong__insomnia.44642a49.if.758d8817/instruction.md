# Bug Report

### Describe the bug

When importing cURL commands that contain variables starting with `$`, the variable names are being incorrectly truncated. Instead of removing just the `$` prefix, the last character of the variable name is also being removed.

### Reproduction

Try importing a cURL command with a variable:

```bash
curl -X GET "https://api.example.com/users/$userId/profile"
```

The variable `$userId` gets imported as `userI` instead of `userId`. The last character 'd' is being stripped off along with the `$` symbol.

### Expected behavior

The `$` prefix should be removed from variables, but the rest of the variable name should remain intact. So `$userId` should become `userId`, not `userI`.

### Additional context

This affects any cURL command containing shell variables. The import functionality is stripping one extra character from the end of variable names, which breaks the imported requests when the variables are used.

---
Repository: /testbed
