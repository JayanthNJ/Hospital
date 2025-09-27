## Statistical Insights ##

**Analytics**

- The analytics sheet contains aggregated KPIs across departments and time.
- Key metrics include total_spending, avg_transaction_cost, transaction_count, and formulary_adherence_pct.
- These metrics are derived from transactional data and are suitable for trend and variance analysis.
- Total spending varies significantly by department, with a skew where a few departments account for most spend.
- The mean and median total_spending differ, indicating right-skewed distribution.
- This suggests focused cost-control in high-spend departments will yield outsized savings.
- Transaction counts show varying activity levels; some departments have very high transaction volumes.
- High-transaction departments also show higher quantity and spending patterns.
- Volume correlates with operational burden and needs targeted efficiency measures.
- Formulary adherence ranges broadly across departments with an average near mid-70s percent.
- Lower adherence departments contribute to higher cost variability.
- Standardizing formularies and decision support can improve adherence.
- Cost volatility (measured per department) highlights departments with unstable spend profiles.
- Seasonal demands and emergency responses often drive volatility.
- These areas benefit from fixed contracts and buffer stock strategies.
- Revenue_lost due to bounced prescriptions is non-trivial across departments.
- Aggregated revenue_lost represents leakage that impacts realized income.
- Addressing prescription bounce workflow reduces financial leakage.

**Hospital**

- There are 10+ departments with varying bed counts and monthly budgets.
- Department-level budgets are available to align resources with demand.
- Department granularity enables per-unit performance measurement.
- Physician roster includes over 100 physicians across specialties.
- Specialties show concentration in areas like cardiology and internal medicine.
- Experience distribution supports workforce planning and training.
- SKUs number over 1,000 items with some missing therapeutic metadata.
- Missing fields in SKUs (therapeutic_area, base_drug_name) affect clinical grouping.
- Completing SKU metadata improves procurement and formulary reporting.
- Vendor list includes ~50 vendors with lead time and fill rate metrics.
- Vendor performance metrics like average_lead_time_days and fill_rate_percentage are present.
- These enable vendor scorecards and procurement decisions.
- Data quality is generally good for hospital, departments, physicians, and vendors.
- However, SKU nulls require remediation before complex analytics.
- Implement MDM to ensure sustained data quality across the master.

**Inventory**

- Inventory dataset contains 1,197 SKU-level stock records across the hospital.
- Each record captures on-hand quantities, reorder thresholds, expiry, and batch information.
- This forms the operational source for replenishment and audits.
- Current_stock shows mean approx 42.9 units with wide dispersion.
- Min and max values indicate differing stocking strategies by SKU.
- Many SKUs are low-stock while few maintain high buffer stock.
- About 49 unique vendors supply inventory items, with the top vendor supplying ~17% of SKUs.
- Vendor concentration poses supply risk if a single vendor fails.
- Diversification or secondary sourcing is advised for critical SKUs.
- There are multiple SKUs flagged as Critical_Low indicating potential stockout exposures.
- Reorder_level and days_of_stock columns enable automated replenishment triggers.
- Critical items should be fast-tracked for reordering.
- Average days_to_expiry is several hundred days, but a subset of items approach near-expiry status.
- Batch-level expiry and FIFO/FEFO handling is available via batch_number and expiry_date.
- Prioritize near-expiry items for consumption or internal redistribution.
- Aggregated stock_value ties up significant working capital concentrated in a Pareto set of SKUs.
- Turnover rates show which items consume working capital faster.
- Optimizing stock_value reduces financial burden and improves liquidity.

**Patients**

