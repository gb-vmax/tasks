# Bug Report

### Describe the bug

The swizzle command is showing components that shouldn't be available for certain actions. When trying to swizzle components, the list includes components that have no safe actions available, which seems incorrect.

### Reproduction

When running the swizzle command to list available components, components that should be filtered out (because they don't have any safe actions) are still appearing in the list.

Steps to reproduce:
1. Run the swizzle command to list components
2. Notice that components without any safe swizzle actions are included
3. The filtering logic appears to be inverted - components are shown when they should be hidden

### Expected behavior

Components should only appear in the swizzle list if they have at least one safe action available. Components with no safe actions should be filtered out from the available options.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
