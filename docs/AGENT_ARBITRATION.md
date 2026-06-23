# Multi-Agent Arbitration Layer — Meridian

## Purpose
This document defines deterministic rules for concurrent write access by multiple AI agents (ChatGPT, Claude, Gemini, Codex, etc.).

---

## Problem Statement
Without coordination, multiple agents may:
- overwrite drafts
- diverge schema interpretations
- create conflicting dependency edges
- corrupt event ordering

---

## Core Principle
> All agents must treat Meridian as a shared-state system with a single serialized write lane.

---

## System Components

### 1. Agent Identity Layer
Each agent MUST declare:
- agent_id
- source_model
- session_id

---

### 2. Write Arbitration Queue
All writes MUST pass through:
```
agents/queue.jsonl
```

Each entry:
```json
{
  "agent_id": "string",
  "timestamp": "ISO-8601",
  "target_path": "string",
  "operation": "create|update|delete",
  "priority": 0-10,
  "status": "queued|granted|rejected"
}
```

---

### 3. Locking Model
- Only one ACTIVE writer per target path
- Locks are advisory but enforced via CI

---

### 4. Deterministic Resolution Rules
Priority ordering:
1. CI system writes (highest)
2. DAG enforcement system
3. Event store appenders
4. External AI agents (lowest)

---

## Conflict Resolution
If two agents conflict:
- CI halts merge
- ledger records conflict event
- latest validated state wins only if DAG consistent

---

## Auditability
Every arbitration decision MUST emit:
- event log entry
- CI annotation
- optional replay snapshot

---

## Outcome
This layer ensures multi-agent safe concurrency without requiring real-time coordination.
