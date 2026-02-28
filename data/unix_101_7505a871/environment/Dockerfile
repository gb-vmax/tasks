FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/code
RUN echo -e '#include <stdio.h>\nint main() {\n    printf("Hello!\\n");\n    return 0;\n}' > /home/user/code/file.c
RUN cat > /home/user/change.patch <<EOF
--- code/file.c	2024-01-01 12:00:00.000000000 +0000
+++ code/file.c	2024-01-01 12:00:00.000000000 +0000
@@ -1,5 +1,6 @@
 #include <stdio.h>
 int main() {
-    printf("Hello!\\n");
+    printf("Patched!\\n");
     return 0;
 }
EOF
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