- Patients dataset contains approximately 5,000 patient records with demographic and clinical data.
- Key fields include patient_type, age_group, chronic_conditions, insurance_type, and length_of_stay.
- This supports cohort analysis, utilization, and outcome studies.
- Age distribution is concentrated in adult groups (26-65) with the top age segments driving volume.
- Pediatric and geriatric volumes are smaller but require targeted capability.
- Age mix informs staffing and equipment allocation decisions.
- Outpatients constitute roughly 60% of encounters while inpatients account for ~40%.
- Outpatient growth drives visit volume and routine-revenue streams.
- Inpatient cases, although fewer, have higher per-patient resource intensity.
- Approximately 40% of patients have chronic conditions such as diabetes and hypertension.
- Chronic cohorts show higher readmission risk and longer LOS on average.
- Chronic-disease management programs can reduce utilization and improve outcomes.
- Average length_of_stay is around 6.3 days with wide variability across specialties.
- LOS correlates with complexity_score and presence of comorbidities.
- Reducing avoidable LOS increases bed availability and throughput.
- Average patient_complexity_score is mid-range (~52.6), indicating a mixed case-mix.
- Higher complexity patients disproportionately consume resources and lengthen stays.
- Risk stratification enables targeted case management and cost control.

**SupplyChain**

- Supply chain includes Purchase Orders and Deliveries with PO-level and delivery-level detail.
- Key fields include po_date, requested_delivery_date, ordered_quantity, unit_price, delivered_quantity, and quality ratings.
- This enables analysis of lead times, rejections, and delivery performance.
- Total PO spend is concentrated in certain categories with heterogeneous unit prices.
- High variance in unit_price across suppliers indicates negotiation opportunities.
- Category-level spend analysis will reveal priority negotiation targets.
- Delivery timeliness shows non-zero late deliveries; mean delay is material for planning.
- Late deliveries correlate with emergency procurement and stockouts.
- Vendor-level performance tracking is essential to reduce disruptions.
- Rejected quantities and rejections reasons surface supplier quality issues.
- Quality-related rejections drive extra costs and delays in usable stock.
- Supplier quality improvement programs can reduce these failures.
- PO status distribution reveals many POs in pending or partial states.
- Process bottlenecks in approval or fulfillment create aging POs.
- Automation and clearer SLAs can address PO aging.
- Market_condition and vendor_selection_reason fields provide context for urgent buys.
- These fields help explain price spikes and emergency sourcing decisions.
- Documenting rationale improves future procurement choices.

**Transactions**

- Transactions dataset contains patient- and SKU-level billing and consumption records.
- Key fields: transaction_date, quantity_consumed, unit_cost, total_cost, transaction_type, and formulary_adherent.
- This dataset underpins revenue cycle and cost analytics.
- Total_cost distribution is skewed with a small number of high-cost transactions driving a large share of revenue.
- Mean and median differ significantly, highlighting skew.
- Targeted review of high-cost claims protects margins.
- Top transaction types include consumption and purchase events with different cost profiles.
- Understanding transaction_type helps tailor billing and inventory policies.
- Some types correlate with higher urgency and higher unit costs.
- Formulary adherence rate is moderate; non-adherent items increase procurement unpredictability.
- Non-adherent prescribing often leads to higher-priced SKUs.
- Improving adherence reduces cost variance and improves forecasting.
- Bounce and revenue_lost fields quantify operational friction and financial leakage.
- Bounced transactions often stem from stockouts or authorization failures.
- Reducing bounces improves realization of billed services.
- Seasonality and urgency_level drive spikes in transaction volume and cost variability.
- Emergency-driven transactions are costlier and require contingency stock policies.
- Modeling seasonality aids budget and inventory planning.

## Business Insights ##

**Analytics**

- Use analytics to inform dynamic staffing and capacity planning.
- Seasonal peaks identified should drive temporary staffing and resource allocation.
- This reduces overcrowding and improves patient experience.
- Negotiate strategic procurement with high-spend departments to lock-in savings.
- Targeted formularies and preferred supplier lists reduce unit costs.
- Savings compound when applied to high-volume categories.
- Automate high-transaction workflows to reduce manual processing time.
- Automation improves accuracy in billing and inventory updates.
- It also frees staff for clinical duties.
- Deploy EMR nudges and formulary pop-ups to improve prescribing behavior.
- Measure adherence and provide feedback to prescribers.
- Incentivize departments that meet adherence targets.
- Insulate volatile spend areas with contracted pricing and safety stock.
- Use historical volatility to set procurement and safety stock rules.
- This reduces emergency procurements at premium costs.
- Fix bounced-prescription causes by integrating pharmacy checks in order flows.
- Track bounce reasons and address root causes (stock, formularies, auth).
- Reduced bounces increase realized revenue.

