# SmartSpend Anomaly Detector (GxP-Compliant)

A financial anomaly detection system built for regulated environments using Isolation Forest. Supports audit traceability, ALCOA+ data integrity, and real-time anomaly detection with full logging and validation documentation.

## 📦 Features
- Isolation Forest-based anomaly detection
- Audit logs with timestamps
- Plot of anomalies saved as PNG
- Output CSV with detected outliers
- GxP-aligned project structure and documentation
- ALCOA+ compliant: Attributable, Legible, Contemporaneous, etc.

## 📁 Project Structure
SmartSpend_AnomalyDetection_GxP/
├── src/ # Python script directory
│ └── Bank_Anomaly_Detection_System.py
├── input/ # Example input CSVs
│ └── Bank_sample_transactions.csv
├── output/ # Timestamped outputs (CSV + plot)
├── logs/ # Run logs for audit traceability
├── docs/ # GxP validation & documentation
│ ├── validation_report.pdf
│ ├── readme_GxP.md
│ └── change_log.txt
├── README.md
├── .gitignore
└── requirements.txt

## 🧪 Run the Script
```bash
cd src
python Bank_Anomaly_Detection_System.py
📄 Validation
See docs/validation_report.pdf for GxP compliance.

 GxP + ALCOA+ Compliance
    This system includes:
        Attributable: Logs are timestamped and written at run-time
        Legible: Outputs in standard CSV and PNG formats
        Contemporaneous: All logs and outputs written immediately
        Original: Source data is unmodified
        Accurate: Algorithm validated against test data
        Complete, Consistent, Enduring, Available
        Versioning
        v1.0 – Initial GxP-compliant release with logging, outputs, and validation

## 📄 License

This project is open for educational and validation purposes within audit, compliance, and regulated data workflows.

---

**Maintainer:** [@jbamigbade](https://github.com/jbamigbade) | SmartSpend Initiative

