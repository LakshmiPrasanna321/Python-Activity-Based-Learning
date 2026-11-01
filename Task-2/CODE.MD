
### PROBLEM STATEMENT
 Campus Event Financial Planning: Calculate venue, equipment, catering, transport, and certificate costs; determine participant contributions, sponsorship shortfalls, and the minimum registration count needed to break even.

### ALGORITHM
1. Start
2. Input fixed costs - venue, equipment, transport
3. Input per person costs - catering, certificate
4. Input fee, sponsorship, participants
5. fixed = venue + equipment + transport
6. per_person_cost = catering + certificate
7. total_cost = fixed + per_person_cost _ n
8. total_income = sponsorship + fee _ n
9. shortfall = total_cost - total_income
10. break_even = (fixed - sponsorship) / (fee - per_person_cost)
11. Print all
12. Stop

```mermaid
### FLOWCHART (MERMAID)
flowchart TD
    A[Start] --> B[Input venue, equipment, transport, catering, certificate, fee, sponsorship, n]
    B --> C[fixed = venue+equipment+transport]
    C --> D[per_person = catering+certificate]
    D --> E[total_cost = fixed + per_person*n]
    E --> F[total_income = sponsorship + fee*n]
    F --> G[shortfall = total_cost - total_income]
    G --> H[break_even = (fixed-sponsorship)/(fee-per_person)]
    H --> I[Print total_cost, total_income, shortfall, break_even]
    I --> J[Stop]
```

### SAMPLE INPUT
Venue cost: 10000
Equipment cost: 5000
Transport cost: 3000
Catering per person: 150
Certificate per person: 20
Registration fee per person: 300
Sponsorship: 10000
No. of participants: 50
### SAMPLE OUTPUT
Total Cost: 26500
Total Income: 25000
Participant Contribution: 15000
Shortfall: 1500
Min. Registration to Break Even: 62
