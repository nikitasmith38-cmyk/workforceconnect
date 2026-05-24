# WorkforceConnect - System Security Plan Summary
## Week 3 Control Implementation

### AC-2: Account Management
Control: IAM roles scoped to least privilege. AdministratorAccess removed from EC2
role.
Implementation: BCE-EC2-WorkforceConnect-Policy attached. Reviewed and documented.

### AC-6: Least Privilege
Control: EC2 instance granted only CloudWatch log write and EC2 describe permissions.
Implementation: Custom IAM policy. No wildcard actions permitted.

### AU-2: Audit Events
Control: All management API calls logged via CloudTrail.
Implementation: BCE-DOL-OWS-Audit-Trail enabled, multi-region, delivering to S3.

### AU-9: Protection of Audit Information
Control: CloudTrail logs stored in S3 with bucket policy restricting access to
CloudTrail service only

Implementation: Public access blocked. Bucket policy applied.

### IR-4: Incident Handling
Control: CloudWatch alarms trigger SNS email alerts for unauthorized API calls and
root account usage.
Implementation: Two alarms active. SNS topic confirmed. Email subscription verified.

### SC-7: Boundary Protection
Control: Security groups enforce least-privilege network access. ALB is the sole
public ingress point.
Implementation: SSH restricted to student IP. RDS accessible only from EC2 security
group. EC2 accepts HTTP only from ALB security group.

### SC-5: Denial of Service Protection
Control: AWS WAF Web ACL attached to ALB blocks common web exploits and known
malicious patterns.
Implementation: BCE-WorkforceConnect-WAF with AWSManagedRulesCommonRuleSet,
SQLiRuleSet, and KnownBadInputsRuleSet. WAF verified via 403 response to SQL injection
test pattern.

### SI-3: Malicious Code Protection
Control: WAF managed rule groups inspect all inbound HTTP requests for malicious
payloads before they reach the application.
Implementation: Three AWS Managed Rule Groups active. Default action: Block on rule
match.
