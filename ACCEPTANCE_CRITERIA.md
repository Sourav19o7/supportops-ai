# SupportOps AI — Acceptance Criteria

## 1. Ticket Management

- [ ] An authenticated user can create a support ticket with a title, message, category, and priority.
- [ ] Required fields are validated by the backend.
- [ ] Tickets can be listed and opened individually.
- [ ] Invalid requests return structured errors without crashing the API.

## 2. Knowledge Base

- [ ] A user can ingest a Markdown or plain-text document.
- [ ] Documents are split into searchable chunks.
- [ ] Each chunk retains its source document ID and original text.
- [ ] Relevant passages can be retrieved for a question.
- [ ] Empty or invalid documents are rejected with a useful error.

## 3. AI Response Generation

- [ ] A ticket can be used to generate a response draft based on retrieved knowledge-base passages.
- [ ] The output follows a validated response schema.
- [ ] Citations reference only passages retrieved for that specific AI run.
- [ ] When the available knowledge is insufficient, the system declines to make unsupported factual claims.
- [ ] Provider failures and timeouts produce controlled errors.

## 4. Human Review

- [ ] A user can view and edit a generated draft.
- [ ] A user can approve or reject the draft.
- [ ] The original generated draft and the final reviewed response are stored separately.
- [ ] No response is sent to a real customer automatically.

## 5. AI Traces and Observability

- [ ] Each completed AI run records its configuration or prompt version.
- [ ] The trace records retrieved passage IDs, execution duration, and outcome.
- [ ] Token usage and estimated cost are recorded when available from the provider.
- [ ] Failed runs are distinguishable from successful runs.
- [ ] Secrets and sensitive credentials are not written to logs.

## 6. Evaluation

- [ ] A version-controlled dataset contains representative questions and expected results.
- [ ] The evaluation runner can execute the dataset reproducibly.
- [ ] Retrieval quality, citation validity, classification performance, and latency are measured.
- [ ] Answer quality is reviewed against documented criteria.
- [ ] Results from two configurations can be compared.
- [ ] The report identifies individual failures, not just aggregate scores.

## 7. Security and Reliability

- [ ] Private API routes reject unauthenticated requests.
- [ ] Users cannot access tickets or documents they are not authorized to access.
- [ ] Input validation runs on the backend.
- [ ] Retrieved documents are treated as untrusted content, not as instructions to override system rules.
- [ ] Tests cover invalid inputs, unauthorized access, and provider failures.

## 8. Deployment and Documentation

- [ ] The frontend and backend are deployed and accessible.
- [ ] Production environment variables are configured without exposing secrets.
- [ ] Automated tests and static checks run in CI.
- [ ] The README documents setup, architecture, environment variables, and test commands.
- [ ] A short demo demonstrates the complete ticket-to-reviewed-draft workflow.

## Definition of Done

A feature is complete only when its acceptance criteria pass, relevant tests are written, errors are handled, and the implementation is committed to version control.
