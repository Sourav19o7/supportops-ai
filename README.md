# SupportOps AI

An AI-assisted customer support workspace that drafts grounded responses from a knowledge base, keeps humans in control, and measures AI quality through repeatable evaluations.

## Problem

Support teams need to answer customer questions consistently. Generic AI responses can invent information, miss relevant documentation, and make quality difficult to measure.

SupportOps AI aims to make AI-assisted support more traceable and testable.

## Core workflow

1. Create and view a support ticket.
2. Ingest Markdown or text documents into a searchable knowledge base.
3. Retrieve relevant passages for a ticket.
4. Generate a response draft with source citations and a predicted category and priority.
5. Review, edit, approve, or reject the draft.
6. Inspect AI execution traces and run repeatable evaluations.

## Technology stack

- Frontend: Next.js, TypeScript, Tailwind CSS
- Backend: Python, FastAPI, Pydantic
- Database: Supabase PostgreSQL with pgvector
- Authentication: Supabase Auth
- Testing: Pytest, HTTPX
- CI: GitHub Actions

## Architecture

The Next.js frontend communicates with a FastAPI backend. The backend authenticates requests, retrieves relevant knowledge-base passages, calls an LLM provider, validates generated citations, and persists results and execution traces.

A separate evaluation runner tests a fixed dataset against different prompt or retrieval configurations.

## Non-goals

- Autonomous customer communication
- Multi-agent orchestration
- Billing and payments
- External support-platform integrations
- Model fine-tuning
- Complex enterprise permissions
- Production claims unsupported by measurements

## Quality principles

- AI-generated answers require human review.
- Citations must reference passages retrieved for the corresponding run.
- Provider failures must be handled safely.
- Evaluation datasets and configurations must be versioned.
- Quality, latency, and cost measurements must be reproducible.
- Secrets must never be committed or exposed to the browser.

## Project status

Day 1: Scope and acceptance criteria.

The MVP is intentionally limited to a single end-to-end support workflow and its evaluation pipeline.

## Local development

Setup instructions, environment variables, database migrations, and test commands will be added as the implementation progresses.

## Known limitations

This is a portfolio project. Its evaluation results will reflect the documented test dataset and methodology, not a guarantee of production performance or general AI accuracy.
