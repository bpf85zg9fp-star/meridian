---
document_id: "RFQ-0101"
title: "Automated Asset Population & Preference-Only Human Involvement Framework"
version: "0.1"
status: "Draft"
classification: "Technical / Implementation"
date: "2026-06-23"
programme: "Meridian"
author: "ChatGPT (Layer 1 Governance Drafting Role)"
yaml_schema: "meridian-a1-markdown-artefact-standard.yaml v1.1"
---

# RFQ-0101 — Automated Asset Population & Preference-Only Human Involvement Framework

## Purpose
Establish a Meridian-standard architecture where objective asset data is populated automatically while human involvement is restricted to preference definition, weighting and exception approval.

## Core Principle

> Assets are facts.
> Preferences are vectors.

Humans may influence weighting and constraints but may not directly curate asset facts.

## Architectural Layers

### Deterministic Asset Layer
- Discovery
- Ingestion
- Canonicalisation
- Deduplication
- Enrichment
- Versioning

### Graph Intelligence Layer
- Dependency mapping
- Compatibility analysis
- Substitution analysis
- Impact propagation

### Preference Layer
- Weight vectors
- Hard constraints
- Soft preferences
- Exception approvals

## Mandatory Amendments

### A1. Confidence Scoring
Every asset record shall carry:
- source confidence
- freshness score
- completeness score
- verification status

### A2. Provenance Requirements
Every field shall be traceable to:
- source
- timestamp
- ingestion event
- transformation history

### A3. Human Preference Learning
Preference vectors may be learned from approved historical selections but never modify source asset facts.

### A4. Continuous Re-evaluation
Material changes in pricing, availability, compliance, performance, or lifecycle characteristics shall trigger automatic re-scoring.

### A5. Auditability
All scoring outcomes must be reproducible through event replay.

## Outcome
A scalable, auditable and deterministic framework supporting Meridian asset discovery, procurement, RFQ generation and system design workflows.