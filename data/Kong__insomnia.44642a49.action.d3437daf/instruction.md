# Bug Report

### Describe the bug

After a recent update, the plugin system appears to have a syntax error in the `index.ts` file. The `DocumentAction` interface definition is broken - it looks like function implementations were accidentally inserted into the middle of the interface declaration.

### Reproduction

When trying to use the application with plugins enabled, the TypeScript compilation fails. The `DocumentAction` interface should define the structure for document actions, but instead has function code mixed into it.

Looking at the code:
```ts
export interface DocumentAction extends InternalProperties {
  action: (context: Record<string, any>, documents: ParsedApiSpec) => void | Promise<void>;
  label: string;
export function filterDocumentActionsByContext(
  // ... function implementation
}
  hideAfterClick?: boolean;
}
```

The interface definition starts normally with `action` and `label` properties, but then abruptly transitions into function declarations (`filterDocumentActionsByContext` and `getDocumentActions`) before closing with `hideAfterClick`.

### Expected behavior

The `DocumentAction` interface should be properly closed before any function declarations. The interface should only contain type definitions, not function implementations.

### System Info
- Package: @insomnia/insomnia
- File: packages/insomnia/src/plugins/index.ts

---
Repository: /testbed
