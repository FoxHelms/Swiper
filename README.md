# Swiper (no swiping!)

A distributed payment-as-a-microservice system. 

```
                +--------------------+
                |   Mobile/Web App   |
                +---------+----------+
                          |
                          v
              +-----------+-----------+
              |   API Gateway (REST)  | 
              +-----------+-----------+
                          |
          +---------------+---------------------+
          |                                     |
          v                                     v
+---------------------+             +------------------------+
| Payment Service     |             | User Wallet Service    |
| - Validates payment |             | - Balance management   |
| - Orchestrates flow |             | - Lock/unlock funds    |
+---------+-----------+             +-----------+------------+
          |                                     |
          v                                     v
+---------------------+             +------------------------+
| Kafka Payment Topic | ←--- Events & transactions →         |
+---------+-----------+             +-----------+------------+
          |                                     |
          v                                     v
+---------------------+             +------------------------+
| Fraud Detection     |             | Ledger Service         |
| Service             |             | - Append-only log      |
| - Real-time checks  |             | - Settlement tracking  |
+---------------------+             +------------------------+

                  |
                  v
       +----------+-----------+
       | PostgreSQL/Cassandra|
       | - Ledger DB         |
       +---------------------+

                  |
                  v
       +----------+-----------+
       | Grafana + Prometheus |
       | - Monitoring         |
       +---------------------+


```
