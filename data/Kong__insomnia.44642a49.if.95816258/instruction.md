# Bug Report

### Describe the bug

When working with authentication options, variables with empty keys or certain empty values are not being properly filtered out. This causes issues when trying to set up auth configurations, as invalid/empty variables are being included in the authentication flow.

### Reproduction

```js
const authVars = [
  new Variable({ key: '', value: 'some-value' }),  // Empty key
  new Variable({ key: 'username', value: 'testuser' }),
  new Variable({ key: 'api-key', value: '' }),  // Empty value
  new Variable({ key: 'password', value: '' })  // Empty password (should be allowed)
];

// When converting to auth options, empty key variables are included
const result = rawOptionsToVariables(authVars);
// Expected: Only valid variables should be included
// Actual: All variables are included, even those with empty keys
```

Also having issues with disabled variables not being filtered:

```js
const authOptions = {
  type: 'bearer',
  bearer: [
    { key: 'token', value: 'abc123', disabled: true }
  ]
};

// Disabled variables should be excluded but they're not
```

### Expected behavior

- Variables with empty or whitespace-only keys should be filtered out
- Variables marked as disabled should be excluded from the auth configuration
- Empty values should be filtered except for specific keys like 'password', 'value', 'scope', and 'state' where empty strings might be valid

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
