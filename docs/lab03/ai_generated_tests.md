# AI-Generated Test Data

## Prompt

You are helping with a university software testing lab (COMP 441). I need you to generate test cases for a specific Python function using two formal test design techniques: equivalence partitioning and boundary value analysis.

Treat this function as if it has no documentation beyond the docstring shown. The specification is: "premium users receive a 20% discount on the given price; non-premium users pay full price."

Here is the function under test:

    def calculate_discount(price, is_premium):
        """Apply a loyalty discount for premium users."""
        if is_premium == True:
            return price * 0.8
        else:
            return price

Please produce the following, structured clearly:

1. EQUIVALENCE CLASSES
   For each input variable (price and is_premium), list the equivalence classes. Mark each as VALID or INVALID, and give sample values for each class.

2. BOUNDARY VALUES
   For each equivalence class boundary, list:
   - the boundary value
   - the value just inside the boundary
   - the value just outside the boundary
   Give the rationale for each boundary.

3. CONCRETE TEST CASES
   A table of test cases with columns:
   | TC ID | Description | price | is_premium | Expected Output |
   Include at least 10 test cases that together cover every equivalence class and boundary you identified.

4. NOTES
   Briefly note any assumptions you are making about the specification that were not stated explicitly.

Keep the output concise and structured so it can be compared directly against a manually derived test set.

## AI Response

### 1. Equivalence Classes

#### Input variable: price

| Class | Description | Type | Sample Values |
|-------|-------------|------|---------------|
| P1 | Positive price | Valid | 10, 50, 100 |
| P2 | Zero price | Valid | 0 |
| P3 | Negative price | Invalid | -10, -50 |

#### Input variable: is_premium

| Class | Description | Type | Sample Values |
|-------|-------------|------|---------------|
| B1 | True (premium) | Valid | True |
| B2 | False (non-premium) | Valid | False |

### 2. Boundary Values

price — boundaries at 0 (transition from invalid to valid):

| Boundary | Value | Position |
|----------|-------|----------|
| B1 | -0.01 | Just outside (negative) |
| B2 | 0 | On the boundary |
| B3 | 0.01 | Just inside (positive) |
| B4 | 100 | Nominal positive value |
| B5 | 10000 | Upper nominal (assumed max retail price) |

is_premium — only two valid values, so boundaries are the class transitions themselves:

| Boundary | Value | Position |
|----------|-------|----------|
| B6 | True | Valid |
| B7 | False | Valid |

### 3. Concrete Test Cases

| TC ID | Description | price | is_premium | Expected Output |
|-------|-------------|-------|------------|-----------------|
| AI-01 | Premium user, normal price | 100 | True | 80.0 |
| AI-02 | Non-premium user, normal price | 100 | False | 100 |
| AI-03 | Premium user, zero price | 0 | True | 0 |
| AI-04 | Non-premium user, zero price | 0 | False | 0 |
| AI-05 | Premium user, just above zero | 0.01 | True | 0.008 |
| AI-06 | Non-premium user, just above zero | 0.01 | False | 0.01 |
| AI-07 | Premium user, just below zero (invalid) | -0.01 | True | -0.008 |
| AI-08 | Non-premium user, just below zero (invalid) | -0.01 | False | -0.01 |
| AI-09 | Premium user, large price | 10000 | True | 8000.0 |
| AI-10 | Non-premium user, large price | 10000 | False | 10000 |

### 4. Notes / Assumptions

- I assume `price` is expected to be non-negative, so the negative-price class is marked INVALID. However, the function does not enforce this — it will silently compute a negative result.
- I assume there is no upper bound on `price`; the value `10000` is used as an illustrative "large" price, not a documented maximum.
- I assume `is_premium` is expected to be a strict boolean. The function does not validate this.
- The function uses `is_premium == True` rather than `is_premium is True`, which means truthy non-boolean values (e.g., `1`) would take the discount branch. I have not tested this case because the specification does not describe non-boolean inputs.
