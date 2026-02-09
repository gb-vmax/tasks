# Bug Report

### Describe the bug

I'm experiencing an issue with the plugin system where document actions are showing duplicate entries in the UI. After a recent update, it looks like document action properties are being defined twice, causing them to appear multiple times in the action menu.

### Reproduction

1. Install a plugin that defines document actions
2. Open a document/API spec
3. Check the available document actions in the menu
4. Notice that some actions appear duplicated or have unexpected properties

The issue seems to be related to how `DocumentAction` interface properties are being defined. Looking at the code, it appears that `hideAfterClick` and potentially other properties might be declared in multiple places.

### Expected behavior

Each document action should appear only once in the menu with the correct set of properties. The `DocumentAction` interface should have a clean, non-duplicated definition including:
- `action` callback
- `label` string
- Optional `icon`
- Optional `hideAfterClick`
- Optional `visible` function

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking our plugin development workflow. Any help would be appreciated!

---
Repository: /testbed
