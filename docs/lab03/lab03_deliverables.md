# Lab 3

## Equivalence Partition Table

**Target function:** `calculate_discount(price, is_premium)` in `app/tasks.py`

**Function under test:**

def calculate_discount(price, is_premium):
    """Apply a loyalty discount for premium users."""
    if is_premium == True:
        return price * 0.8
    else:
        return price

### Input variables and valid domains

| Input        | Type    | Valid domain                      |
| ------------ | ------- | --------------------------------- |
| price      | numeric | non-negative prices |
| is_premium | boolean | true or false               |

### Input variable: price

| Partition ID | Class Description | Type | 
|--------------|-------------------|------|
| P1 | price > 0 | valid |
| P2 | price = 0 | valid |
| P3 | price < 0 | invalid |
| P4 | non-numeric | invalid |

### Input variable: is_premium

| Partition ID | Class Description | Type | 
|--------------|-------------------|------|
| B1 | true | valid | 
| B2 | false | valid | 
| B3 | null | invalid | 

## Boundary Value Table

**Target function:** `calculate_discount(price, is_premium)`

### Variable: price

| Boundary ID | Value | Position | 
|-------------|-------|----------|
| BV1 | -1.00 | outside | 
| BV2 | -0.01 | just outside | 
| BV3 | 0 | boundary | 
| BV4 | 0.01 | just inside | 
| BV5 | 1.00 | inside | 

### Variable: is_premium

| Boundary ID | Value | Position |
|-------------|-------|----------|
| BV6 | true | boundary | 
| BV7 | false | boundary |
| BV8 | null | outside | 

## Test Design Table

| TC ID | Description | price | is_premium | Expected Output | 
|-------|-------------|-------|------------|-----------------|
| TC01 | premium user, price > 0 | 100 | true | 80.0 |
| TC02 | non-premium user, price > 0 | 100 | false | 100 | 
| TC03 | premium user, price = 0 | 0 | true | 0 | 
| TC04 | non-premium user, price = 0 | 0 | false | 0 | 
| TC05 | premium user, tiny positive price | 0.01 | true | 0.008 | 
| TC06 | non-premium user, tiny positive price | 0.01 | false | 0.01 | 
| TC07 | premium user, tiny negative price | -0.01 | true | value error | 
| TC08 | non-premium user, tiny negative price | -0.01 | false | value error | 
| TC09 | is_premium is null, price > 0 | 100 | null | type error |
| TC10 | is_premium is null, price = 0 | 0 | null | type error |

## Manual vs AI-Generated Test Cases

### Comparison Table

| Metric | Manual set | AI-generated set | Overlap |
|--------|-----------|------------------|---------|
| Total test cases | 12 | 10 | 8 |
| Partition coverage (price) | P1, P2, P3, P$ | P1, P2, P3, P4 | Full |
| Partition coverage (is_premium) | B1, B2, B3| B1, B2 | Partial|
| Boundary values tested | -1.00, -0.01, 0, 0.01, 1.00 | -0.01, 0, 0.01, 100, 10,000 | Partial |
| Invalid-input tests | 4 (2 price and 2 type) | 2 (only price) | Partial |
| Hallucinated boundaries | 0 | 1 (invented 10,000 max price) | — |

### Overlaps — cases the AI reproduced

| Manual test | AI equivalent | Match |
|-------------|---------------|-------|
| TC01 — premium, 100 | AI-01 | full |
| TC02 — non-premium, 100 | AI-02 | full |
| TC03 — premium, 0 | AI-03 | full |
| TC04 — non-premium, 0 | AI-04 | full |
| TC05 — premium, 0.01 | AI-05 | full |
| TC06 — non-premium, 0.01 | AI-06 | full |
| TC07 — premium, -0.01 | AI-07 | full |
| TC08 — non-premium, -0.01 | AI-08 | full |

### Verdict

The AI-generated set was structurally correct but shallow on invalid inputs. It reproduced the obvious nominal and boundary cases but missed every type-level and null case.

The manual set was stronger as it tested invalid types and not just invalid values.

**Recommendation:** AI-generated test data is a useful first draft for the happy path and simple boundaries, but it must be supplemented by a manual pass over the invalid partitions. That is where the majority of the defects in this function live.

## Reflection

The AI assistant reproduced 8 of my 12 manual test cases. The overlaps were concentrated in the obvious cases: the nominal valid price with each boolean value, zero price with each boolean value, and the just-inside and just-outside boundaries at 0.01 and -0.01. All of these fall naturally out of a first-pass partition analysis.

What the AI missed was concentrated in invalid input types. My manual set included tests for:

- is_premium = 1 (truthy integer — Python's 1 == True silently takes the discount branch)
- is_premium = None (missing/null flag — falls through to the else branch and returns full price)

The AI did not test either. In its own notes it acknowledged that 1 == True would take the discount branch, but chose not to generate a test for it because "the specification does not describe non-boolean inputs." 

The AI also hallucinated one constraint: it invented a maximum price of 10,000 and labelled it "assumed max retail price." No such maximum exists in the specification. A test derived from that assumption could give false confidence about the valid input range.

Finally, the AI misinterpreted expected outputs for invalid inputs. For the negative-price cases it listed -0.008 and -0.01 as expected outputs treating the current buggy behaviour as correct. My manual set correctly classifies those as invalid inputs.

### Proportion of manual boundary cases reproduced

| Manual boundary case | Reproduced by AI |
|----------------------|-------------------|
| -1.00 (outside) | no |
| -0.01 (just outside) | yes |
| 0 (on the boundary) | yes |
| 0.01 (just inside) | yes |
| 1.00 (inside) | no |
| is_premium = 1 (invalid type) | no |
| is_premium = None (invalid type) | no |

3 of 7 boundary cases reproduced exactly.

### Takeaway

The AI was useful for generating the baseline set and for cross-checking whether I had missed any obvious partition. But it was systematically weak at invalid input types and prone to inventing unstated constraints.

