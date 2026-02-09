# Bug Report

### Bug with version validation in docs plugin

I'm experiencing an issue with the docs plugin version validation. It seems like the validation logic for `onlyIncludeVersions` and `lastVersion` options is not working as expected.

### Reproduction

When I configure my docusaurus.config.js with the following:

```js
{
  docs: {
    onlyIncludeVersions: ['1.0.0'],
    lastVersion: '1.0.0'
  }
}
```

I get an error saying that an empty array is not allowed, even though I'm providing a single version. The error message doesn't match what I'm actually doing.

Also, when I try this configuration:

```js
{
  docs: {
    onlyIncludeVersions: ['1.0.0', '2.0.0'],
    lastVersion: '1.0.0'
  }
}
```

I get an error saying that `lastVersion` must be present in the `onlyIncludeVersions` array, but it clearly is present in the array!

### Expected behavior

1. When `onlyIncludeVersions` contains a single version, it should be accepted without errors
2. When `lastVersion` is included in the `onlyIncludeVersions` array, the validation should pass

The validation seems to be checking for the opposite conditions of what it should be checking for.

---
Repository: /testbed
