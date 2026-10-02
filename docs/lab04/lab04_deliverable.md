# Requirements Traceability Matrix

| Req ID  | Requirement Description                                                                                 | Test Case ID(s)                                | Test Level | Status   |
| ------- | ------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | ---------- | -------- |
| REQ-001 | New user can register with a unique email and a password of at least 8 characters.                      | TC-REG-01, TC-REG-02, TC-REG-03                | System     | Not run |
| REQ-002 | Registration is rejected when the email is already in use and an error message is displayed.            | TC-REG-04, TC-REG-05                           | System     | Not run |
| REQ-003 | Users can search by title, author, or ISBN and matching results are returned within 2 seconds.          | TC-SRCH-01, TC-SRCH-02, TC-SRCH-03, TC-SRCH-04 | System     | Not run |
| REQ-004 | The system displays "No results found" when a search returns no matches.                                | TC-SRCH-05                                     | System     | Designed |
| REQ-005 | A registered user can borrow up to 3 available books at a time, with a 14-day loan period.              | TC-BRW-01, TC-BRW-02, TC-BRW-03, TC-BRW-04     | System     | Not designed |
| REQ-006 | Borrowing is prevented when the user already has 3 books on loan or an overdue item.                    | TC-BRW-05, TC-BRW-06, TC-BRW-07                | System     | Not run |
| REQ-007 | A return is recorded, book availability is updated, and an overdue fine is calculated at P2.00 per day. | TC-RET-01, TC-RET-02, TC-RET-03, TC-RET-04     | System     | Not run |
| REQ-008 | An email is sent 2 days before the due date and again on each day the book is overdue.                  | TC-NOT-01, TC-NOT-02, TC-NOT-03                | System     | Not run |


# Mini Test Plan 

**Selected requirement:** REQ-005 — "A registered user shall be able to borrow up to 3 available books at a time for a 14-day loan period."

## In Scope

* Verifying that a registered user can borrow available books.
* Verifying borrowing of one, two, and three books.
* Verifying that three books is the maximum permitted number of active loans under REQ-005.
* Verifying that each borrowed book receives a 14-day loan period.

## Out of Scope

* Return processing and fine calculation, covered by REQ-007.
* Borrowing restrictions caused by overdue items, covered by REQ-006.
* Overdue email notifications, covered by REQ-008.
* User registration, covered by REQ-001 and REQ-002.
* Book searching, covered by REQ-003 and REQ-004.
* Payment processing, which is not specified in the supplied requirements.
* Load or concurrency testing, which is not specified in REQ-005.

## Entry Criteria

Testing can begin when:

* The system is deployed to a test environment.
* A registered test user account exists.
* The test user has fewer than three active loans.
* At least three available books exist.
* The borrowing function is accessible.
* Test data has been loaded and validated.

## Exit Criteria

Testing is complete when:

* TC-BRW-01 through TC-BRW-04 have been executed.
* All in-scope test cases have passed, or failures have been documented as defects.
* Any identified defects have been logged and triaged.
* The RTM has been updated with the final test status.
* No unresolved Critical or High severity defects remain for REQ-005.

## Test Cases Covered

| Test Case ID | Description                                               |
| ------------ | --------------------------------------------------------- |
| TC-BRW-01    | Borrow one available book and verify the 14-day due date. |
| TC-BRW-02    | Borrow two available books successfully.                  |
| TC-BRW-03    | Borrow three available books successfully.                |
| TC-BRW-04    | Verify that the loan period is exactly 14 days.           |


# Defect Lifecycle Log

## Defect 1 — Minimum Password Length Not Enforced

**GitHub Issue:** https://github.com/ISAACS-I/task-manager/issues/1

## Defect 2 — Incorrect Overdue Fine Calculation

**GitHub Issue:** https://github.com/ISAACS-I/task-manager/issues/2


# Severity and Priority Scales

## Severity

| Severity | Meaning                                                                             |
| -------- | ----------------------------------------------------------------------------------- |
| Critical | System crash or complete failure where testing cannot continue.                     |
| Major    | A major feature fails or a primary user task cannot be completed correctly.         |
| Medium   | A functional problem exists but a workaround is available or the impact is limited. |
| Low      | A minor problem with little functional impact.                                      |

## Priority

| Priority | Meaning                                                                                      |
| -------- | -------------------------------------------------------------------------------------------- |
| P1       | Fix immediately because the defect blocks or significantly affects an important requirement. |
| P2       | Fix during the current development cycle.                                                    |
| P3       | Fix when resources permit.                                                                   |


# AI-Generated Traceability Matrix

| Req ID  | Test Case ID | Test Case                                                                                    | Test Level | Status   |
| ------- | ------------ | -------------------------------------------------------------------------------------------- | ---------- | -------- |
| REQ-001 | AI-TC-01     | Register using a unique email and password of at least 8 characters.                         | System     | Designed |
| REQ-002 | AI-TC-02     | Attempt registration using an existing email address and verify rejection and error message. | System     | Designed |
| REQ-003 | AI-TC-03     | Search by title and verify matching results are returned within 2 seconds.                   | System     | Designed |
| REQ-003 | AI-TC-04     | Search by author and verify matching results are returned within 2 seconds.                  | System     | Designed |
| REQ-003 | AI-TC-05     | Search by ISBN and verify matching results are returned within 2 seconds.                    | System     | Designed |
| REQ-004 | AI-TC-06     | Search for a term with no matching records and verify "No results found" is displayed.       | System     | Designed |
| REQ-005 | AI-TC-07     | Borrow an available book as a registered user and verify the 14-day loan period.             | System     | Designed |
| REQ-005 | AI-TC-08     | Borrow three available books and verify that the third borrowing succeeds.                   | System     | Designed |
| REQ-006 | AI-TC-09     | Attempt to borrow a fourth book when three are already on loan.                              | System     | Designed |
| REQ-006 | AI-TC-10     | Attempt to borrow while an overdue item exists.                                              | System     | Designed |
| REQ-007 | AI-TC-11     | Return a book and verify the return is recorded and availability is updated.                 | System     | Designed |
| REQ-007 | AI-TC-12     | Return an overdue book and verify the fine is calculated at P2.00 per day.                   | System     | Designed |
| REQ-008 | AI-TC-13     | Verify an email is sent two days before the due date.                                        | System     | Designed |
| REQ-008 | AI-TC-14     | Verify emails are sent while the book remains overdue.                                       | System     | Designed |


## Main Differences

The largest difference is test depth.

The AI-generated matrix establishes a valid one-to-many traceability relationship and covers every requirement but it uses fewer test cases. The manual matrix expands requirements with numerical boundaries and different valid scenarios.

For example, REQ-001 states that the password must contain **at least 8 characters**. The manual matrix tests both:

* 7 characters — just below the boundary.
* 8 characters — exactly at the boundary.

The AI matrix only tests the minimum requirement without explicitly testing the value immediately below it.


# Reflection

The AI-generated traceability matrix mapped all eight requirements to at least one test case giving it 100% requirement coverage. Its main limitation was depth. The key lesson is AI-generated RTM can quickly establish initial requirement-to-test traceability but it still needs human review to ensure that the tests adequately cover boundaries, state changes, and other important conditions in the requirements.

