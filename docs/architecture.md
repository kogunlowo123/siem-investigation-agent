# SIEM Investigation Agent Architecture

SIEM investigation agent that translates natural language questions into SIEM queries (KQL, SPL, Lucene), analyzes search results, identifies attack patterns, and generates structured investigation reports.

## Domain Tools

- **analyze**: Primary analysis function for SIEM Investigation Agent
- **scan**: Scan target for issues relevant to SIEM Investigation Agent
- **report**: Generate report for SIEM Investigation Agent
- **remediate**: Execute remediation action
- **monitor**: Monitor for ongoing issues