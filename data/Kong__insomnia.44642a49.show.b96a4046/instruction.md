# Bug Report

### Describe the bug

After a recent update, the application fails to build. There seems to be a syntax error in the `prompt-modal.tsx` file that's preventing compilation. The TypeScript compiler is throwing errors related to the `PromptModalHandle` interface definition.

### Reproduction

1. Pull the latest changes
2. Try to build the project
3. Build fails with TypeScript compilation errors

The issue appears to be in `packages/insomnia/src/ui/components/modals/prompt-modal.tsx` around the `PromptModalHandle` interface definition. The interface structure looks malformed - it seems like there's incomplete or incorrectly nested code that's breaking the TypeScript parser.

### Expected behavior

The project should build successfully without TypeScript compilation errors. The `PromptModalHandle` interface should be properly defined with its `show` and `hide` methods.

### Additional context

This is blocking development as the app won't compile at all. Looks like maybe some code got accidentally committed that wasn't fully completed? The interface definition appears to have extra nested code that doesn't belong there.

---
Repository: /testbed
