# Bug Report

### Describe the bug

When opening workspaces that were created with the old 'spec' scope, they are no longer being migrated to the 'design' scope as expected. Instead, these workspaces are now treated as if they already have a valid scope and no migration occurs.

### Reproduction

1. Create or load a workspace with `scope: 'spec'`
2. The workspace migration logic runs
3. The workspace keeps `scope: 'spec'` instead of being migrated to `WorkspaceScopeKeys.design`

Expected: Workspaces with the legacy 'spec' scope should be migrated to 'design' scope (same as 'designer' scope workspaces)

Actual: The 'spec' scope is now treated as valid and no migration happens

### Additional context

This affects users who have older workspaces that still use the 'spec' scope value. These workspaces should be automatically migrated to use the new scope system, but the migration is being skipped.

---
Repository: /testbed
