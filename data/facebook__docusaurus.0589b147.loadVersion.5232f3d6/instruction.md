# Bug Report

### Describe the bug

I'm seeing error messages in the console even when documentation versions load successfully. The logs show "Loading of version failed" messages for every version, even though the build completes without any actual errors.

### Reproduction

1. Set up a Docusaurus project with versioned docs
2. Run the build or start the dev server
3. Check the console output

You'll see error messages like:
```
[ERROR] Loading of version failed for version name=current
[ERROR] Loading of version failed for version name=1.0.0
```

But the versions actually load fine and the site works as expected.

### Expected behavior

Error messages should only appear when version loading actually fails. Successful version loads shouldn't log error messages.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
