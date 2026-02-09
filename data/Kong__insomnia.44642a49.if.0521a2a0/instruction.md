# Bug Report

### Describe the bug

I'm experiencing an issue with the cURL importer where it's not handling empty or whitespace-only parameter values correctly. When importing cURL commands that contain parameters with empty strings or only whitespace, the importer seems to be accepting these invalid values instead of falling back to default values.

### Reproduction

```bash
# Example cURL command with empty parameter value
curl -X POST "https://api.example.com" --data ""

# Or with whitespace-only value
curl -X GET "https://api.example.com" -H "Authorization:    "
```

When importing these commands, the empty or whitespace-only values are being processed as valid inputs rather than being ignored and replaced with appropriate defaults.

### Expected behavior

The importer should detect when parameter values are empty or contain only whitespace and fall back to the default value instead of using the invalid empty/whitespace value. This would make the imported requests more usable and prevent issues with empty headers or data fields.

### System Info
- Insomnia version: latest
- OS: Multiple platforms affected

---
Repository: /testbed
