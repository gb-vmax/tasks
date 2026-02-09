# Bug Report

### Describe the bug

After a recent update, the prompt template tag is now hiding/masking values in the preview even when the "Mask Text" option is not explicitly enabled. This is happening for prompts that have storage keys containing certain words like "password", "token", "key", etc.

### Reproduction

```js
// Create a prompt template tag with the following configuration:
{
  title: 'Enter Value',
  label: 'Value',
  defaultValue: 'test',
  storageKey: 'my_api_key',
  maskText: false  // explicitly set to false
}
```

The preview is being disabled/masked even though `maskText` is set to false. This seems to be triggered by having "api" or "key" in the storage key name.

### Expected behavior

The preview should only be disabled when the "Mask Text" option is explicitly enabled by the user. Having certain keywords in the storage key name shouldn't automatically trigger preview masking.

This is breaking existing workflows where we use descriptive storage keys that happen to contain words like "api", "key", "token" etc., but don't actually contain sensitive data.

### Additional context

This appears to have started after a recent change to the template tag logic. The behavior is particularly problematic because:
1. It's not documented anywhere that certain keywords would trigger this behavior
2. There's no way to override it even if you explicitly set maskText to false
3. Many common variable names naturally include these keywords (e.g., "api_endpoint", "encryption_key_size", "auth_type")

---
Repository: /testbed