**Hospital**


- Use the hospital master as the authoritative source for reporting.
- Implement change control and stewardship to prevent divergence.
- This reduces downstream reconciliation needs and errors.
- Allocate budgets based on departmental utilization and outcomes.
- Redirect funds toward high-impact, high-demand services.
- Ensure smaller specialty units are appropriately funded for strategic value.
- Address physician specialty imbalances via hiring or redistribution.
- Support overloaded specialties with locum or targeted recruitment.
- Incentivize retention in high-demand areas.
- Remediate SKU metadata gaps by assigning data stewards and enrichment projects.
- Accurate SKU attributes improve formulary and pricing analytics.
- This also enhances procurement automation and compliance.
- Use vendor metrics to form preferred vendor lists and contingency plans.
- Favor vendors with strong fill rates for critical items.
- Negotiate SLAs and penalty clauses for repeated underperformance.
- Establish MDM and governance policies to lock in data quality.
- Periodic audits and KPIs ensure continued compliance.
- This improves trust in analytics and operational systems.

**Inventory**

- Automate reorder processes by integrating reorder_level and estimated_daily_consumption.
- This minimizes manual errors and speeds up replenishment cycles.
- Link reorder events to POs for auditability and tracking.
- Setup secondary suppliers for top-vendor dependent SKUs to mitigate single-supplier risk.
- Negotiate contingency agreements to secure critical items during disruptions.
- Regularly review vendor performance to re-balance sourcing.
- Establish safety stock and lead-time aware reorder points for critical SKUs.
- Use historical consumption and lead time variance to compute safety stock.
- This prevents emergency purchases at premium prices.
- Implement FEFO as default for expiry management and internal transfers.
- Run near-expiry campaigns and internal redistribution before write-offs.
- Track expiry trends to avoid recurring waste.
- Perform Pareto analysis on stock_value to prioritize negotiation and inventory reduction.
- Target high-value, low-turn SKUs for contract renegotiation or delisting.
- This frees working capital for critical supplies.
- Conduct regular cycle counts and reconciliations to align physical stock with records.
- Use exceptions from audits to improve receiving and handling processes.
- Accurate records reduce revenue leakage and clinical risk.

**Patients**

- Invest in chronic care pathways and follow-up clinics to reduce readmissions.
- Chronic programs create predictable appointment volumes and improve patient outcomes.
- They can also establish long-term revenue streams through repeat visits.
- Scale outpatient services, including telemedicine, to handle the volume efficiently.
- This reduces pressure on inpatient capacity and improves access for patients.
- Optimize clinic scheduling to balance load across the week.
- Use insurance mix data to prioritize billing, denials management, and patient counseling.
- Identify cohorts with high uninsured rates for financial assistance programs.
- Strengthen claims management processes to improve cash collections.
- Implement discharge planning and post-acute coordination to shorten LOS.
- Enhanced care coordination reduces readmissions and speeds up bed turnover.
- Invest in case managers for high-complexity patients.
- Segment patients by complexity and route them to appropriate care teams.
- High-complexity patients benefit from multidisciplinary care and proactive follow-up.
- This improves outcomes and optimizes resource use.
- Forecast demand based on demographic trends and plan capital investments accordingly.
- Align OR time, specialty clinics, and equipment procurement with projected needs.
- Avoid reactive, costly expansions by planning with data.

**SupplyChain**

