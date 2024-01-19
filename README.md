Consent Management Auto-Consent Mode- Beta Documentation

Readme
This document provides details regarding Prisma Public Cloud’s Beta support for Consent Management- Auto-Consent Mode . This
document is organized into various sections, starting with target audience, assumptions, scope etc. If you have any questions or
clarifications, please reach out to your Sales / Support personnel at Palo Alto Networks and / or email at racharya@paloaltonetworks.com

Feature Overview
Amongst other features, Prisma Cloud offers its customers the widest support in terms of API & Policy coverage when it comes to
Misconfiguration Detection and continuously endeavours to support new API.
The Cloud Accounts status page is intended to indicate any missing permissions that the customer must grant to Prisma Cloud and ensure
Visibility for the new API being supported. For some customers, the resulting ‘amber’ status of the cloud account gave an inaccurate picture
of their visibility posture.
With Consent Management, Prisma Cloud aims to -
Ensure that the Cloud account status(Starting with Config) is green as long as Prisma Cloud is able to ingest the API that is relevant to
the customer.
Give Customer a means to choose which API they would like Prisma Cloud to ingest for them.
Few of the salient points to note with regards to the roll out of the feature.
Prisma Cloud ingests metadata for an API only if customer has consented, else ignores.

Customers will have an option to choose any of the 3 modes for consent management- Manual Mode, Semi-Automatic Mode, Auto-
Consent Mode.

Auto-Consent mode-Customers who do not want to manage consent on a continuous basis can grant read-all type permissions to
Prisma Cloud. Prisma Cloud mark consent as Yes and auto-ingest every single API for all cloud types[AWS/Azure/GCP/OCI].
Manual Mode- Customers will be able to manage consent(Grant,Deny,Revoke) at an API level for each of their accounts and cloud
types on PC. Customer is able to Grant, Deny & Revoke consent at a cloud account+ Service+ API level within the product.
Semi- Automatic Mode- This will be applicable only for AWS, GCP & Azure cloud types. PC will automatically detect usage of
services from audit logs on the customer’s cloud accounts, mark the consent as Y. PC will ingest automatically if permissions are
present but will ask the customer to mark consent and grant permissions if permissions missing.
Ingestion status remains green for the customer as long as the ingestion is successful for the API’s they have consented.

Target Audience

This document is intended for all beta users as a starting point to use Palo Alto Networks’ Prisma Cloud’s consent management Auto-
Consent mode.

Assumptions
The following are some of the basic assumptions / expectations from you for the usage of this product.
1. Your organization has been invited to use the beta availability of the product and are in touch with a Sales / Support person of Prisma
Public Cloud.
2. You are familiar with Prisma Cloud’s CSPM features and have a good working knowledge of it.

3. You have onboarded your AWS/Azure/GCP/OCI Cloud accounts onto Prisma Cloud.
4. You are comfortable with granting ‘read-all’ type of permissions to Prisma Cloud.
5. Since its a beta release please be aware that the Prisma Cloud functionality may not be fully tested and may change by GA.
6. While the Auto-Consent Mode is intended to ensure that the Config Status of your cloud account status is kept in a compliant
status(green) with a one-time run of the CFT/TFT, do note that you may still need to run the CFT/TFT periodically when certain new API
require explicit read permissions which are outside the scope of the roles assumed by Prisma Cloud. This is typically a function of your
CSP’s IAM implementation.
7. All of the data which has been on board, used, created on the tenant in this environment will remain in this environment unless the
customer deletes it.

Day 1 requirement
The following are the basic and baseline requirements which are needed to use the Product.
1. AWS/Azure/GCP/ OCI Cloud accounts.
2. User with Administrator permissions in Cloud Account (To run the CFT/TFT).
3. If you are a new customer, it's recommended to have a presentation from Prisma Public Cloud sales / support on the usage of the
Product.
4. Login Details of Prisma Public Cloud(Permissions to onboard Cloud accounts)

Scope
The following sections explain the feature set and scope for Consent Management - Auto-Consent Mode.
Supported Regions
This feature is region-agnostic.

Getting Started
Following are the steps to start the beta access of the product.
1. Creation / availability of the AWS/Azure/GCP/OCI Cloud account onboarded onto Prisma Cloud
2. Python installed on your system,
3. Prisma Admin credentials
4. Admin Credentials on the CSP

Enabling Auto-Consent
1. You can enable Auto-Consent for a standalone account or for an Org construct on your CSP. Note that you cannot enable or disable
auto-consent individually for member-accounts inside an Org construct on your CSP.
2. Enable Auto-Consent by inputting the below details in the attached Enable_Auto_Consent.py script.
a. base_url
b. Prisma Admin user name & password
c. comma separated values of the cloud types and the account Id



3. Save and run the python script

4. On success, you will receive a message as shown.

5. Login to Prisma Cloud with your admin credentials and browse to Settings-> Cloud Accounts and edit the cloud account in question. It is
currently amber owing to warnings as shown below.

6. Edit the cloud account and download the CFT/TFT. The example below shows for AWS accounts. The process will be same for
Azure/GCP/OCI.

7. Login to your cloud account on the CSP and update the Prisma role using the downloaded CFT/TFT in the previous step.

8. Once the update is successful, revisit the edit flow of your cloud account on Prisma Cloud. The config status should have turned green.

9. The status should stay green even when Prisma Cloud releases support for new API since Prisma Cloud should automatically ingest the
new API.
Notes
1. While the Auto-Consent Mode is intended to ensure that the Config Status of your cloud account status is kept in a compliant
status(green) with a one-time run of the CFT/TFT, do note that you may still need to run the CFT/TFT periodically when certain new API

require explicit read permissions which are outside the scope of the roles assumed by Prisma Cloud. This is typically a function of your
CSP’s IAM implementation

Disabling Auto-Consent
1. You can disable Auto-Consent for a standalone account or for an Org construct on your CSP. Note that you cannot enable or disable
auto-consent individually for member-accounts inside an Org construct on your CSP.
2. Disable Auto-Consent by inputting the below details in the attached Disable_Auto_Consent.py script.
a. base_url
b. Prisma Admin user name & password
c. comma separated values of the cloud types and the account Id

3. Save and run the python script
4. Follow the steps 3-7 in the section above.
5. The prisma role on the CSP will now have the granular permissions and not have the read-all type of permissions. The cloud account
status(config) will initially be green but will turn amber once Prisma Cloud releases support for new API in the coming days.
