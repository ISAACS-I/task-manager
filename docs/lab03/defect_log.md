# Lab 3 - Defect Log

**Severity scale:** Critical / Major / Medium / Low (same as Lab 1).

| ID | File | Line | Found by test | Description | Severity | Status |
|----|------|------|---------------|-------------|----------|--------|
| D1 | app/tasks.py | 77–82 | TC07, TC08 | calculate_discount() does not validate price. Negative prices are accepted instead of being rejected. For premium users, the negative price is discounted further; for non-premium users, it is returned unchanged. | Major | Open |
| D2 | app/tasks.py | 77–82 | TC09, TC10 | calculate_discount() does not validate is_premium. A None value is silently treated as non-premium instead of being rejected.| Major | Open |
| D3 | app/tasks.py | 77–82 | test_is_premium_as_none1 (TC09) | calculate_discount() does not type-check is_premium. Passing None with a positive price is silently accepted; because None == True is False, the function returns the full price instead of flagging the missing/null flag. | Medium | Open |
| D4 | app/tasks.py | 77–82 | test_is_premium_as_none (TC10) | Same root cause as D3, exercised with price = 0. Demonstrates the missing-validation behaviour is independent of the price value. | Medium | Open |
| D5 | app/tasks.py | 79 | pylint C0121 (Lab 2) | Comparison is_premium == True should be is_premium is True. Using == allows truthy non-booleans to silently take the discount branch. This was flagged statically in Lab 2; dynamic analysis now confirms its runtime impact. | Low | Open |