- Digitize PO workflows and enforce SLAs for approvals to reduce PO aging.
- Faster approvals cut lead times and reduce emergency sourcing.
- Track PO aging KPIs and hold approvers accountable.
- Use spend analytics to consolidate categories and negotiate better terms.
- Category managers can aggregate demand to obtain scale discounts.
- Centralized procurement drives stronger supplier engagement.
- Hold underperforming vendors to improvement plans and consider delisting when necessary.
- Incorporate delivery performance into contract renewals.
- Maintain alternate suppliers for critical SKUs to ensure continuity.
- Strengthen incoming inspection and supplier quality agreements.
- Work with vendors on corrective actions for repeated rejections.
- Improve supplier onboarding to ensure quality from the outset.
- Automate PO-to-delivery matching and exceptions handling.
- This reduces manual effort and speeds reconciliation.
- Dashboards should highlight exceptions for rapid response.
- Record market conditions and rationale for spot buys to inform negotiation.
- Use historical evidence to justify future procurement strategies.
- Align purchasing with market intelligence for cost containment.

**Transactions**

- Audit high-cost transactions for coding accuracy and denial prevention.
- Ensure proper documentation to avoid revenue leakage.
- Regular audits protect net revenue and compliance.
- Implement formulary stewardship programs with EMR guidance to reduce non-adherent prescriptions.
- Provide prescribers with cost and formulary alternatives at point-of-care.
- Savings accumulate when adherence improves across volumes.
- Integrate real-time inventory checks into transaction entry to prevent bounces.
- This reduces rework, revenue_lost, and patient dissatisfaction.
- Improve integration between pharmacy, inventory, and order entry systems.
- Plan for seasonal demand by increasing buffer stocks for high-urgency SKUs.
- Align staffing and procurement timelines with predictable peaks.
- This avoids emergency procurements and reduces premium costs.
- Create exception workflows for high-urgency, high-cost items with pre-approved vendors.
- Negotiate emergency pricing or standing agreements for critical items.
- This reduces time-to-fill and cost uncertainty.
- Automate transaction-to-finance reconciliation to speed up revenue recognition.
- Use matching logic to connect transactions with payments and claims.
- This reduces monthly close effort and exposes revenue gaps quickly.







