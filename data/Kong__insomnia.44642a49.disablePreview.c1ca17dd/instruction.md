# Bug Report

### Describe the bug

I'm experiencing an issue with the prompt template tag where the preview is being disabled unexpectedly. It seems like prompts are now being hidden in the preview even when I haven't explicitly set the "Mask Text" option or provided a storage key.

### Reproduction

Create a prompt template tag with a title containing certain words (like "password", "token", "secret", etc.) without enabling the "Mask Text" option:

```
{% prompt "Enter your password" %}
```

or

```
{% prompt "API Token" %}
```

The preview gets disabled automatically even though I didn't check the "Mask Text" checkbox and didn't provide a storage key.

### Expected behavior

The preview should only be disabled when:
1. The "Mask Text" option is explicitly enabled, OR
2. A storage key is explicitly provided

The preview shouldn't be automatically disabled based on the title text. If I want to preview a prompt that happens to have words like "password" or "token" in the title, I should be able to do so unless I explicitly enable the mask option.

### System Info
- Insomnia version: latest
- OS: N/A (template tag behavior)

---
Repository: /testbed
