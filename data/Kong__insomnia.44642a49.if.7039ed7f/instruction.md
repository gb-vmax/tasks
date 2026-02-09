# Bug Report

### Describe the bug

When creating or editing environment variables, the validation for key names appears to be inverted. Keys that should be valid are being rejected with an error message saying they "must begin with '$' or contain a '.'", while keys that should actually be invalid (those starting with '$' or containing '.') are being accepted.

### Reproduction

1. Open the environment editor
2. Try to add a new variable with a normal key name like `API_KEY` or `baseUrl`
3. The editor shows an error: `"API_KEY" must begin with '$' or contain a '.'`
4. Now try adding a variable with a key like `$invalid` or `my.key`
5. These invalid keys are accepted without any validation error

### Expected behavior

- Normal key names (without '$' prefix or '.' characters) should be accepted
- Keys starting with '$' or containing '.' should be rejected with an appropriate error message
- The error message should say the key "cannot begin with '$' or contain a '.'"

### System Info
- Insomnia version: latest
- OS: [any]

This is blocking me from creating any environment variables with standard naming conventions.

---
Repository: /testbed
