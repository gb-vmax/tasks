FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/pipeline

cat > /home/user/pipeline/build.log << 'EOF'
[BUILD] module=core status=SUCCESS duration_ms=3420
[WARN] module=core file=NetworkUtils.kt message=Deprecated API usage in sendRequest()
[WARN] module=core file=CacheManager.kt message=Unchecked cast to List<String>
[BUILD] module=auth status=SUCCESS duration_ms=1870
[WARN] module=auth file=LoginActivity.kt message=Variable 'token' is never used
[ERROR] module=auth file=OAuthHandler.kt message=Unresolved reference: refreshToken
[BUILD] module=payments status=FAILED duration_ms=5210
[ERROR] module=payments file=PaymentGateway.kt message=Type mismatch: inferred type is String but Int was expected
[ERROR] module=payments file=CheckoutFlow.kt message=None of the following candidates is applicable
[ERROR] module=payments file=PaymentGateway.kt message=Overload resolution ambiguity
[BUILD] module=notifications status=SUCCESS duration_ms=980
[WARN] module=notifications file=PushHandler.kt message=Deprecated API usage in scheduleNotification()
[BUILD] module=analytics status=SUCCESS duration_ms=2650
[WARN] module=analytics file=EventTracker.kt message=Unchecked cast to Map<String, Any>
[WARN] module=analytics file=SessionManager.kt message=Variable 'userId' is never used
[BUILD] module=ui-components status=FAILED duration_ms=4100
[ERROR] module=ui-components file=ThemeManager.kt message=Unresolved reference: colorSurface
[WARN] module=ui-components file=ButtonStyles.kt message=Deprecated API usage in applyRipple()
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