|Sl.No|	Dataset|	Statistical Insights|	Business Insights|
|-----|--------|------------------------|--------------------|
|1|	 Analytics |	"The analytics sheet contains aggregated KPIs across departments and time.Key metrics include total_spending, avg_transaction_cost, transaction_count, and formulary_adherence_pct.These metrics are derived from transactional data and are suitable for trend and variance analysis." |	"Use analytics to inform dynamic staffing and capacity planning.Seasonal peaks identified should drive temporary staffing and resource allocation.This reduces overcrowding and improves patient experience." |
2|	Analytics|	"Total spending varies significantly by department, with a skew where a few departments account for most spend.The mean and median total_spending differ, indicating right-skewed distribution.This suggests focused cost-control in high-spend departments will yield outsized savings."	|"Negotiate strategic procurement with high-spend departments to lock-in savings.Targeted formularies and preferred supplier lists reduce unit costs.Savings compound when applied to high-volume categories."|
3|	Analytics|	"Transaction counts show varying activity levels; some departments have very high transaction volumes.
High-transaction departments also show higher quantity and spending patterns.
Volume correlates with operational burden and needs targeted efficiency measures."	"Automate high-transaction workflows to reduce manual processing time.
Automation improves accuracy in billing and inventory updates.
It also frees staff for clinical duties."
4	Analytics	"Formulary adherence ranges broadly across departments with an average near mid-70s percent.
Lower adherence departments contribute to higher cost variability.
Standardizing formularies and decision support can improve adherence."	"Deploy EMR nudges and formulary pop-ups to improve prescribing behavior.
Measure adherence and provide feedback to prescribers.
Incentivize departments that meet adherence targets."
5	Analytics	"Cost volatility (measured per department) highlights departments with unstable spend profiles.
Seasonal demands and emergency responses often drive volatility.
These areas benefit from fixed contracts and buffer stock strategies."	"Insulate volatile spend areas with contracted pricing and safety stock.
Use historical volatility to set procurement and safety stock rules.
This reduces emergency procurements at premium costs."
6	Analytics	"Revenue_lost due to bounced prescriptions is non-trivial across departments.
Aggregated revenue_lost represents leakage that impacts realized income.
Addressing prescription bounce workflow reduces financial leakage."	"Fix bounced-prescription causes by integrating pharmacy checks in order flows.
Track bounce reasons and address root causes (stock, formularies, auth).
Reduced bounces increase realized revenue."
7	Hospital	"Hospital master links department, physician, SKU, and vendor entities.
It includes core attributes such as bed_capacity, annual_budget, and establishment_year.
This master supports cross-dataset joins and enterprise reporting."	"Use the hospital master as the authoritative source for reporting.
Implement change control and stewardship to prevent divergence.
This reduces downstream reconciliation needs and errors."
8	Hospital	"There are 10+ departments with varying bed counts and monthly budgets.
Department-level budgets are available to align resources with demand.
Department granularity enables per-unit performance measurement."	"Allocate budgets based on departmental utilization and outcomes.
Redirect funds toward high-impact, high-demand services.
Ensure smaller specialty units are appropriately funded for strategic value."
9	Hospital	"Physician roster includes over 100 physicians across specialties.
Specialties show concentration in areas like cardiology and internal medicine.
Experience distribution supports workforce planning and training."	"Address physician specialty imbalances via hiring or redistribution.
Support overloaded specialties with locum or targeted recruitment.
Incentivize retention in high-demand areas."
10	Hospital	"SKUs number over 1,000 items with some missing therapeutic metadata.
Missing fields in SKUs (therapeutic_area, base_drug_name) affect clinical grouping.
Completing SKU metadata improves procurement and formulary reporting."	"Remediate SKU metadata gaps by assigning data stewards and enrichment projects.
Accurate SKU attributes improve formulary and pricing analytics.
This also enhances procurement automation and compliance."
11	Hospital	"Vendor list includes ~50 vendors with lead time and fill rate metrics.
Vendor performance metrics like average_lead_time_days and fill_rate_percentage are present.
These enable vendor scorecards and procurement decisions."	"Use vendor metrics to form preferred vendor lists and contingency plans.
Favor vendors with strong fill rates for critical items.
Negotiate SLAs and penalty clauses for repeated underperformance."
12	Hospital	"Data quality is generally good for hospital, departments, physicians, and vendors.
However, SKU nulls require remediation before complex analytics.
Implement MDM to ensure sustained data quality across the master."	"Establish MDM and governance policies to lock in data quality.
Periodic audits and KPIs ensure continued compliance.
This improves trust in analytics and operational systems."
13	Inventory	"Inventory dataset contains 1,197 SKU-level stock records across the hospital.
Each record captures on-hand quantities, reorder thresholds, expiry, and batch information.
This forms the operational source for replenishment and audits."	"Automate reorder processes by integrating reorder_level and estimated_daily_consumption.
This minimizes manual errors and speeds up replenishment cycles.
Link reorder events to POs for auditability and tracking."
14	Inventory	"Current_stock shows mean approx 42.9 units with wide dispersion.
Min and max values indicate differing stocking strategies by SKU.
Many SKUs are low-stock while few maintain high buffer stock."	"Setup secondary suppliers for top-vendor dependent SKUs to mitigate single-supplier risk.
Negotiate contingency agreements to secure critical items during disruptions.
Regularly review vendor performance to re-balance sourcing."
15	Inventory	"About 49 unique vendors supply inventory items, with the top vendor supplying ~17% of SKUs.
Vendor concentration poses supply risk if a single vendor fails.
Diversification or secondary sourcing is advised for critical SKUs."	"Establish safety stock and lead-time aware reorder points for critical SKUs.
Use historical consumption and lead time variance to compute safety stock.
This prevents emergency purchases at premium prices."
16	Inventory	"There are multiple SKUs flagged as Critical_Low indicating potential stockout exposures.
Reorder_level and days_of_stock columns enable automated replenishment triggers.
Critical items should be fast-tracked for reordering."	"Implement FEFO as default for expiry management and internal transfers.
Run near-expiry campaigns and internal redistribution before write-offs.
Track expiry trends to avoid recurring waste."
17	Inventory	"Average days_to_expiry is several hundred days, but a subset of items approach near-expiry status.
Batch-level expiry and FIFO/FEFO handling is available via batch_number and expiry_date.
Prioritize near-expiry items for consumption or internal redistribution."	"Perform Pareto analysis on stock_value to prioritize negotiation and inventory reduction.
Target high-value, low-turn SKUs for contract renegotiation or delisting.
This frees working capital for critical supplies."
18	Inventory	"Aggregated stock_value ties up significant working capital concentrated in a Pareto set of SKUs.
Turnover rates show which items consume working capital faster.
Optimizing stock_value reduces financial burden and improves liquidity."	"Conduct regular cycle counts and reconciliations to align physical stock with records.
Use exceptions from audits to improve receiving and handling processes.
Accurate records reduce revenue leakage and clinical risk."
19	Patients	"Patients dataset contains approximately 5,000 patient records with demographic and clinical data.
Key fields include patient_type, age_group, chronic_conditions, insurance_type, and length_of_stay.
This supports cohort analysis, utilization, and outcome studies."	"Invest in chronic care pathways and follow-up clinics to reduce readmissions.
Chronic programs create predictable appointment volumes and improve patient outcomes.
They can also establish long-term revenue streams through repeat visits."
20	Patients	"Age distribution is concentrated in adult groups (26-65) with the top age segments driving volume.
Pediatric and geriatric volumes are smaller but require targeted capability.
Age mix informs staffing and equipment allocation decisions."	"Scale outpatient services, including telemedicine, to handle the volume efficiently.
This reduces pressure on inpatient capacity and improves access for patients.
Optimize clinic scheduling to balance load across the week."
21	Patients	"Outpatients constitute roughly 60% of encounters while inpatients account for ~40%.
Outpatient growth drives visit volume and routine-revenue streams.
Inpatient cases, although fewer, have higher per-patient resource intensity."	"Use insurance mix data to prioritize billing, denials management, and patient counseling.
Identify cohorts with high uninsured rates for financial assistance programs.
Strengthen claims management processes to improve cash collections."
22	Patients	"Approximately 40% of patients have chronic conditions such as diabetes and hypertension.
Chronic cohorts show higher readmission risk and longer LOS on average.
Chronic-disease management programs can reduce utilization and improve outcomes."	"Implement discharge planning and post-acute coordination to shorten LOS.
Enhanced care coordination reduces readmissions and speeds up bed turnover.
Invest in case managers for high-complexity patients."
23	Patients	"Average length_of_stay is around 6.3 days with wide variability across specialties.
LOS correlates with complexity_score and presence of comorbidities.
Reducing avoidable LOS increases bed availability and throughput."	"Segment patients by complexity and route them to appropriate care teams.
High-complexity patients benefit from multidisciplinary care and proactive follow-up.
This improves outcomes and optimizes resource use."
24	Patients	"Average patient_complexity_score is mid-range (~52.6), indicating a mixed case-mix.
Higher complexity patients disproportionately consume resources and lengthen stays.
Risk stratification enables targeted case management and cost control."	"Forecast demand based on demographic trends and plan capital investments accordingly.
Align OR time, specialty clinics, and equipment procurement with projected needs.
Avoid reactive, costly expansions by planning with data."
25	SupplyChain	"Supply chain includes Purchase Orders and Deliveries with PO-level and delivery-level detail.
Key fields include po_date, requested_delivery_date, ordered_quantity, unit_price, delivered_quantity, and quality ratings.
This enables analysis of lead times, rejections, and delivery performance."	"Digitize PO workflows and enforce SLAs for approvals to reduce PO aging.
Faster approvals cut lead times and reduce emergency sourcing.
Track PO aging KPIs and hold approvers accountable."
26	SupplyChain	"Total PO spend is concentrated in certain categories with heterogeneous unit prices.
High variance in unit_price across suppliers indicates negotiation opportunities.
Category-level spend analysis will reveal priority negotiation targets."	"Use spend analytics to consolidate categories and negotiate better terms.
Category managers can aggregate demand to obtain scale discounts.
Centralized procurement drives stronger supplier engagement."
27	SupplyChain	"Delivery timeliness shows non-zero late deliveries; mean delay is material for planning.
Late deliveries correlate with emergency procurement and stockouts.
Vendor-level performance tracking is essential to reduce disruptions."	"Hold underperforming vendors to improvement plans and consider delisting when necessary.
Incorporate delivery performance into contract renewals.
Maintain alternate suppliers for critical SKUs to ensure continuity."
28	SupplyChain	"Rejected quantities and rejections reasons surface supplier quality issues.
Quality-related rejections drive extra costs and delays in usable stock.
Supplier quality improvement programs can reduce these failures."	"Strengthen incoming inspection and supplier quality agreements.
Work with vendors on corrective actions for repeated rejections.
Improve supplier onboarding to ensure quality from the outset."
29	SupplyChain	"PO status distribution reveals many POs in pending or partial states.
Process bottlenecks in approval or fulfillment create aging POs.
Automation and clearer SLAs can address PO aging."	"Automate PO-to-delivery matching and exceptions handling.
This reduces manual effort and speeds reconciliation.
Dashboards should highlight exceptions for rapid response."
30	SupplyChain	"Market_condition and vendor_selection_reason fields provide context for urgent buys.
These fields help explain price spikes and emergency sourcing decisions.
Documenting rationale improves future procurement choices."	"Record market conditions and rationale for spot buys to inform negotiation.
Use historical evidence to justify future procurement strategies.
Align purchasing with market intelligence for cost containment."
31	Transactions	"Transactions dataset contains patient- and SKU-level billing and consumption records.
Key fields: transaction_date, quantity_consumed, unit_cost, total_cost, transaction_type, and formulary_adherent.
This dataset underpins revenue cycle and cost analytics."	"Audit high-cost transactions for coding accuracy and denial prevention.
Ensure proper documentation to avoid revenue leakage.
Regular audits protect net revenue and compliance."
32	Transactions	"Total_cost distribution is skewed with a small number of high-cost transactions driving a large share of revenue.
Mean and median differ significantly, highlighting skew.
Targeted review of high-cost claims protects margins."	"Implement formulary stewardship programs with EMR guidance to reduce non-adherent prescriptions.
Provide prescribers with cost and formulary alternatives at point-of-care.
Savings accumulate when adherence improves across volumes."
33	Transactions	"Top transaction types include consumption and purchase events with different cost profiles.
Understanding transaction_type helps tailor billing and inventory policies.
Some types correlate with higher urgency and higher unit costs."	"Integrate real-time inventory checks into transaction entry to prevent bounces.
This reduces rework, revenue_lost, and patient dissatisfaction.
Improve integration between pharmacy, inventory, and order entry systems."
34	Transactions	"Formulary adherence rate is moderate; non-adherent items increase procurement unpredictability.
Non-adherent prescribing often leads to higher-priced SKUs.
Improving adherence reduces cost variance and improves forecasting."	"Plan for seasonal demand by increasing buffer stocks for high-urgency SKUs.
Align staffing and procurement timelines with predictable peaks.
This avoids emergency procurements and reduces premium costs."
35	Transactions	"Bounce and revenue_lost fields quantify operational friction and financial leakage.
Bounced transactions often stem from stockouts or authorization failures.
Reducing bounces improves realization of billed services."	"Create exception workflows for high-urgency, high-cost items with pre-approved vendors.
Negotiate emergency pricing or standing agreements for critical items.
This reduces time-to-fill and cost uncertainty."
36	Transactions	"Seasonality and urgency_level drive spikes in transaction volume and cost variability.
Emergency-driven transactions are costlier and require contingency stock policies.
Modeling seasonality aids budget and inventory planning."	"Automate transaction-to-finance reconciliation to speed up revenue recognition.
Use matching logic to connect transactions with payments and claims.
This reduces monthly close effort and exposes revenue gaps quickly."
