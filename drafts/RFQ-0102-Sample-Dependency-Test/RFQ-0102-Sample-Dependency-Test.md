---
document_id: "RFQ-0102"
title: "Sample Dependency Test - Structural Integration"
version: "0.1"
status: "Draft"
classification: "Test / Dependency Validation"
date: "2026-06-30"
programme: "Meridian"
author: "Grok (Layer 3)"
yaml_schema: "meridian-a1-markdown-artefact-standard.yaml v1.1"
document_taxonomy: "RFQ Requirements and Framework Standards"
tags:
  - dependency-test
  - structural
related_documents: []
dependencies:
  - component: "High-efficiency HVAC system"
    requires:
      - "Ductwork modifications for zoning"
      - "Electrical panel upgrade: capacity increase"
      - "Smart thermostat integration with existing BMS"
      - "Condensate drainage and insulation retrofits"
---

# RFQ-0102 — Sample Dependency Test

Test case for dynamic dependency resolution (new HVAC example in estate context). Ensures synergy/gap-filling without blocking.